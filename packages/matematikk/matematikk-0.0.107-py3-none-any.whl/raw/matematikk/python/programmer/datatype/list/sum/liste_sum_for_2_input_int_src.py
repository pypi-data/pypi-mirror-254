from __init__ import Pref, Datafil


##########################################
# Pref
##########################################

__   = Pref()
_  = Datafil()


##########################################
# Create
##########################################

_fil_navn_src = __._liste_sum_for_int_input_src_py


##########################################
# Hotkeys
##########################################

# python /Users/krj/Desktop/program/src/_dir_1/bld/data_fil/_exe/python/programmer/datatype/list/sum/liste_sum_for_2_input_int.py


##########################################
# Fil content
##########################################

_fil_content = f"""
{_._h_top_py}
{_._p_list_sum_for}

{_._c_input}
{_._v_liste} = input("{_._i_list_sum}") {_._c_input_husk_par_square_int}

{_._c_fn_str_til_int_arr}
{_._f_str_til_int_liste_def}

{_._c_fn_sum_arr}
def {_._f_sum_arr}({_._v_liste}):

	{_._c_nullstill}
	{_._v_sum} = 0

	{_._c_oppdater_sum_for_hver_iter}
	for {_._v_el} in {_._v_liste}:
		{_._v_sum} += {_._v_el}

	return({_._v_sum})

{_._c_fnc_str_til_int_arr}
{_._v_liste} = {_._f_str_til_int_liste}({_._v_liste})

{_._c_fnc_sum_core}
{_._v_sum} = {_._f_sum_arr}({_._v_liste})

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
