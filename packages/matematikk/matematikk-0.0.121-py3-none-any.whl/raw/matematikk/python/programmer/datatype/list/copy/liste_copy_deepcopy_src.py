from __init__ import Pref, Datafil


##########################################
# Pref
##########################################

__   = Pref()
_  = Datafil()


##########################################
# Create
##########################################

_fil_navn_src = __._liste_copy_deepcopy_src_py


##########################################
# Hotkeys
##########################################

# python /Users/krj/Desktop/program/src/_dir_1/bld/data_fil/_exe/python/programmer/datatype/list/copy/liste_copy_deepcopy.py


##########################################
# Fil content
##########################################

_fil_content = f"""
{_._h_top_py}
{_._p_copy_liste_deep}

from copy import deepcopy

{_._c_verdier_L}
{_._v_liste_1} = {_._e_list_copy_deepcopy}
{_._v_liste_2} = {_._e_list_copy_deepcopy}

{_._c_fn_copy_liste_copy}
{_._v_liste_copy_1} = {_._v_liste_1}.copy()

{_._c_copy_liste_endre_vari}
{_._v_liste_1}[0]["{_._v_Navn}"] = "{_._e_list_copy_val}"

{_._c_copy_liste_begge_endres}
print(f"{_._r_list_copy_liste_print_1}")
print(f"{_._c_list_original_C} {_._v_kolon} {{{_._v_liste_1}}}")
print(f"{_._c_list_copy_C}  {_._v_kolon} {{{_._v_liste_copy_1}}}")

{_._c_fn_copy_liste_deepcopy}
{_._v_liste_copy_2} = deepcopy({_._v_liste_2})

{_._c_copy_liste_endre_vari}
{_._v_liste_2}[0]["{_._v_Navn}"] = "{_._e_list_copy_val}"

{_._c_copy_liste_kun_en_endres}
print(f"{_._r_list_copy_liste_print_2}")
print(f"{_._c_list_original_C} {_._v_kolon} {{{_._v_liste_2}}}")
print(f"{_._c_list_copy_C}  {_._v_kolon} {{{_._v_liste_copy_2}}}")
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
