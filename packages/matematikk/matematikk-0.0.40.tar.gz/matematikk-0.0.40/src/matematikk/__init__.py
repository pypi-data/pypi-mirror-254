### from sympy import diff

# ekstremalpunkt_max()
#from .ekstremalpunkt_max_fil import (
#    ekstremalpunkt_max,
#    #superløs,
#    #Symbol,
#    #diff
#    )
#from .ekstremalpunkt_maks_fil import (
#    ekstremalpunkt_maks,
#    superløs,
#    Symbol,
#    diff
#    )

# reggis()
from .reggis_fil import (
    reggis,

    # Syntax > Right
    reggis_cas,
    regregsjon,
    regregsjon_cas,
    regregsjon_polynom,
    regregsjon_polynom_cas,

    # Syntax > Reversed
    cas_regresjon,
    cas_regregsjon_polynom,
    regregsjon_polynom_cas,

    #polyfit,
    #Symbol
    )

# superlos()
from .superløs_fil import (
    superløs,

    # Syntax > Right
    los,
    losning,
    løs,
    løsning,
    superlos,
    super_los,
    super_løs,

    # Syntax > Reversed
    los_super,
    løs_super,

    Eq,
    Reals,
    core,
    Symbol,
    ConditionSet,
    FiniteSet,
    Intersection,
    solve,
    solveset,
    nsolve,
    #diff
    )

# overskudd_max()
from .overskudd_max_fil import (
    overskudd_max,

    # Syntax > Right
    overskudd_maks,
    overskudd_maksimalt,
    overskudd_mest,
    overskudd_storst,
    overskudd_størst,

    # Syntax > Reversed
    maks_overskudd,
    maksimalt_overskudd,
    mest_overskudd,
    storst_overskudd,
    størst_overskudd,

    #ekstremalpunkt_max,
    #Symbol
    )

