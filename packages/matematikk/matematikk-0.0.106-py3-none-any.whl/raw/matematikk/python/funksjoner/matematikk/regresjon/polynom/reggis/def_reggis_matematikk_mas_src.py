from __init__ import Pref, Datafil


##########################################
# Pref
##########################################

__   = Pref()
_  = Datafil()


##########################################
# Create
##########################################

_fil_navn_src = __._def_reggis_matematikk_mas_src


##########################################
# Hotkeys
##########################################

# python /Users/krj/Desktop/program/src/_dir_1/bld/data_fil/_exe/python/funksjoner/matematikk/regresjon/polynom/reggis/def_reggis_matematikk_mas.py


##########################################
# Fil content
##########################################

_fil_content = f"""
{_._h_top_py}

{_._c_imp_from_matematikk_import_Symbol_polyfit}

{_._f_reggis_def}


# Alias > 1
reggis_cas                  = reggis
regresjon                   = reggis
regresjon_cas               = reggis
regresjon_polynom           = reggis
regresjon_polynom_cas       = reggis

# Alias > 2
cas_regresjon               = reggis
cas_regresjon_polynom       = reggis
regresjon_polynom_cas       = reggis
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