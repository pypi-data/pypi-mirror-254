from __init__ import Pref, Datafil


##########################################
# Pref
##########################################

__   = Pref()
_  = Datafil()


##########################################
# Create
##########################################

_fil_navn_src = __._liste_bytt_el_src_py


##########################################
# Hotkeys
##########################################

# python /Users/krj/Desktop/program/src/_dir_1/bld/data_fil/_exe/python/programmer/datatype/list/change/liste_bytt_el.py


##########################################
# Fil content
##########################################

_fil_content = f"""
{_._h_top_py}
{_._p_list_change}

{_._c_verdier_L}
{_._v_liste} = {_._e_list_change_arr}

{_._c_print_legacy}
print(f"{_._c_list_C}{_._v_kolon} {{{_._v_liste}}}")

{_._c_change_liste_tmp}
{_._v_el_tmp} = {_._v_liste}[0]

{_._c_change_liste_bytt_el}
{_._v_liste}[0] = {_._v_liste}[-1]

{_._c_change_liste_bytt_el_tmp}
{_._v_liste}[-1] = {_._v_el_tmp}

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
