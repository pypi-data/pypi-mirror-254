from __init__ import Pref, Datafil


##########################################
# Pref
##########################################

__   = Pref()
_  = Datafil()


##########################################
# Create
##########################################

_fil_navn_src = __._variabel_def_src_py


##########################################
# Hotkeys
##########################################

# python /Users/krj/Desktop/program/src/_dir_1/bld/data_fil/_exe/python/tutorial/variabel/_def/variabel_def.py


##########################################
# Fil content
##########################################

_fil_content = f"""
{_._h_top_py}
{_._p_variabel_def}

{_._c_variabler_L}
{_._v_hei} = "{_._e_variabel_def}"

{_._c_print_legacy}
print({_._v_hei})
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
