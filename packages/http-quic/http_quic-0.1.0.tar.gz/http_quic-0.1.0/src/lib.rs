use pyo3::prelude::*;

/// Formats the sum of two numbers as string.
#[pyfunction]
fn check_tls_certificate(certificate_path: String) -> PyResult<String> {
    Ok("".to_string())
}

/// A Python module implemented in Rust.
#[pymodule]
fn http_quic(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(check_tls_certificate, m)?)?;
    Ok(())
}
