from __init__ import Pref, Datafil


##########################################
# Pref
##########################################

__   = Pref()
_  = Datafil()


##########################################
# Create
##########################################

_fil_navn_src = __._liste_sum_int_src_py


##########################################
# Hotkeys
##########################################

# python /Users/krj/Desktop/program/src/_dir_1/bld/data_fil/_exe/python/programmer/datatype/list/sum/liste_sum_1_int.py


##########################################
# Fil content
##########################################

_fil_content = f"""
{_._h_top_py}
{_._p_list_sum}

{_._c_input}
{_._v_liste} = {_._e_list_sum_arr}

{_._c_fnc_sum_core}
{_._v_sum} = sum({_._v_liste})

{_._c_print_legacy}
print(f"{_._c_list_C}                {_._v_kolon} {{{_._v_liste}}}")
print(f"{_._r_list_sum_el} {_._v_kolon} {{{_._v_sum}}}")
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
