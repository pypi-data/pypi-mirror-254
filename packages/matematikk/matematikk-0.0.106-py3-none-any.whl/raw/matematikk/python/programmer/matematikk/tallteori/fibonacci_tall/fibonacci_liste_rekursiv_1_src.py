from __init__ import Pref, Datafil


##########################################
# Pref
##########################################

__   = Pref()
_  = Datafil()


##########################################
# Create
##########################################

_fil_navn_src = __._fibonacci_liste_rekursiv_src_py


##########################################
# Hotkeys
##########################################

# python /Users/krj/Desktop/program/src/_dir_1/bld/data_fil/_exe/python/programmer/matematikk/tallteori/fibonacci_tall/fibonacci_liste_rekursiv_1.py


##########################################
# Fil content
##########################################

_fil_content = f"""
{_._h_top_py}
{_._p_fibonacci_pos_all}
{_._p_fibonacci_def_1_1}
{_._p_fibonacci_def_1_2}

{_._c_verdier_L}
{_._v_fib_1} 		= 0 		{_._c_fibonacci_tall_1}
{_._v_fib_2} 		= 1 		{_._c_fibonacci_tall_2}
{_._v_fib_liste} 	= list() 	{_._c_fibonacci_tall_liste}
{_._v_n}           = {_._e_fibonacci_liste_rekursiv_val}        {_._c_fibonacci_tall_inkl}

{_._c_fibonacci_list_append}
if int({_._v_n}) > 0: {_._v_fib_liste}.append({_._v_fib_1})
if int({_._v_n}) > 1: {_._v_fib_liste}.append({_._v_fib_2})

{_._c_fn_fibonacci_rekursiv_core}
def {_._f_fibonacci_n_liste}({_._v_n}):

	{_._c_type_cast_str_int}
	{_._v_n} = int({_._v_n})

	{_._c_ikke_definert}
	if {_._v_n} < 1:
		print("{_._c_n_must_be_int_C}")
		return "{_._c_Ikke_def_C}"

	{_._c_fibonacci_tall_1}
	elif {_._v_n} <= len({_._v_fib_liste}):
		return {_._v_fib_liste}[{_._v_n} -1]

	{_._c_fibonacci_rekursivt}
	else:

		{_._c_fo_fibonacci_rekursiv}
		{_._v_fib_n} = {_._f_fibonacci_n_liste}({_._v_n} - 1) + {_._f_fibonacci_n_liste}({_._v_n} - 2)

		{_._c_fibonacci_list_append_print}
		{_._v_fib_liste}.append({_._v_fib_n})

		return {_._v_fib_n}

{_._c_fnc_fibonacci_n_list_core}
{_._f_fibonacci_n_liste}({_._v_n})

{_._c_print_legacy}
print(f"{_._r_fibonacci_list} {{{_._v_fib_liste}}}")
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
