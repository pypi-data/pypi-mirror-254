from __init__ import Pref, Datafil


##########################################
# Pref
##########################################

__   = Pref()
_  = Datafil()


##########################################
# Create
##########################################

_fil_navn_src = __._variabelnavn_case_src_py


##########################################
# Hotkeys
##########################################

# python /Users/krj/Desktop/program/src/_dir_1/bld/data_fil/_exe/python/tutorial/variabel/variabelnavn/variabelnavn_case.py


##########################################
# Fil content
##########################################

_fil_content = f"""
{_._h_top_py}
{_._p_variabelnavn_case}

{_._c_variabler_L}
{_._v_camel_case} = "{_._v_camel_case_val}"
{_._v_pascal_case}      = "{_._v_pascal_case_val}"
{_._v_snake_case}     = "{_._v_snake_case_val}"
{_._v_screaming_snake_case}      = "{_._v_screaming_snake_case_val}"

{_._c_print_legacy}
print({_._v_snake_case})
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
