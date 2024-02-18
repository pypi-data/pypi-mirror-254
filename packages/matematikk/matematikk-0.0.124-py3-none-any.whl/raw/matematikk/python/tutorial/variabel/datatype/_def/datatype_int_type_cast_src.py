from __init__ import Pref, Datafil


##########################################
# Pref
##########################################

__   = Pref()
_  = Datafil()


##########################################
# Create
##########################################

_fil_navn_src = __._datatype_int_type_cast_src_py


##########################################
# Hotkeys
##########################################

# python /Users/krj/Desktop/program/src/_dir_1/bld/data_fil/_exe/python/tutorial/variabel/datatype/_def/datatype_int_type_cast.py


##########################################
# Fil content
##########################################

_fil_content = f"""
{_._h_top_py}
{_._p_datatype_int_type_cast}

{_._c_variabler_L}
{_._v_tall_1} = {_._e_int_tall_1}
{_._v_tall_2} = "{_._e_int_tall_2}"

{_._c_datatype_int_type_cast}
{_._v_sum} = {_._v_tall_1} + int({_._v_tall_2})

{_._c_print_legacy}
print({_._v_sum})
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
