from __init__ import Pref, Datafil


##########################################
# Pref
##########################################

__   = Pref()
_  = Datafil()


##########################################
# Create
##########################################

_fil_navn_src = __._negative_tall_src_py


##########################################
# Hotkeys
##########################################

# python /Users/krj/Desktop/program/src/_dir_1/bld/data_fil/_exe/python/programmer/matematikk/tallteori/negative_tall/negative_tall_1.py


##########################################
# Fil content
##########################################

_fil_content = f"""
{_._h_top_py}
{_._p_negative_tall}

{_._c_verdier_L}
{_._v_liste} = {_._e_negative_tall_arr}

{_._c_fn_negative_tall_liste}
def {_._f_negative_tall_liste}({_._v_liste}):

	{_._c_nullstill}
	{_._v_negative_tall_liste} = list()

	{_._c_iterer_gjennom_listen}
	for {_._v_tall} in {_._v_liste}:

		{_._c_negative_tall}
		if {_._v_tall} < 0:
			{_._v_negative_tall_liste}.append({_._v_tall})

	return {_._v_negative_tall_liste}

{_._c_fnc_negative_tall}
{_._v_negative_tall_liste} = {_._f_negative_tall_liste}({_._v_liste})

{_._c_print_legacy}
print(f"{_._c_list_original_C}          {_._v_kolon} {{{_._v_liste}}}")
print(f"{_._r_negative_tall_list} {_._v_kolon} {{{_._v_negative_tall_liste}}}")
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
