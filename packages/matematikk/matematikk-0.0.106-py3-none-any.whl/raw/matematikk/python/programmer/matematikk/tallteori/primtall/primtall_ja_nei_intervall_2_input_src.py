from __init__ import Pref, Datafil


##########################################
# Pref
##########################################

__   = Pref()
_  = Datafil()


##########################################
# Create
##########################################

_fil_navn_src = __._primtall_ja_nei_intervall_input_src_py


##########################################
# Hotkeys
##########################################

# python /Users/krj/Desktop/program/src/_dir_1/bld/data_fil/_exe/python/programmer/matematikk/tallteori/primtall/primtall_ja_nei_intervall_2_input.py


##########################################
# Fil content
##########################################

_fil_content = f"""
{_._h_top_py}
{_._p_prim_inter}
{_._p_prim_optimal}

{_._c_input}
{_._v_min} = input("{_._i_min}")
{_._v_max} = input("{_._i_max}")

{_._c_fn_er_primtall_intervall_core}
def {_._f_er_primtall_intervall}({_._v_min}, {_._v_max}):

    {_._c_iterer_gjennom_intervallet}
	for {_._v_n} in range(int({_._v_min}), int({_._v_max}) + 1):

		{_._c_prim_gt_1}
		if {_._v_n} > 1:

			{_._c_prim_iterer_n_half}
			for {_._v_i} in range(2, int({_._v_n} / 2) + 1):

				{_._c_prim_cond_ikke_div}
				if {_._v_n} % {_._v_i} == 0:
					print(f"{_._r_Er} {{{_._v_n}}} {_._r_et_primtall}{_._v_question} {_._r_Nei}")
					break

			{_._c_for_hvis_ikke_break}
			else: print(f"{_._r_Er} {{{_._v_n}}} {_._r_et_primtall}{_._v_question} {_._r_Ja}")

		{_._c_prim_cond_ikke_gt}
		else: print(f"{_._r_Er} {{{_._v_n}}} {_._r_et_primtall}{_._v_question} {_._r_Nei}")

{_._c_fnc_er_primtall_core}
{_._f_er_primtall_intervall}({_._v_min}, {_._v_max})
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
