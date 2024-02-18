from __init__ import Pref, Datafil


##########################################
# Pref
##########################################

__   = Pref()
_  = Datafil()


##########################################
# Create
##########################################

_fil_navn_src = __._datatype_list_indeks_src_py


##########################################
# Hotkeys
##########################################

# python /Users/krj/Desktop/program/src/_dir_1/bld/data_fil/_exe/python/tutorial/variabel/datatype/list/datatype_list_indeks.py


##########################################
# Fil content
##########################################

_fil_content = f"""
{_._h_top_py}
{_._p_datatype_list_indeks}

{_._c_variabler_L}
{_._v_liste} = {_._e_list_copy_gen}

{_._c_print_legacy}
print({_._v_liste}[0])
print({_._v_liste}[1])
print({_._v_liste}[2])
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
