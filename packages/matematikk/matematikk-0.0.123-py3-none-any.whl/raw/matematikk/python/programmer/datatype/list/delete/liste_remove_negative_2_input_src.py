from __init__ import Pref, Datafil


##########################################
# Pref
##########################################

__   = Pref()
_  = Datafil()


##########################################
# Create
##########################################

_fil_navn_src = __._liste_remove_negative_tall_input_src_py

##########################################
# Hotkeys
##########################################

# python /Users/krj/Desktop/program/src/_dir_1/bld/data_fil/_exe/python/programmer/datatype/list/delete/liste_remove_negative_2_input.py


##########################################
# Fil content
##########################################

_fil_content = f"""
{_._h_top_py}
{_._p_remove_neg}

{_._c_input}
{_._v_liste} = input("{_._i_list}") {_._c_input_husk_par_square_float}

{_._c_fn_str_til_float_arr}
{_._f_str_til_float_liste_def}

{_._c_fn_remove_negative_tall}
def {_._f_remove_negative_tall}({_._v_liste}):

	{_._c_nullstill}
	{_._v_positive_tall_liste} = list()

	{_._c_iterer_gjennom_listen}
	for {_._v_tall} in {_._v_liste}:

		{_._c_remove_negative_tall}
		if {_._v_tall} > 0:
			{_._v_positive_tall_liste}.append({_._v_tall})

	return {_._v_positive_tall_liste}

{_._c_fnc_str_til_float_arr}
{_._v_liste} = {_._f_str_til_float_liste}({_._v_liste})

{_._c_fnc_remove_negative_tall}
{_._v_positive_tall_liste} = {_._f_remove_negative_tall}({_._v_liste})

{_._c_print_legacy}
print(f"{_._c_list_original_C}          {_._v_kolon} {{{_._v_liste}}}")
print(f"{_._r_list_remove_positive_tall} {_._v_kolon} {{{_._v_positive_tall_liste}}}")
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
