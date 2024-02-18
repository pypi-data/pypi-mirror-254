from __init__ import Pref, Datafil


##########################################
# Pref
##########################################

__   = Pref()
_  = Datafil()


##########################################
# Create
##########################################

_fil_navn_src = __._liste_sortert_ja_nei_sort_to_src_py


##########################################
# Hotkeys
##########################################

# python /Users/krj/Desktop/program/src/_dir_1/bld/data_fil/_exe/python/programmer/datatype/list/monotonic/liste_sortert_ja_nei_sort_3_to.py


##########################################
# Fil content
##########################################

_fil_content = f"""
{_._h_top_py}
{_._p_list_monotonic}
{_._p_list_monotonic_ver_sort}

{_._c_input}
{_._v_liste_1} = {_._e_list_monotonic_1_arr}
{_._v_liste_2} = {_._e_list_monotonic_2_arr}

{_._c_fn_er_arr_monotonic_core}
def {_._f_er_arr_monotonic_sort}({_._v_liste}):

    {_._c_list_monotonic_sort_append}
	{_._v_stigende_arr} = {_._v_liste}.copy()
	{_._v_synkende_arr} = {_._v_liste}.copy()

	{_._c_list_monotonic_sort_begge}
	{_._v_stigende_arr}.sort()
	{_._v_synkende_arr}.sort()

	{_._c_list_monotonic_sort_rev_1}
	{_._v_synkende_arr}.reverse()

	{_._c_list_monotonic_sort_if_mono}
	if {_._v_stigende_arr} == {_._v_liste} or {_._v_synkende_arr} == {_._v_liste}: return True

    {_._c_list_monotonic_sort_not_mono}
	else: return False

{_._c_fnc_er_arr_monotonic_core}
{_._v_er_monotonisk_1} = {_._f_er_arr_monotonic_sort}({_._v_liste_1})
{_._v_er_monotonisk_2} = {_._f_er_arr_monotonic_sort}({_._v_liste_2})

{_._c_list_1}
print(f"{_._c_list_1_C}{_._v_kolon} {{{_._v_liste_1}}}")
if {_._v_er_monotonisk_1} == True:
	print(f"{_._r_list_er_monotonic_1}{_._v_question} {_._r_Ja}")
if {_._v_er_monotonisk_1} == False:
	print(f"{_._r_list_er_monotonic_1}{_._v_question} {_._r_Nei}")

{_._c_list_2}
print(f"{_._c_list_2_C}{_._v_kolon} {{{_._v_liste_2}}}")
if {_._v_er_monotonisk_2} == True:
	print(f"{_._r_list_er_monotonic_2}{_._v_question} {_._r_Ja}")
if {_._v_er_monotonisk_2} == False:
	print(f"{_._r_list_er_monotonic_2}{_._v_question} {_._r_Nei}")
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
