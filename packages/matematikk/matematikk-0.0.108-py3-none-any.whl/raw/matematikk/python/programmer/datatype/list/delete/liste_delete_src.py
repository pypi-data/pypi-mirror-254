from __init__ import Pref, Datafil


##########################################
# Pref
##########################################

__   = Pref()
_  = Datafil()


##########################################
# Create
##########################################

_fil_navn_src = __._liste_delete_src_py


##########################################
# Hotkeys
##########################################

# python /Users/krj/Desktop/program/src/_dir_1/bld/data_fil/_exe/python/programmer/datatype/list/delete/liste_delete.py


##########################################
# Fil content
##########################################

_fil_content = f"""
{_._h_top_py}
{_._p_list_delete}

{_._c_verdier_L}
{_._v_liste} = {_._e_list_delete_arr}

{_._c_print_legacy}
print(f"{_._c_list_C}{_._v_kolon} {{{_._v_liste}}}")

{_._c_fn_delete_liste_core}
{_._v_liste} = []

{_._c_print_legacy}
print(f"{_._c_list_C}{_._v_kolon} {{{_._v_liste}}}")
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
