from __init__ import Pref, Datafil


##########################################
# Pref
##########################################

__   = Pref()
_  = Datafil()


##########################################
# Create
##########################################

_fil_navn_src = __._liste_copy_comprehension_src_py


##########################################
# Hotkeys
##########################################

# python /Users/krj/Desktop/program/src/_dir_1/bld/data_fil/_exe/python/programmer/datatype/list/copy/liste_copy_comprehension.py


##########################################
# Fil content
##########################################

_fil_content = f"""
{_._h_top_py}
{_._p_copy_liste_comprehension}

{_._c_verdier_L}
{_._v_liste} = {_._e_list_copy_gen}

{_._c_fn_copy_liste_pres_core}
{_._v_liste_copy} = [i for i in {_._v_liste}]

{_._c_print_legacy}
print(f"{_._c_list_original_C} {_._v_kolon} {{{_._v_liste}}}")
print(f"{_._c_list_copy_C}  {_._v_kolon} {{{_._v_liste_copy}}}")
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
