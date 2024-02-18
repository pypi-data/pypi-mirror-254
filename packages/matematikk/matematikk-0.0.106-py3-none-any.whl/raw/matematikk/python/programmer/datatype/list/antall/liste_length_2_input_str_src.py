from __init__ import Pref, Datafil


##########################################
# Pref
##########################################

__   = Pref()
_  = Datafil()


##########################################
# Create
##########################################

_fil_navn_src = __._liste_length_input_str_src_py


##########################################
# Hotkeys
##########################################

# python /Users/krj/Desktop/program/src/_dir_1/bld/data_fil/_exe/python/programmer/datatype/list/antall/liste_length_2_input_str.py


##########################################
# Fil content
##########################################

_fil_content = f"""
{_._h_top_py}
{_._p_list_length}

{_._c_input}
{_._v_liste} = input("{_._i_list}") {_._c_input_husk_par_square_str}

{_._c_fn_str_til_str_arr}
{_._f_str_til_str_liste_def}

{_._c_fnc_str_til_str_arr}
{_._v_liste} = {_._f_str_til_str_liste}({_._v_liste})

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
