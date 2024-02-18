from __init__ import Pref, Datafil


##########################################
# Pref
##########################################

__   = Pref()
_  = Datafil()


##########################################
# Create
##########################################

_fil_navn_src = __._armstrong_liste_src_py


##########################################
# Hotkeys
##########################################

# python /Users/krj/Desktop/program/src/_dir_1/bld/data_fil/_exe/python/programmer/matematikk/tallteori/armstrong_tall/armstrong_liste_1.py


##########################################
# Fil content
##########################################

_fil_content = f"""
{_._h_top_py}
{_._p_armstrong_inter}
{_._p_armstrong_def_1}
{_._p_armstrong_def_2}
{_._p_armstrong_eks_1}
{_._p_armstrong_eks_2}

{_._c_verdier_L}
{_._v_min} = {_._e_armstrong_liste_val_1}
{_._v_max} = {_._e_armstrong_liste_val_2}

{_._c_nullstill}
{_._v_armstrong_arr} = list()

{_._c_fn_er_armstrong_tall_intervall}
def {_._f_er_armstrong_tall_intervall}({_._v_min}, {_._v_max}):

    {_._c_iterer_gjennom_intervallet}
    for {_._v_n} in range(int({_._v_min}), int({_._v_max}) + 1):

        {_._c_variabler_L}
        {_._v_n_kopi}          = {_._v_n}             {_._c_kopier_n_init}
        {_._v_siffer_ant}      = len(str({_._v_n}))   {_._c_eks_siffer_ant_len}
        {_._v_sum}             = 0             {_._c_nullstill}

        {_._c_iterer_gjennom_sifrene_stop}
        while {_._v_n} != 0:

            {_._c_get_bakerste_siffer_mod_ti}
            {_._v_siffer} = {_._v_n} % 10 {_._c_eks_siffer_get_bakerste_siffer}

            {_._c_oppdater_sum_for_hver_iter}
            {_._v_sum} = {_._v_sum} + ({_._v_siffer}**{_._v_siffer_ant})

            {_._c_get_bakerste_siffer_del_10}
            {_._v_n} = int({_._v_n} / 10) {_._c_eks_siffer_del_10_iter}

        {_._c_sammenlign_opprinnelig_verdi}
        if {_._v_sum} == {_._v_n_kopi}: {_._v_armstrong_arr}.append({_._v_n_kopi})

    return {_._v_armstrong_arr}

{_._c_fnc_er_armstrong_tall_intervall}
{_._v_armstrong_arr} = {_._f_er_armstrong_tall_intervall}({_._v_min}, {_._v_max})

{_._c_print_legacy}
print(f"{_._r_list_med_armstrong_tall}{_._v_kolon} {{{_._v_armstrong_arr}}}")
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
