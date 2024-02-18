from __init__ import Pref, Datafil


##########################################
# Pref
##########################################

__   = Pref()
_  = Datafil()


##########################################
# Create
##########################################

_fil_navn_src = __._datatype_tuple_def_src_py


##########################################
# Hotkeys
##########################################

# python /Users/krj/Desktop/program/src/_dir_1/bld/data_fil/_exe/python/tutorial/variabel/datatype/tuple/datatype_tuple_def.py


##########################################
# Fil content
##########################################

_fil_content = f"""
{_._h_top_py}
{_._p_datatype_tuple_def}

{_._c_variabler_L}
{_._v_tuppel} = {_._e_tuple}

{_._c_datatype_tuple_print_tup}
print({_._v_tuppel})

{_._c_datatype_tuple_print_el}
print({_._v_tuppel}[0])
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
