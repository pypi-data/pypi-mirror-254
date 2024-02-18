from __init__ import Pref, Datafil


##########################################
# Pref
##########################################

__   = Pref()
_    = Datafil()


##########################################
# Create
##########################################

_fil_navn_src = __._def_superlos_matematikk_mas_src



##########################################
# Hotkeys
##########################################

# python /Users/krj/Desktop/program/src/_dir_1/bld/data_fil/_exe/python/funksjoner/matematikk/likninger/superlos/def_superlos_matematikk_mas.py


##########################################
# Fil content
##########################################

_fil_content = f"""
{_._h_top_py}

{_._c_imp_from_matematikk_import_ConditionSet_core_Eq_FiniteSet_Intersection_nsolve_Reals_solve_solveset_Symbol_C}

{_._f_superlos_def}


# Alias > 1
los                     = superløs
losning                 = superløs
løs                     = superløs
løsning                 = superløs
superlos                = superløs
super_los               = superløs
super_løs               = superløs

# Alias > 2
los_super               = superløs
løs_super               = superløs
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