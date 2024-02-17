# Copyright (c) 2023 ING Analytics Wholesale Banking


# start delvewheel patch
def _delvewheel_patch_1_5_2():
    import os
    libs_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, 'sparse_dot_topn.libs'))
    if os.path.isdir(libs_dir):
        os.add_dll_directory(libs_dir)


_delvewheel_patch_1_5_2()
del _delvewheel_patch_1_5_2
# end delvewheel patch

import importlib.metadata

__version__ = importlib.metadata.version("sparse_dot_topn")
from sparse_dot_topn.api import awesome_cossim_topn, sp_matmul, sp_matmul_topn
from sparse_dot_topn.lib import _sparse_dot_topn_core as _core
from sparse_dot_topn.lib._sparse_dot_topn_core import _has_openmp_support

__all__ = ["awesome_cossim_topn", "sp_matmul", "sp_matmul_topn", "_core", "__version__", "_has_openmp_support"]
