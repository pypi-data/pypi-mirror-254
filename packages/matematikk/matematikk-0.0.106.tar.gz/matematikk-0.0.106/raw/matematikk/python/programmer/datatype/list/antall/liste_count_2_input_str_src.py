from __init__ import Pref, Datafil


##########################################
# Pref
##########################################

__   = Pref()
_  = Datafil()


##########################################
# Create
##########################################

_fil_navn_src = __._liste_count_str_input_src_py


##########################################
# Hotkeys
##########################################

# python /Users/krj/Desktop/program/src/_dir_1/bld/data_fil/_exe/python/programmer/datatype/list/antall/liste_count_2_input_str.py


##########################################
# Fil content
##########################################

_fil_content = f"""
{_._h_top_py}
{_._p_list_count}

{_._c_input}
{_._v_liste} = input("{_._i_list}") {_._c_input_husk_par_square_str}
{_._v_karakter} = input("{_._i_karakter}") {_._c_input_husk_uten_hermetegn}

{_._c_fn_str_til_str_arr}
{_._f_str_til_str_liste_def}

{_._c_fnc_str_til_str_arr}
{_._v_liste} = {_._f_str_til_str_liste}({_._v_liste})

{_._c_antall}
{_._v_antall} = {_._v_liste}.count({_._v_karakter})

{_._c_print_legacy}
if {_._v_antall} > 0:
	print(f"{{{_._v_antall}}} {_._r_elever_fikk} {_._r_karakter} {{{_._v_karakter}}}")
else:
	print(f"{_._r_ingen_elever_fikk} {_._r_karakter} {{{_._v_karakter}}}")
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
