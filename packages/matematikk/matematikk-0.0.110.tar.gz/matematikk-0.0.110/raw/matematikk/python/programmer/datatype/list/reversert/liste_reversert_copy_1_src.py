from __init__ import Pref, Datafil


##########################################
# Pref
##########################################

__   = Pref()
_  = Datafil()


##########################################
# Create
##########################################

_fil_navn_src = __._liste_reversert_copy_src_py


##########################################
# Hotkeys
##########################################

# python /Users/krj/Desktop/program/src/_dir_1/bld/data_fil/_exe/python/programmer/datatype/list/reversert/liste_reversert_copy_1.py


##########################################
# Fil content
##########################################

_fil_content = f"""
{_._h_top_py}
{_._p_list_reversed}
{_._p_list_reversed_algo_time}

{_._c_verdier_L}
{_._v_original_liste} = {_._e_list_reversed_copy_arr}

{_._c_list_reversed_kopier}
{_._v_reversert_liste} = {_._v_original_liste}.copy()

{_._c_list_reverse}
{_._v_reversert_liste}.reverse()

{_._c_print_legacy}
print(f"{_._c_list_original_C}  {_._v_kolon} {{{_._v_original_liste}}}")
print(f"{_._c_list_reversert_C} {_._v_kolon} {{{_._v_reversert_liste}}}")
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
