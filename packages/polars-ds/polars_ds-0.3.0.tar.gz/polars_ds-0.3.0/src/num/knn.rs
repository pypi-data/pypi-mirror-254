/// Performs KNN related search queries, classification and regression, and
/// other features/entropies that require KNN to be efficiently computed.
use super::which_distance;
use crate::list_u64_output;
use itertools::Itertools;
use kdtree::KdTree;
use ndarray::{ArrayView2, Axis};
use polars::prelude::*;
use pyo3_polars::export::polars_core::utils::rayon::iter::{
    FromParallelIterator, IntoParallelIterator, ParallelBridge,
};
use pyo3_polars::{
    derive::polars_expr,
    export::polars_core::utils::rayon::iter::{IndexedParallelIterator, ParallelIterator},
};
use serde::Deserialize;

#[derive(Deserialize, Debug)]
pub(crate) struct KdtreeKwargs {
    pub(crate) k: usize,
    pub(crate) leaf_size: usize,
    pub(crate) metric: String,
    pub(crate) parallel: bool,
}

#[derive(Deserialize, Debug)]
pub(crate) struct KdtreeRadiusKwargs {
    pub(crate) r: f64,
    pub(crate) leaf_size: usize,
    pub(crate) metric: String,
    pub(crate) parallel: bool,
}

#[inline]
pub fn build_standard_kdtree<'a>(
    dim: usize,
    leaf_size: usize,
    data: &'a ArrayView2<f64>,
) -> Result<KdTree<f64, usize, &'a [f64]>, PolarsError> {
    // Building the tree
    let mut tree = KdTree::with_capacity(dim, leaf_size);
    for (i, p) in data.rows().into_iter().enumerate() {
        let s = p.to_slice().unwrap(); // C order makes sure rows are contiguous
        let _is_ok = tree
            .add(s, i)
            .map_err(|e| PolarsError::ComputeError(e.to_string().into()))?;
    }
    Ok(tree)
}

pub fn knn_full_output(_: &[Field]) -> PolarsResult<Field> {
    let idx = Field::new("idx", DataType::List(Box::new(DataType::UInt64)));

    let dist = Field::new("dist", DataType::List(Box::new(DataType::Float64)));
    let v = vec![idx, dist];
    Ok(Field::new("knn_w_dist", DataType::Struct(v)))
}

#[polars_expr(output_type_func=list_u64_output)]
fn pl_knn_ptwise(inputs: &[Series], kwargs: KdtreeKwargs) -> PolarsResult<Series> {
    // Set up params
    let id = inputs[0].u64()?;

    let dim = inputs[1..].len();
    if dim == 0 {
        return Err(PolarsError::ComputeError(
            "KNN: No column to decide distance from.".into(),
        ));
    }
    let mut vs: Vec<Series> = Vec::with_capacity(dim);
    for (i, s) in inputs[1..].into_iter().enumerate() {
        let news = s.rechunk().with_name(&i.to_string());
        vs.push(news)
    }
    let data = DataFrame::new(vs)?;
    let k = kwargs.k;
    let leaf_size = kwargs.leaf_size;
    let parallel = kwargs.parallel;
    let dist_func = which_distance(kwargs.metric.as_str(), dim)?;

    // Need to use C order because C order is row-contiguous
    let data = data.to_ndarray::<Float64Type>(IndexOrder::C)?;

    // Building the tree
    let binding = data.view();
    let tree = build_standard_kdtree(dim, leaf_size, &binding)?;

    // Building output
    let mut builder =
        ListPrimitiveChunkedBuilder::<UInt64Type>::new("", id.len(), k + 1, DataType::UInt64);
    if parallel {
        let mut nbs: Vec<Option<Vec<u64>>> = Vec::with_capacity(id.len());
        data.axis_iter(Axis(0))
            .into_par_iter()
            .map(|p| {
                let s = p.to_slice().unwrap(); // C order makes sure rows are contiguous
                if let Ok(v) = tree.nearest(s, k + 1, &dist_func) {
                    // By construction, this unwrap is safe.
                    // k+ 1 because we include the point itself, and ask for k more neighbors.
                    Some(
                        v.into_iter()
                            .map(|(_, i)| id.get(*i).unwrap())
                            .collect_vec(),
                    )
                } else {
                    None
                }
            })
            .collect_into_vec(&mut nbs);
        for op_s in nbs {
            if let Some(s) = op_s {
                builder.append_slice(&s);
            } else {
                builder.append_null();
            }
        }
    } else {
        for p in data.rows() {
            let s = p.to_slice().unwrap(); // C order makes sure rows are contiguous
            if let Ok(v) = tree.nearest(s, k + 1, &dist_func) {
                // By construction, this unwrap is safe
                let w: Vec<u64> = v
                    .into_iter()
                    .map(|(_, i)| id.get(*i).unwrap())
                    .collect_vec();
                builder.append_slice(w.as_slice());
            } else {
                builder.append_null();
            }
        }
    }
    let ca = builder.finish();
    Ok(ca.into_series())
}

#[polars_expr(output_type_func=list_u64_output)]
fn pl_query_radius_ptwise(inputs: &[Series], kwargs: KdtreeRadiusKwargs) -> PolarsResult<Series> {
    // Set up params
    let id = inputs[0].u64()?;
    let id = id.rechunk();
    let sl = id.cont_slice()?;

    let dim = inputs[1..].len();
    if dim == 0 {
        return Err(PolarsError::ComputeError(
            "KNN: No column to decide distance from.".into(),
        ));
    }
    let mut vs: Vec<Series> = Vec::with_capacity(dim);
    for (i, s) in inputs[1..].into_iter().enumerate() {
        let news = s.rechunk().with_name(&i.to_string());
        vs.push(news)
    }
    let data = DataFrame::new(vs)?;
    let leaf_size = kwargs.leaf_size;
    let parallel = kwargs.parallel;
    let radius = kwargs.r;
    let dist_func = which_distance(kwargs.metric.as_str(), dim)?;

    // Need to use C order because C order is row-contiguous
    let data = data.to_ndarray::<Float64Type>(IndexOrder::C)?;

    // Building the tree
    let binding = data.view();
    let tree = build_standard_kdtree(dim, leaf_size, &binding)?;

    // Building output
    if parallel {
        let out_par_iter = data.axis_iter(Axis(0)).into_par_iter().map(|p| {
            let s = p.to_slice().unwrap(); // C order makes sure rows are contiguous
            if let Ok(v) = tree.iter_nearest(s, &dist_func) {
                let out = v.take_while(|(d, _)| d <= &radius).map(|(_, i)| sl[*i]);
                let ca = UInt64Chunked::from_iter_values("", out);
                Some(ca.into_series())
            } else {
                None
            }
        });
        let ca = ListChunked::from_par_iter(out_par_iter);
        Ok(ca.into_series())
    } else {
        let mut builder =
            ListPrimitiveChunkedBuilder::<UInt64Type>::new("", id.len(), 16, DataType::UInt64);
        for p in data.rows() {
            let s = p.to_slice().unwrap(); // C order makes sure rows are contiguous
            if let Ok(v) = tree.iter_nearest(s, &dist_func) {
                let mut out: Vec<u64> = v
                    .take_while(|(d, _)| d <= &radius)
                    .map(|(_, i)| id.get(*i).unwrap())
                    .collect();
                out.shrink_to_fit();
                builder.append_slice(&out);
            } else {
                builder.append_null();
            }
        }
        let ca = builder.finish();
        Ok(ca.into_series())
    }
}

#[polars_expr(output_type_func=knn_full_output)]
fn pl_knn_ptwise_w_dist(inputs: &[Series], kwargs: KdtreeKwargs) -> PolarsResult<Series> {
    // Set up params
    let id = inputs[0].u64()?;
    let dim = inputs[1..].len();
    if dim == 0 {
        return Err(PolarsError::ComputeError(
            "KNN: No column to decide distance from.".into(),
        ));
    }
    let mut vs: Vec<Series> = Vec::with_capacity(dim);
    for (i, s) in inputs[1..].into_iter().enumerate() {
        let news = s.rechunk().with_name(&i.to_string());
        vs.push(news)
    }
    let data = DataFrame::new(vs)?;
    let k = kwargs.k;
    let leaf_size = kwargs.leaf_size;
    let parallel = kwargs.parallel;
    let dist_func = which_distance(kwargs.metric.as_str(), dim)?;

    // Need to use C order because C order is row-contiguous
    let data = data.to_ndarray::<Float64Type>(IndexOrder::C)?;

    // Building the tree
    let binding = data.view();
    let tree = build_standard_kdtree(dim, leaf_size, &binding)?;

    // Building output
    let mut builder =
        ListPrimitiveChunkedBuilder::<UInt64Type>::new("", id.len(), k + 1, DataType::UInt64);

    let mut builder_dist =
        ListPrimitiveChunkedBuilder::<Float64Type>::new("", id.len(), k + 1, DataType::Float64);

    if parallel {
        let mut nbs: Vec<(Option<Vec<u64>>, Option<Vec<f64>>)> = Vec::with_capacity(id.len());
        data.axis_iter(Axis(0))
            .into_par_iter()
            .map(|p| {
                let s = p.to_slice().unwrap(); // C order makes sure rows are contiguous
                if let Ok(v) = tree.nearest(s, k + 1, &dist_func) {
                    // k+ 1 because we include the point itself, and ask for k more neighbors.
                    let mut w_idx: Vec<u64> = Vec::with_capacity(k + 1);
                    let mut w_dist: Vec<f64> = Vec::with_capacity(k + 1);
                    // By construction, this unwrap is safe.
                    for (d, i) in v.into_iter() {
                        w_idx.push(id.get(*i).unwrap());
                        w_dist.push(d);
                    }
                    (Some(w_idx), Some(w_dist))
                } else {
                    (None, None)
                }
            })
            .collect_into_vec(&mut nbs);
        for (op_s, op_d) in nbs {
            if let (Some(s), Some(d)) = (op_s, op_d) {
                builder.append_slice(&s);
                builder_dist.append_slice(&d);
            } else {
                builder.append_null();
                builder_dist.append_null();
            }
        }
    } else {
        for p in data.rows() {
            let s = p.to_slice().unwrap(); // C order makes sure rows are contiguous
            if let Ok(v) = tree.nearest(s, k + 1, &dist_func) {
                // By construction, this unwrap is safe
                let mut w_idx: Vec<u64> = Vec::with_capacity(k + 1);
                let mut w_dist: Vec<f64> = Vec::with_capacity(k + 1);
                for (d, i) in v.into_iter() {
                    w_idx.push(id.get(*i).unwrap());
                    w_dist.push(d);
                }
                builder.append_slice(&w_idx);
                builder_dist.append_slice(&w_dist);
            } else {
                builder.append_null();
            }
        }
    }
    let ca1 = builder.finish();
    let indices = ca1.with_name("idx").into_series();
    let ca2 = builder_dist.finish();
    let distances = ca2.with_name("dist").into_series();
    let out = StructChunked::new("knn_full_output", &[indices, distances])?;
    Ok(out.into_series())
}

/// Find all the rows that are the k-nearest neighbors to the point given.
/// Note, only k points will be returned as true, because here the point is considered an "outside" point,
/// not a point in the data.
#[polars_expr(output_type=Boolean)]
fn pl_knn_pt(inputs: &[Series], kwargs: KdtreeKwargs) -> PolarsResult<Series> {
    // Check len
    let pt = inputs[0].f64()?;
    let dim = inputs[1..].len();
    if dim == 0 || pt.len() != dim {
        return Err(PolarsError::ComputeError(
            "KNN: There has to be at least one column in `others` and input point \
            must be the same dimension as the number of columns in `others`."
                .into(),
        ));
    }
    // Set up the point to query
    let binding = pt.rechunk();
    let p = binding.cont_slice()?;
    // Set up params
    let mut vs: Vec<Series> = Vec::with_capacity(dim);
    for (i, s) in inputs[1..].into_iter().enumerate() {
        let news = s.rechunk().with_name(&i.to_string());
        vs.push(news)
    }
    let data = DataFrame::new(vs)?;
    let nrows = data.height();
    let dim = inputs[1..].len();
    let k = kwargs.k;
    let leaf_size = kwargs.leaf_size;
    let dist_func = which_distance(kwargs.metric.as_str(), dim)?;

    // Need to use C order because C order is row-contiguous
    let data = data.to_ndarray::<Float64Type>(IndexOrder::C)?;

    // Building the tree
    let binding = data.view();
    let tree = build_standard_kdtree(dim, leaf_size, &binding)?;

    // Building the output
    let mut out: Vec<bool> = vec![false; nrows];
    match tree.nearest(p, k, &dist_func) {
        Ok(v) => {
            for (_, i) in v.into_iter() {
                out[*i] = true;
            }
        }
        Err(e) => {
            return Err(PolarsError::ComputeError(
                ("KNN: ".to_owned() + e.to_string().as_str()).into(),
            ));
        }
    }
    Ok(BooleanChunked::from_slice("", &out).into_series())
}

/// Neighbor count query
#[inline]
pub fn query_nb_cnt<F>(
    tree: &KdTree<f64, usize, &[f64]>,
    data: ArrayView2<f64>,
    dist_func: &F,
    r: f64,
    parallel: bool,
) -> UInt32Chunked
where
    F: Fn(&[f64], &[f64]) -> f64 + std::marker::Sync,
{
    if parallel {
        UInt32Chunked::from_par_iter(data.axis_iter(Axis(0)).into_par_iter().map(|pt| {
            let s = pt.to_slice().unwrap(); // C order makes sure rows are contiguous
            if let Ok(v) = tree.within(s, r, dist_func) {
                Some(v.len() as u32)
            } else {
                None
            }
        }))
    } else {
        UInt32Chunked::from_iter(data.axis_iter(Axis(0)).map(|pt| {
            let s = pt.to_slice().unwrap(); // C order makes sure rows are contiguous
            if let Ok(v) = tree.within(s, r, dist_func) {
                Some(v.len() as u32)
            } else {
                None
            }
        }))
    }
}

/// For every point in this dataframe, find the number of neighbors within radius r
/// The point itself is always considered as a neighbor to itself.
#[polars_expr(output_type=UInt32)]
fn pl_nb_cnt(inputs: &[Series], kwargs: KdtreeKwargs) -> PolarsResult<Series> {
    // Set up radius
    let radius = inputs[0].f64()?;

    // Set up params
    let dim = inputs[1..].len();
    if dim == 0 {
        return Err(PolarsError::ComputeError(
            "KNN: No column to decide distance from.".into(),
        ));
    }

    let mut vs: Vec<Series> = Vec::with_capacity(dim);
    for (i, s) in inputs[1..].into_iter().enumerate() {
        let news = s.rechunk().with_name(&i.to_string());
        vs.push(news)
    }
    let data = DataFrame::new(vs)?;
    let nrows = data.height();
    let parallel = kwargs.parallel;
    let leaf_size = kwargs.leaf_size;
    let dist_func = which_distance(kwargs.metric.as_str(), dim)?;
    // Need to use C order because C order is row-contiguous
    let data = data.to_ndarray::<Float64Type>(IndexOrder::C)?;

    // Building the tree
    let binding = data.view();
    let tree = build_standard_kdtree(dim, leaf_size, &binding)?;

    if radius.len() == 1 {
        let r = radius.get(0).unwrap();
        let ca = query_nb_cnt(&tree, data.view(), &dist_func, r, parallel);
        Ok(ca.into_series())
    } else if radius.len() == nrows {
        if parallel {
            let ca = UInt32Chunked::from_par_iter(
                radius
                    .into_iter()
                    .zip(data.axis_iter(Axis(0)))
                    .par_bridge()
                    .map(|(rad, pt)| {
                        let r = rad?;
                        let s = pt.to_slice().unwrap(); // C order makes sure rows are contiguous
                        if let Ok(v) = tree.within(s, r, &dist_func) {
                            Some(v.len() as u32)
                        } else {
                            None
                        }
                    }),
            );
            Ok(ca.into_series())
        } else {
            let ca = UInt32Chunked::from_iter(radius.into_iter().zip(data.axis_iter(Axis(0))).map(
                |(rad, pt)| {
                    let r = rad?;
                    let s = pt.to_slice().unwrap(); // C order makes sure rows are contiguous
                    if let Ok(v) = tree.within(s, r, &dist_func) {
                        Some(v.len() as u32)
                    } else {
                        None
                    }
                },
            ));
            Ok(ca.into_series())
        }
    } else {
        Err(PolarsError::ShapeMismatch(
            "Inputs must have the same length or one of them must be a scalar.".into(),
        ))
    }
}
