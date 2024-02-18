"""""" # start delvewheel patch
def _delvewheel_patch_1_5_2():
    import ctypes
    import os
    import platform
    import sys
    libs_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, 'python_flint.libs'))
    is_conda_cpython = platform.python_implementation() == 'CPython' and (hasattr(ctypes.pythonapi, 'Anaconda_GetVersion') or 'packaged by conda-forge' in sys.version)
    if sys.version_info[:2] >= (3, 8) and not is_conda_cpython or sys.version_info[:2] >= (3, 10):
        if os.path.isdir(libs_dir):
            os.add_dll_directory(libs_dir)
    else:
        load_order_filepath = os.path.join(libs_dir, '.load-order-python_flint-0.6.0')
        if os.path.isfile(load_order_filepath):
            with open(os.path.join(libs_dir, '.load-order-python_flint-0.6.0')) as file:
                load_order = file.read().split()
            for lib in load_order:
                lib_path = os.path.join(os.path.join(libs_dir, lib))
                kernel32 = ctypes.WinDLL('kernel32', use_last_error=True)
                if os.path.isfile(lib_path) and not kernel32.LoadLibraryExW(ctypes.c_wchar_p(lib_path), None, 0x00000008):
                    raise OSError('Error loading {}; {}'.format(lib, ctypes.FormatError(ctypes.get_last_error())))


_delvewheel_patch_1_5_2()
del _delvewheel_patch_1_5_2
# end delvewheel patch

from .pyflint import *

from .types.fmpz import *
from .types.fmpz_poly import *
from .types.fmpz_mat import *
from .types.fmpz_series import *

from .types.fmpq import *
from .types.fmpq_poly import *
from .types.fmpq_mat import *
from .types.fmpq_series import *

from .types.nmod import *
from .types.nmod_poly import *
from .types.nmod_mat import *
from .types.nmod_series import *

from .types.fmpz_mpoly import *
from .types.fmpz_mod import *
from .types.fmpz_mod_poly import *
from .types.fmpz_mod_mat import fmpz_mod_mat

from .types.arf import *
from .types.arb import *
from .types.arb_poly import *
from .types.arb_mat import *
from .types.arb_series import *
from .types.acb import *
from .types.acb_poly import *
from .types.acb_mat import *
from .types.acb_series import *

from .types.dirichlet import *
from .functions.showgood import good, showgood

__version__ = '0.6.0'
