from __init__ import Pref, Datafil


##########################################
# Pref
##########################################

__   = Pref()
_  = Datafil()


##########################################
# Create
##########################################

_fil_navn_src = __._variabelnavn_gyldig_src_py


##########################################
# Hotkeys
##########################################

# python /Users/krj/Desktop/program/src/_dir_1/bld/data_fil/_exe/python/tutorial/variabel/variabelnavn/variabelnavn_gyldig.py


##########################################
# Fil content
##########################################

_fil_content = f"""
{_._h_top_py}
{_._p_variabelnavn_gyldig}

{_._c_variabler_L}
{_._v_smaa}         = "{_._v_smaa_val}"
{_._v_STORE}       = "{_._v_STORE_val}"
{_._v_tall_42}     = {_._v_tall_42_val}
{_._v_underscore_} = "{_._v_underscore_val}"

{_._c_print_legacy}
print({_._v_smaa})
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
