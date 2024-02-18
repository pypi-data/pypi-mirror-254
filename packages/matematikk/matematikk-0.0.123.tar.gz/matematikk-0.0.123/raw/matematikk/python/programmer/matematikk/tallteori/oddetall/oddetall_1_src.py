from __init__ import Pref, Datafil


##########################################
# Pref
##########################################

__   = Pref()
_  = Datafil()


##########################################
# Create
##########################################

_fil_navn_src = __._oddetall_src_py


##########################################
# Hotkeys
##########################################

# python /Users/krj/Desktop/program/src/_dir_1/bld/data_fil/_exe/python/programmer/matematikk/tallteori/oddetall/oddetall_1.py


##########################################
# Fil content
##########################################

_fil_content = f"""
{_._h_top_py}
{_._p_oddetall}

{_._c_verdier_L}
{_._v_liste} = {_._e_oddetall_arr}

{_._c_fn_oddetall_mod}
def {_._f_oddetall_liste_mod}({_._v_liste}):

	{_._c_nullstill}
	{_._v_oddetall_liste} = list()

	{_._c_iterer_gjennom_listen}
	for {_._v_tall} in {_._v_liste}:

		{_._c_oddetall}
		if {_._v_tall} % 2 != 0:
			{_._v_oddetall_liste}.append({_._v_tall})

	return {_._v_oddetall_liste}

{_._c_fnc_oddetall_mod}
{_._v_oddetall_liste} = {_._f_oddetall_liste_mod}({_._v_liste})

{_._c_print_legacy}
print(f"{_._c_list_original_C} {_._v_kolon} {{{_._v_liste}}}")
print(f"{_._r_oddetall_list}  {_._v_kolon} {{{_._v_oddetall_liste}}}")
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
