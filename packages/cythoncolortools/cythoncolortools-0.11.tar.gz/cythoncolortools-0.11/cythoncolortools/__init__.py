import os
import numpy as np

try:
    from .pictcycomp import searchforcolor, are_any_colors_in_pic
except Exception:
    from cycompi import compile_cython_code
    import os

    numpyincludefolder = np.get_include()
    pyxfile = "pictcycomp.pyx"
    uniqueproductcythonmodule = pyxfile.split(".")[0]
    dirname = os.path.abspath(os.path.dirname(__file__))
    pyxfile_complete_path = os.path.join(dirname, pyxfile)
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
        "name": uniqueproductcythonmodule,
        "sources": [pyxfile_complete_path],
        "include_dirs": [numpyincludefolder],
        "define_macros": [
            ("NPY_NO_DEPRECATED_API", "NPY_1_7_API_VERSION"),
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
        "extra_compile_args": ["/O2", "/Oy", "/openmp"],
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
        "overflowcheck.fold": False,
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
        "language_level": "3str",  # (2/3/3str)
        "c_string_type": "bytes",  # (bytes / str / unicode)
        "c_string_encoding": "ascii",  # (ascii, default, utf-8, etc.)
        "type_version_tag": False,
        "unraisable_tracebacks": True,
        "iterable_coroutine": False,
        "annotation_typing": False,
        "emit_code_comments": False,
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
        name=uniqueproductcythonmodule,
        configdict=configdict,
        optionsdict=optionsdict,
        cmd_line_args=compiler_directives,
        cwd=dirname,
        shell=True,
        env=os.environ.copy(),
    )
    from .pictcycomp import searchforcolor, are_any_colors_in_pic


def search_colors(pic, colors, add_results=True, cpus=-1):
    """
    Search for specified colors in an image.

    Parameters:
        pic (numpy.ndarray): The input RGB image as a 2D numpy array (np.uint8).
        colors (numpy.ndarray or list): Colors to search for in the image.
            It can be a 1D numpy array (np.uint8) or a list of color values.
        add_results (bool, optional): If True, include rgb colors for each match.
            If False, only return a the coords.
        cpus (int, optional): Number of CPU cores to use for parallel processing.
            If set to -1, it will use all available cores.
    Returns:
        numpy.ndarray: If add_results is True, a 2D array with 5 columns
        , otherwise, a 2D array with 2 columns.
    """
    if not isinstance(colors, np.ndarray):
        colors = np.array(colors, dtype=np.uint8)
    rav_colors = np.ascontiguousarray(colors.ravel())
    totallengthcolor = rav_colors.shape[0] - 1
    totallenghtpic = np.prod(pic.shape) - 1
    width = pic.shape[1]
    if add_results:
        results = np.zeros((totallenghtpic, 5), dtype=np.int64)
    else:
        results = np.zeros((totallenghtpic, 2), dtype=np.int64)
    countervar = np.zeros(1, dtype=np.int64)
    searchforcolor(
        pic.ravel(),
        rav_colors,
        results,
        countervar,
        width,
        totallenghtpic,
        totallengthcolor,
        cpus,
        add_results,
    )
    return results[: countervar[0]]


def are_any_colors_in_picture(pic, colors, cpus=-1):
    """
    Check if any of the specified colors are present in an image.

    Parameters:
        pic (numpy.ndarray): The input RGB image as a 2D numpy array (np.uint8).
        colors (numpy.ndarray or list): Colors to search for in the image.
            It can be a 1D numpy array (np.uint8) or a list of color values.
        cpus (int, optional): Number of CPU cores to use for parallel processing.
            If set to -1, it will use all available cores.
    Returns:
        bool: True if any of the specified colors are present, False otherwise.
    """
    if not isinstance(colors, np.ndarray):
        colors = np.array(colors, dtype=np.uint8)
    rav_colors = np.ascontiguousarray(colors.ravel())
    totallengthcolor = rav_colors.shape[0] - 1
    totallenghtpic = np.prod(pic.shape) - 1
    width = pic.shape[1]
    results = np.zeros(1, dtype=np.int64)
    are_any_colors_in_pic(
        pic.ravel(),
        rav_colors,
        results,
        width,
        totallenghtpic,
        totallengthcolor,
        cpus,
    )
    return bool(results[0])
