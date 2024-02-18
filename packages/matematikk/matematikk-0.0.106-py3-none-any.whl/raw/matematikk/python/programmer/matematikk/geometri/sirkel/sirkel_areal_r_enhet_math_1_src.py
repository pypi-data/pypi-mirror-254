from __init__ import Pref, Datafil


##########################################
# Pref
##########################################

__   = Pref()
_  = Datafil()


##########################################
# Create
##########################################

_fil_navn_src = __._sirkel_areal_r_enhet_math_src_py


##########################################
# Hotkeys
##########################################

# python /Users/krj/Desktop/program/src/_dir_1/bld/data_fil/_exe/python/programmer/matematikk/geometri/sirkel/sirkel_areal_r_enhet_math_1.py


##########################################
# Fil content
##########################################

_fil_content = f"""
{_._h_top_py}
{_._p_sirkel_areal_r_enhet}

import math

{_._c_verdier_L}
{_._v_enhet} = "{_._e_sirkel_areal_r_enhet_math_unit}"
{_._v_r}     = {_._e_sirkel_areal_r_enhet_math_val}

{_._c_fn_sirkel_areal_core}
def {_._f_sirkel_areal_math}({_._v_r}):

    {_._c_fo_sirkel_areal}
    {_._v_areal} = math.pi * pow(float({_._v_r}), 2)

    return {_._v_areal}

{_._c_fnc_sirkel_areal_core}
{_._v_areal} = {_._f_sirkel_areal_math}({_._v_r})

{_._c_print_legacy}
print(f"{_._r_arealet_er}{_._v_kolon} {{{_._v_areal}}} {{{_._v_enhet}}}^2")
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
