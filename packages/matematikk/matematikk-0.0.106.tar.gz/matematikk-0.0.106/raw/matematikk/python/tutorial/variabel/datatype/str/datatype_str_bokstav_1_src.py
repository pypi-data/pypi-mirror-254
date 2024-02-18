from __init__ import Pref, Datafil


##########################################
# Pref
##########################################

__   = Pref()
_  = Datafil()


##########################################
# Create
##########################################

_fil_navn_src = __._datatype_str_bokstav_src_py


##########################################
# Hotkeys
##########################################

# python /Users/krj/Desktop/program/src/_dir_1/bld/data_fil/_exe/python/tutorial/variabel/datatype/str/datatype_str_bokstav_1.py


##########################################
# Fil content
##########################################

_fil_content = f"""
{_._h_top_py}
{_._p_datatype_str_bokstav}

{_._c_variabler_L}
{_._v_pyt} = "{_._e_pyt}"

{_._c_print_legacy}
print({_._v_pyt}[0])
print({_._v_pyt}[1])
print({_._v_pyt}[2])
print({_._v_pyt}[3])
print({_._v_pyt}[4])
print({_._v_pyt}[5])
print({_._v_pyt}[6])
print({_._v_pyt}[7])
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
