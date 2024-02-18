from __init__ import Pref, Datafil


##########################################
# Pref
##########################################

__   = Pref()
_  = Datafil()


##########################################
# Create
##########################################

_fil_navn_src = __._liste_oppdeling_for_src_py


##########################################
# Hotkeys
##########################################

# python /Users/krj/Desktop/program/src/_dir_1/bld/data_fil/_exe/python/programmer/datatype/list/oppdeling/liste_oppdeling_for_1.py


##########################################
# Fil content
##########################################

_fil_content = f"""
{_._h_top_py}
{_._p_list_oppdeling}

{_._c_verdier_L}
{_._v_steg}  = {_._e_list_oppdeling_n_for_val}
{_._v_liste} = {_._e_list_oppdeling_arr}

{_._c_fn_oppdeling_lister_core}
def {_._f_oppdeling_lister_for_loop}({_._v_liste}):

    {_._c_nullstill}
    {_._v_start}      = 0
    {_._v_slutt}      = len({_._v_liste})
    {_._v_del_arr_plur} = []

    {_._c_iterer_gjennom_listen}
    for {_._v_i} in range({_._v_start}, {_._v_slutt}, {_._v_steg}):
        {_._v_del_arr_plur}.append({_._v_liste}[{_._v_i} : {_._v_i} + {_._v_steg}])

    return {_._v_del_arr_plur}

{_._c_fnc_oppdeling_lister_core}
{_._v_del_arr_plur} = {_._f_oppdeling_lister_for_loop}({_._v_liste})

{_._c_print_legacy}
print(f"{_._r_list_oppdeling_hele}{_._v_kolon} {{{_._v_del_arr_plur}}}")
print("{_._r_list_oppdeling_en_og_en}{_._v_kolon}")
for {_._v_del_arr} in {_._v_del_arr_plur}:
	print(f"{{{_._v_del_arr}}}")
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
