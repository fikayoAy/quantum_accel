from setuptools import setup, find_packages
from setuptools_rust import Binding, RustExtension

setup(
    name="quantum_accel",
    version="0.1.0",
    packages=["Optimized_quantum_gates"],  # Explicitly list packages
    include_package_data=True,
    rust_extensions=[
        RustExtension("quantum_accel", 
                      path="quantum_accel/Cargo.toml",
                      binding=Binding.PyO3)
    ],
    install_requires=[
        "numpy>=1.20.0",
    ],
    python_requires=">=3.7",
    zip_safe=False,
)