from __init__ import Pref, Datafil


##########################################
# Pref
##########################################

__   = Pref()
_  = Datafil()


##########################################
# Create
##########################################

_fil_navn_src = __._liste_oppdeling_comprehension_input_str_src_py


##########################################
# Hotkeys
##########################################

# python /Users/krj/Desktop/program/src/_dir_1/bld/data_fil/_exe/python/programmer/datatype/list/oppdeling/liste_oppdeling_comprehension_2_input_str.py


##########################################
# Fil content
##########################################

_fil_content = f"""
{_._h_top_py}
{_._p_list_oppdeling}

{_._c_input}
{_._v_liste} = input("{_._i_list_oppdeling}") {_._c_input_husk_par_square_str}
{_._v_n_deler} = input("{_._i_list_deler}")

{_._c_fn_str_til_str_arr}
{_._f_str_til_str_liste_def}

{_._c_fnc_str_til_str_arr}
{_._v_liste} = {_._f_str_til_str_liste}({_._v_liste})

{_._c_fn_oppdeling_lister_core}
def {_._f_oppdeling_lister_comprehension}({_._v_liste}, {_._v_n_deler}):

    {_._v_n_deler}    = int({_._v_n_deler})
    {_._v_del_arr_plur} = []

    {_._c_list_oppdeling_comprehension}
    {_._v_del_arr_plur} = [{_._v_liste}[{_._v_i} : {_._v_i} + {_._v_n_deler}] for {_._v_i} in range(0, len({_._v_liste}), {_._v_n_deler})]

    return {_._v_del_arr_plur}

{_._c_fnc_oppdeling_lister_core}
{_._v_del_arr_plur} = {_._f_oppdeling_lister_comprehension}({_._v_liste}, {_._v_n_deler})

{_._c_print_legacy}
print(f"{_._r_list_oppdeling_hele}{_._v_kolon} {{{_._v_del_arr_plur}}}")
print("{_._r_list_oppdeling_en_og_en}{_._v_kolon}")
for {_._v_del_arr} in {_._v_del_arr_plur}:
	print(f"{{{_._v_del_arr}}}")
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
