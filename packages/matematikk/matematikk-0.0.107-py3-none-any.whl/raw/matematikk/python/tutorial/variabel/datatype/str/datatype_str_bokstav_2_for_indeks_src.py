from __init__ import Pref, Datafil


##########################################
# Pref
##########################################

__   = Pref()
_  = Datafil()


##########################################
# Create
##########################################

_fil_navn_src = __._datatype_str_bokstav_for_indeks_src_py


##########################################
# Hotkeys
##########################################

# python /Users/krj/Desktop/program/src/_dir_1/bld/data_fil/_exe/python/tutorial/variabel/datatype/str/datatype_str_bokstav_2_for_indeks.py


##########################################
# Fil content
##########################################

_fil_content = f"""
{_._h_top_py}
{_._p_datatype_str_bokstav_for}

{_._c_variabler_L}
{_._v_pyt} = "{_._e_pyt}"

{_._c_datatype_str_char_iterate}
for {_._v_i} in range(len({_._v_pyt})):
    print({_._v_pyt}[{_._v_i}])
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
