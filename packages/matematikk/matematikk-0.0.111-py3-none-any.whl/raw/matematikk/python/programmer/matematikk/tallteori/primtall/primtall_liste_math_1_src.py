from __init__ import Pref, Datafil


##########################################
# Pref
##########################################

__   = Pref()
_  = Datafil()


##########################################
# Create
##########################################

_fil_navn_src = __._primtall_liste_math_src_py


##########################################
# Hotkeys
##########################################

# python /Users/krj/Desktop/program/src/_dir_1/bld/data_fil/_exe/python/programmer/matematikk/tallteori/primtall/primtall_liste_math_1.py


##########################################
# Fil content
##########################################

_fil_content = f"""
{_._h_top_py}
{_._p_prim_inter}

{_._c_variabler_L}
{_._v_primtall_liste} = list()

from math import sqrt

{_._c_verdier_L}
{_._v_min} = {_._e_primtall_liste_math_val_1}
{_._v_max} = {_._e_primtall_liste_math_val_2}

{_._c_fn_er_primtall_intervall_core}
def {_._f_er_primtall_intervall_sqrt}({_._v_min}, {_._v_max}):

    {_._c_iterer_gjennom_intervallet}
	for {_._v_n} in range(int({_._v_min}), int({_._v_max}) + 1):

		{_._c_prim_gt_1}
		if {_._v_n} > 1:

			{_._c_prim_iterer_n_half}
			for {_._v_i} in range(2, int(sqrt({_._v_n})) + 1):

				{_._c_prim_cond_ikke_div}
				if {_._v_n} % {_._v_i} == 0: break

			{_._c_for_hvis_ikke_break}
			else: {_._v_primtall_liste}.append({_._v_n})

	return {_._v_primtall_liste}

{_._c_fnc_er_primtall_core}
{_._v_primtall_liste} = {_._f_er_primtall_intervall_sqrt}({_._v_min}, {_._v_max})

{_._c_print_legacy}
if len({_._v_primtall_liste}) == 0:
	print(f"{_._r_ingen_prim_i_inter} {{{_._v_min}}} {_._r_og} {{{_._v_max}}}")
else:
	print(f"{_._r_primtallene_mellom} {{{_._v_min}}} {_._r_og} {{{_._v_max}}} {_._r_er}{_._v_kolon} {{{_._v_primtall_liste}}}")
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
