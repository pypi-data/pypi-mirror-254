from __init__ import Pref, Datafil


##########################################
# Pref
##########################################

__   = Pref()
_  = Datafil()


##########################################
# Create
##########################################

_fil_navn_src = __._datatype_list_for_el_src_py


##########################################
# Hotkeys
##########################################

# python /Users/krj/Desktop/program/src/_dir_1/bld/data_fil/_exe/python/tutorial/variabel/datatype/list/datatype_list_for_2_el.py


##########################################
# Fil content
##########################################

_fil_content = f"""
{_._h_top_py}
{_._p_datatype_list_for_el}

{_._c_variabler_L}
{_._v_liste} = {_._e_list_copy_gen}

{_._c_datatype_list_print_el_iterate}
for {_._v_el} in {_._v_liste}:
    print({_._v_el})
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
