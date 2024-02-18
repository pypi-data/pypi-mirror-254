from __init__ import Pref, Datafil


##########################################
# Pref
##########################################

__   = Pref()
_  = Datafil()


##########################################
# Create
##########################################

_fil_navn_src = __._addisjon_to_tall_src_py


##########################################
# Hotkeys
##########################################

# python /Users/krj/Desktop/program/src/_dir_1/bld/data_fil/_exe/python/programmer/matematikk/aritmetikk/addisjon/to_tall/addisjon_to_tall_1.py


##########################################
# Fil content
##########################################

_fil_content = f"""
{_._h_top_py}
{_._p_addisjon_to_tall}

{_._c_verdier_L}
{_._v_a} = 40
{_._v_b} = 2

{_._c_fn_to_tall_sum}
def {_._f_to_tall_sum}({_._v_a}, {_._v_b}):

    {_._c_regn_ut_sum}
    {_._v_c} = float({_._v_a}) + float({_._v_b})

    return {_._v_c}

{_._c_fnc_sum_core}
{_._v_c} = {_._f_to_tall_sum}({_._v_a}, {_._v_b})

{_._c_print_legacy}
print(f"{_._r_summen_er}{_._v_kolon} {{{_._v_a}}} + {{{_._v_b}}} = {{{_._v_c}}}")
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