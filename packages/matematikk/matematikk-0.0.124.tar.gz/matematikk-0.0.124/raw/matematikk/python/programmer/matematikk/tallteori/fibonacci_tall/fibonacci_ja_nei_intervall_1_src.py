from __init__ import Pref, Datafil


##########################################
# Pref
##########################################

__   = Pref()
_  = Datafil()


##########################################
# Create
##########################################

_fil_navn_src = __._fibonacci_ja_nei_intervall_src_py


##########################################
# Hotkeys
##########################################

# python /Users/krj/Desktop/program/src/_dir_1/bld/data_fil/_exe/python/programmer/matematikk/tallteori/fibonacci_tall/fibonacci_ja_nei_intervall_1.py


##########################################
# Fil content
##########################################

_fil_content = f"""
{_._h_top_py}
{_._p_fibonacci_inter}
{_._p_fibonacci_def_1_1}
{_._p_fibonacci_def_1_2}
{_._p_fibonacci_def_2}

import math

{_._c_verdier_L}
{_._v_min} = {_._e_fibonacci_ja_nei_intervall_val_1}
{_._v_max} = {_._e_fibonacci_ja_nei_intervall_val_2}

{_._c_fn_er_kvadrat_tall}
{_._f_er_kvadrat_tall_def}

{_._c_fn_er_fibonacci_tall}
def {_._f_er_fibonacci_tall}({_._v_n}):

    {_._c_ikke_definert}
    if {_._v_n} < 1: return False

    {_._c_fibonacci_if_form}
    {_._v_er_fib_true_1} = {_._f_er_kvadrattall_C}(5 * int({_._v_n})**2 + 4)
    {_._v_er_fib_true_2} = {_._f_er_kvadrattall_C}(5 * int({_._v_n})**2 - 4)

    {_._c_fibonacci_or}
    if {_._v_er_fib_true_1} or {_._v_er_fib_true_2}: return True

    {_._c_fibonacci_ingen}
    else: return False

{_._c_fn_er_fibonacci_tall_print}
def {_._f_er_fibonacci_tall_print}(n):

    {_._c_print_legacy}
    if {_._f_er_fibonacci_tall}({_._v_n}) == True: print(f"{_._r_Er} {{{_._v_n}}} {_._r_et_fibonacci_tall}{_._v_question} {_._r_Ja}")
    else:                            print(f"{_._r_Er} {{{_._v_n}}} {_._r_et_fibonacci_tall}{_._v_question} {_._r_Nei}")

{_._c_fn_er_fibonacci_tall_intervall}
def {_._f_er_fibonacci_tall_intervall}({_._v_min}, {_._v_max}):

    {_._c_iterer_gjennom_intervallet}
    for {_._v_n} in range(int({_._v_min}), int({_._v_max}) + 1):
        {_._f_er_fibonacci_tall_print}({_._v_n})

{_._c_fnc_er_fibonacci_core}
{_._f_er_fibonacci_tall_intervall}({_._v_min}, {_._v_max})
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
