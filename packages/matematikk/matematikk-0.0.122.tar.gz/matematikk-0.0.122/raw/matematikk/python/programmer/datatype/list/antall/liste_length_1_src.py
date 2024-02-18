from __init__ import Pref, Datafil


##########################################
# Pref
##########################################

__   = Pref()
_  = Datafil()


##########################################
# Create
##########################################

_fil_navn_src = __._liste_length_src_py


##########################################
# Hotkeys
##########################################

# python /Users/krj/Desktop/program/src/_dir_1/bld/data_fil/_exe/python/programmer/datatype/list/antall/liste_length_1.py


##########################################
# Fil content
##########################################

_fil_content = f"""
{_._h_top_py}
{_._p_list_length}

{_._c_verdier_L}
{_._v_liste} = {_._e_list_length_arr}

{_._c_print_legacy}
print(f"{_._c_list_C}{_._v_kolon} {{{_._v_liste}}}")

{_._c_fn_lenth_liste_core}
{_._v_el_ant} = len({_._v_liste})

{_._c_print_legacy}
print(f"{_._r_list_length}{_._v_kolon} {{{_._v_el_ant}}}")
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
