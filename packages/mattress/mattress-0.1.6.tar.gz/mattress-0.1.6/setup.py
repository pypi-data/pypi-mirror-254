"""Setup file for mattress. Use setup.cfg to configure your project.

This file was generated with PyScaffold 4.5.
PyScaffold helps you to put up the scaffold of your new Python project.
Learn more under: https://pyscaffold.org/
"""
from setuptools import setup
from setuptools.extension import Extension
import assorthead

if __name__ == "__main__":
    try:
        setup(
            use_scm_version={"version_scheme": "no-guess-dev"},
            ext_modules=[
                Extension(
                    "mattress._core",
                    [
                        "src/mattress/lib/dense.cpp",
                        "src/mattress/lib/compressed_sparse.cpp",
                        "src/mattress/lib/delayed_binary_isometric_op.cpp",
                        "src/mattress/lib/delayed_unary_isometric_op_simple.cpp",
                        "src/mattress/lib/delayed_unary_isometric_op_with_args.cpp",
                        "src/mattress/lib/delayed_subset.cpp",
                        "src/mattress/lib/delayed_combine.cpp",
                        "src/mattress/lib/delayed_transpose.cpp",
                        "src/mattress/lib/common.cpp",
                        "src/mattress/lib/bindings.cpp",
                    ],
                    include_dirs=[
                        assorthead.includes(),
                        "src/mattress/include",
                    ],
                    language="c++",
                    extra_compile_args=[
                        "-std=c++17",
                    ],
                )
            ],
        )
    except:  # noqa
        print(
            "\n\nAn error occurred while building the project, "
            "please ensure you have the most updated version of setuptools, "
            "setuptools_scm and wheel with:\n"
            "   pip install -U setuptools setuptools_scm wheel\n\n"
        )
        raise
