from __init__ import Pref, Datafil


##########################################
# Pref
##########################################

__   = Pref()
_  = Datafil()


##########################################
# Create
##########################################

_fil_navn_src = __._liste_min_for_src_py


##########################################
# Hotkeys
##########################################

# python /Users/krj/Desktop/program/src/_dir_1/bld/data_fil/_exe/python/programmer/datatype/list/min/liste_min_for_1.py


##########################################
# Fil content
##########################################

_fil_content = f"""
{_._h_top_py}
{_._p_list_min_for}

{_._c_input}
{_._v_liste} = {_._e_list_min_for_loop_arr}

{_._c_fn_min_for_loop}
def {_._f_min_for_loop}({_._v_liste}):

	{_._c_list_min_for_loop_max_tmp}
	{_._v_min} = {_._v_liste}[0]

	{_._c_iterer_gjennom_listen}
	for i in range(1, len({_._v_liste})):

		{_._c_list_min_for_loop_update}
		if {_._v_liste}[i] < {_._v_min}:
			{_._v_min} = {_._v_liste}[i]

	return {_._v_min}

{_._c_fnc_min_core}
{_._v_min} = {_._f_min_for_loop}({_._v_liste})

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
