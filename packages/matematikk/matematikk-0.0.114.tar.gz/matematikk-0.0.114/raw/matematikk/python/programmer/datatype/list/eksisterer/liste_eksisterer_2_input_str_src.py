from __init__ import Pref, Datafil


##########################################
# Pref
##########################################

__   = Pref()
_  = Datafil()


##########################################
# Create
##########################################

_fil_navn_src = __._liste_eksisterer_input_str_src_py


##########################################
# Hotkeys
##########################################

# python /Users/krj/Desktop/program/src/_dir_1/bld/data_fil/_exe/python/programmer/datatype/list/eksisterer/liste_eksisterer_2_input_str.py


##########################################
# Fil content
##########################################

_fil_content = f"""
{_._h_top_py}
{_._p_list_eksisterer}

{_._c_input}
{_._v_liste} = input("{_._i_list}") {_._c_input_husk_par_square_str}
{_._v_el} = input("{_._i_eksisterer_el}") {_._c_input_husk_uten_hermetegn}

{_._c_fn_str_til_str_arr}
{_._f_str_til_str_liste_def}

{_._c_fnc_str_til_str_arr}
{_._v_liste} = {_._f_str_til_str_liste}({_._v_liste})

{_._c_list_eksisterer_if}
if {_._v_el} in {_._v_liste}:
    print(f"{_._r_Ja}{_._v_komma} {{{_._v_el}}} {_._r_list_eksisterer_i_arr}")
else:
	print("{_._r_Nei}{_._v_komma} {_._r_list_eksisterer_not_i_arr_el}")
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
