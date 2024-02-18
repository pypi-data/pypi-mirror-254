from __init__ import Pref, Datafil


##########################################
# Pref
##########################################

__  = Pref()
_   = Datafil()


##########################################
# Create
##########################################

_fil_navn_src = __._init_roten_py_T


##########################################
# Hotkeys
##########################################

# - Ingen hotkey
#   - Får denne feilmeldingen hvis prøver å kjøre filen
#       (env) $ python /Users/<user>/Desktop/program/src/_dir_1/bld/matematikk/src/matematikk/__init__.py
#       Root > __init__.py
#       Traceback (most recent call last):
#         File "/Users/<user>/Desktop/program/src/_dir_1/bld/matematikk/src/matematikk/__init__.py", line 5, in <module>
#           from ._ch_1.ch_2.ch_3.ch_4_fil import ch_5_fn
#       ImportError: attempted relative import with no known parent package
#   - Skal ikke virke > python /Users/<user>/Desktop/program/src/_dir_1/bld/matematikk/src/matematikk/__init__.py


##########################################
# Fil content
##########################################

_fil_content = f"""
# Versjon: {__._pypi_datafil_ver}

# Chain 5 mal
from ._ch_1.ch_2.ch_3.ch_4_fil import ch_5_fn

# numpy()
from numpy import(
    polyfit
    )

# sympy()
from sympy import (
    ConditionSet,
    core,
    diff,
    Eq,
    FiniteSet,
    Intersection,
    nsolve,
    Reals,
    solve,
    solveset,
    Symbol
    )

# reggis()
from .python.funksjoner.matematikk.regresjon.polynom.reggis.def_reggis_matematikk_mas import (
    reggis,

    # Alias > 1
    reggis_cas,
    regresjon,
    regresjon_cas,
    regresjon_polynom,
    regresjon_polynom_cas,

    # Alias > 2
    cas_regresjon,
    cas_regresjon_polynom,
    regresjon_polynom_cas
    )

# superlos()
from .python.funksjoner.matematikk.likninger.superlos.def_superlos_matematikk_mas import (
    superløs,

    # Alias > 1
    los,
    losning,
    løs,
    løsning,
    superlos,
    super_los,
    super_løs,

    # Alias > 2
    los_super,
    løs_super
    )

# ekstremalpunkt_max()
from .python.funksjoner.matematikk.funksjoner._drøfting.ekstremalpunkt.def_ekstremalpunkt_max_mas import (
    ekstremalpunkt_max,

    # Alias > 1
    ekstremalpunkt_maks,
    ekstremalpunkt_maksimalt,
    toppunkt

    # Alias > 2 > ...
    )

# overskudd_max()
from .python.funksjoner.matematikk.funksjoner._drøfting.ekstremalpunkt.def_overskudd_max_mas import (
    overskudd_max,

    # Alias > 1
    overskudd_maks,
    overskudd_maksimalt,
    overskudd_mest,
    overskudd_storst,
    overskudd_størst,

    # Alias > 2
    maks_overskudd,
    maksimalt_overskudd,
    mest_overskudd,
    storst_overskudd,
    størst_overskudd
    )
"""


##########################################
# Create fil
##########################################

__.bld_data_fil(
    _fil_navn_src,
    _fil_content)


##########################################
# End
##########################################
