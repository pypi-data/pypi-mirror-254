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
from .reggis_fil import (
    reggis,

    # Alias > Right
    reggis_cas,
    regresjon,
    regresjon_cas,
    regresjon_polynom,
    regresjon_polynom_cas,

    # Alias > Reversed
    cas_regresjon,
    cas_regresjon_polynom,
    regresjon_polynom_cas
    )

# superlos()
from .superløs_fil import (
    superløs,

    # Alias > Right
    los,
    losning,
    løs,
    løsning,
    superlos,
    super_los,
    super_løs,

    # Alias > Reversed
    los_super,
    løs_super
    )

# ekstremalpunkt_max()
from .ekstremalpunkt_max_fil import (
    ekstremalpunkt_max,

    # Alias > Right > ...
    ekstremalpunkt_maks,
    ekstremalpunkt_maksimalt,
    toppunkt

    # Alias > Reversed > ...
    )

# overskudd_max()
from .overskudd_max_fil import (
    overskudd_max,

    # Alias > Right
    overskudd_maks,
    overskudd_maksimalt,
    overskudd_mest,
    overskudd_storst,
    overskudd_størst,

    # Alias > Reversed
    maks_overskudd,
    maksimalt_overskudd,
    mest_overskudd,
    storst_overskudd,
    størst_overskudd
    )

