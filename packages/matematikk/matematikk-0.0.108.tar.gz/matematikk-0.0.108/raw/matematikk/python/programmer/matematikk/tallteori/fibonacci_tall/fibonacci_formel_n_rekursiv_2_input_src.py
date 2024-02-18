from __init__ import Pref, Datafil


##########################################
# Pref
##########################################

__   = Pref()
_  = Datafil()


##########################################
# Create
##########################################

_fil_navn_src = __._fibonacci_formel_n_rekursiv_input_src_py


##########################################
# Hotkeys
##########################################

# python /Users/krj/Desktop/program/src/_dir_1/bld/data_fil/_exe/python/programmer/matematikk/tallteori/fibonacci_tall/fibonacci_formel_n_rekursiv_2_input.py


##########################################
# Fil content
##########################################

_fil_content = f"""
{_._h_top_py}
{_._p_fibonacci_pos}
{_._p_fibonacci_def_1_1}
{_._p_fibonacci_def_1_2}

{_._c_verdier_L}
{_._v_fib_1} = 0   {_._c_fibonacci_tall_1}
{_._v_fib_2} = 1   {_._c_fibonacci_tall_2}

{_._c_input}
{_._v_n} = input("{_._i_fibonacci_pos}")

{_._c_fn_fibonacci_rekursiv_core}
def {_._f_fibonacci_n_rekursiv}({_._v_n}):

	{_._c_type_cast_str_int}
	{_._v_n} = int({_._v_n})

	{_._c_ikke_definert}
	if {_._v_n} < 1:

		{_._c_print_feilmelding}
		print("{_._c_n_must_be_int_C}")

		return "{_._c_Ikke_def_C}"

	{_._c_fibonacci_tall_1}
	elif {_._v_n} == 1: return {_._v_fib_1}

	{_._c_fibonacci_tall_2}
	elif {_._v_n} == 2: return {_._v_fib_2}

	{_._c_fibonacci_rekursivt}
	else:

        {_._c_fo_fibonacci_rekursiv}
		{_._v_fib_n} = {_._f_fibonacci_n_rekursiv}({_._v_n} - 1) + {_._f_fibonacci_n_rekursiv}({_._v_n} - 2)

		return {_._v_fib_n}

{_._c_fnc_fibonacci_tall_core}
{_._v_fib_n} = {_._f_fibonacci_n_rekursiv}({_._v_n})

{_._c_print_legacy}
print(f"{_._r_fibonacci_on_pos_n} {{{_._v_n}}} {_._r_er}{_._v_kolon} {{{_._v_fib_n}}}")
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
