from __init__ import Pref, Datafil


##########################################
# Pref
##########################################

__   = Pref()
_  = Datafil()


##########################################
# Create
##########################################

_fil_navn_src = __._liste_min_sort_src_py


##########################################
# Hotkeys
##########################################

# python /Users/krj/Desktop/program/src/_dir_1/bld/data_fil/_exe/python/programmer/datatype/list/min/liste_min_sort_1.py


##########################################
# Fil content
##########################################

_fil_content = f"""
{_._h_top_py}
{_._p_list_min_sort}

{_._c_verdier_L}
{_._v_liste} = {_._e_list_min_sort_arr}

{_._c_fn_min_sort}
def {_._f_min_sort}({_._v_liste}):

	{_._c_list_min_sort_synkende}
	{_._v_liste}.sort(reverse=True)

	{_._c_list_min_sort_siste_el}
	{_._v_min} = {_._v_liste}[-1]

	return {_._v_min}

{_._c_fnc_min_core}
{_._v_min} = {_._f_min_sort}({_._v_liste})

{_._c_print_legacy}
print(f"{_._c_list_C}             {_._v_kolon} {{{_._v_liste}}}")
print(f"{_._c_list_min_C}  {_._v_kolon} {{{_._v_min}}}")
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
