from __init__ import Pref, Datafil


##########################################
# Pref
##########################################

__   = Pref()
_  = Datafil()


##########################################
# Create
##########################################

_fil_navn_src = __._liste_sortert_ja_nei_all_src_py


##########################################
# Hotkeys
##########################################

# python /Users/krj/Desktop/program/src/_dir_1/bld/data_fil/_exe/python/programmer/datatype/list/monotonic/liste_sortert_ja_nei_all_1.py


##########################################
# Fil content
##########################################

_fil_content = f"""
{_._h_top_py}
{_._p_list_monotonic}
{_._p_list_monotonic_ver_all}

{_._c_verdier_L}
{_._v_liste} = {_._e_list_monotonic_arr}

{_._c_fn_er_arr_monotonic_core}
def {_._f_er_arr_monotonic}({_._v_liste}):

	{_._c_list_monotonic_true_false}
	return (all({_._v_liste}[{_._v_i}] <= {_._v_liste}[{_._v_i} + 1] for {_._v_i} in range(len({_._v_liste}) - 1)) or
			all({_._v_liste}[{_._v_i}] >= {_._v_liste}[{_._v_i} + 1] for {_._v_i} in range(len({_._v_liste}) - 1)))

{_._c_fnc_er_arr_monotonic_core}
{_._v_er_monotonisk} = {_._f_er_arr_monotonic}({_._v_liste})

{_._c_list_legacy}
print(f"{_._c_list_C}{_._v_kolon} {{{_._v_liste}}}")
if {_._v_er_monotonisk} == True:
	print(f"{_._r_list_er_monotonic}{_._v_question} {_._r_Ja}")
if {_._v_er_monotonisk} == False:
	print(f"{_._r_list_er_monotonic}{_._v_question} {_._r_Nei}")
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
