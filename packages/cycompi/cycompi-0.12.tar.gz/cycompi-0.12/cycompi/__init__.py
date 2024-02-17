import sys
import base64
import pickle
import subprocess


def loadargs(compdi):
    """
    Decode the base64-encoded input and load the resulting data using pickle.
    """
    compdi = base64.b64decode(compdi.encode())
    return pickle.loads(compdi)

name=''
if __name__ == "__main__":
    if "--inplace" in sys.argv:
        optionsdict = {}

        compdi = loadargs(sys.argv[-1])

        optionsdict = loadargs(sys.argv[-2])
        clidict = loadargs(sys.argv[-3])
        name=sys.argv[-4].strip('\'" ')
        sys.argv = sys.argv[:-4]
        from Cython.Compiler import Options
        import re

        for key, value in optionsdict.items():
            check1 = re.findall(r"^Options\.[a-z_]+$", str(key))
            check2 = re.findall(r"^(True|False|\d+)$", str(value))
            if check1 and check2:
                exec(f"{key} = {value}", globals())


def dumpdict(configdict):
    """
    Function to dump a dictionary to a base64 encoded string.

    Args:
        configdict (dict): The dictionary to be dumped.

    Returns:
        str: The base64 encoded string representation of the dictionary.
    """
    testdictbytes = pickle.dumps(configdict)
    return base64.b64encode(testdictbytes).decode("utf-8")


def compile_cython_code(name,configdict, optionsdict, cmd_line_args, **kwargs):
    """
    Compile Cython code using the provided configuration, options, and command line arguments.
    :param name: name of the module 
    :param configdict: dictionary containing configuration settings (passed to setuptools.Extension)
    :param optionsdict: dictionary containing options settings (passed to Cython.Compiler.Options)
    :param cmd_line_args: command line arguments (passed to setup as compiler_directives)
    :param **kwargs: additional keyword arguments to be passed to subprocess.run

    :return: None

    Example usage:
        from cycompi import compile_cython_code
        import numpy as np
        import os

        numpyincludefolder = np.get_include()

        optionsdict = {
            "Options.docstrings": False,
            "Options.embed_pos_in_docstring": False,
            "Options.generate_cleanup_code": False,
            "Options.clear_to_none": True,
            "Options.annotate": True,
            "Options.fast_fail": False,
            "Options.warning_errors": False,
            "Options.error_on_unknown_names": True,
            "Options.error_on_uninitialized": True,
            "Options.convert_range": True,
            "Options.cache_builtins": True,
            "Options.gcc_branch_hints": True,
            "Options.lookup_module_cpdef": False,
            "Options.embed": False,
            "Options.cimport_from_pyx": False,
            "Options.buffer_max_dims": 8,
            "Options.closure_freelist_size": 8,
        }
        configdict = {
            "py_limited_api": False,
            "name": "cythondict",
            "sources": ["lookdi.pyx"],
            "include_dirs": [numpyincludefolder],
            "define_macros": [
                ("NPY_NO_DEPRECATED_API", 1),
                ("NPY_1_7_API_VERSION", 1),
                ("CYTHON_USE_DICT_VERSIONS", 1),
                ("CYTHON_FAST_GIL", 1),
                ("CYTHON_USE_PYLIST_INTERNALS", 1),
                ("CYTHON_USE_UNICODE_INTERNALS", 1),
                ("CYTHON_ASSUME_SAFE_MACROS", 1),
                ("CYTHON_USE_TYPE_SLOTS", 1),
                ("CYTHON_USE_PYTYPE_LOOKUP", 1),
                ("CYTHON_USE_ASYNC_SLOTS", 1),
                ("CYTHON_USE_PYLONG_INTERNALS", 1),
                ("CYTHON_USE_UNICODE_WRITER", 1),
                ("CYTHON_UNPACK_METHODS", 1),
                ("CYTHON_USE_EXC_INFO_STACK", 1),
                ("CYTHON_ATOMICS", 1),
            ],
            "undef_macros": [],
            "library_dirs": [],
            "libraries": [],
            "runtime_library_dirs": [],
            "extra_objects": [],
            "extra_compile_args": ["/O2", "/Oy"],
            "extra_link_args": [],
            "export_symbols": [],
            "swig_opts": [],
            "depends": [],
            "language": "c",
            "optional": None,
        }
        compiler_directives = {
            "binding": True,
            "boundscheck": False,
            "wraparound": False,
            "initializedcheck": False,
            "nonecheck": False,
            "overflowcheck": False,
            "overflowcheck.fold": True,
            "embedsignature": False,
            "embedsignature.format": "c",  # (c / python / clinic)
            "cdivision": True,
            "cdivision_warnings": False,
            "cpow": True,
            "always_allow_keywords": False,
            "c_api_binop_methods": False,
            "profile": False,
            "linetrace": False,
            "infer_types": True,
            "language_level": 3,  # (2/3/3str)
            "c_string_type": "bytes",  # (bytes / str / unicode)
            "c_string_encoding": "default",  # (ascii, default, utf-8, etc.)
            "type_version_tag": False,
            "unraisable_tracebacks": True,
            "iterable_coroutine": True,
            "annotation_typing": True,
            "emit_code_comments": True,
            "cpp_locals": False,
            "legacy_implicit_noexcept": False,
            "optimize.use_switch": True,
            "optimize.unpack_method_calls": True,
            "warn.undeclared": False,  # (default False)
            "warn.unreachable": True,  # (default True)
            "warn.maybe_uninitialized": False,  # (default False)
            "warn.unused": False,  # (default False)
            "warn.unused_arg": False,  # (default False)
            "warn.unused_result": False,  # (default False)
            "warn.multiple_declarators": True,  # (default True)
            "show_performance_hints": True,  # (default True)
        }

        compile_cython_code(
            name="lookdi",
            configdict=configdict,
            optionsdict=optionsdict,
            cmd_line_args=compiler_directives,
            cwd=os.getcwd(),
            shell=True,
            env=os.environ.copy(),
        )


    """
    testdictbytesbase64 = dumpdict(configdict)
    optiondictbytesbase64 = dumpdict(optionsdict)
    clidictbytesbase64 = dumpdict(cmd_line_args)

    subprocess.run(
        [
            sys.executable,
            __file__,
            "build_ext",
            "--inplace",
            name,
            clidictbytesbase64,
            optiondictbytesbase64,
            testdictbytesbase64,
        ],
        **kwargs,
    )


if __name__ == "__main__":
    from setuptools import Extension, setup
    from Cython.Build import cythonize

    ext_modules = Extension(**compdi)

    setup(
        name=name,
        ext_modules=cythonize(ext_modules),
        compiler_directives=clidict,
    )
