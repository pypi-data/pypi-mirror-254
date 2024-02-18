from __init__ import Pref, Datafil


##########################################
# Pref
##########################################

__   = Pref()
_  = Datafil()


##########################################
# Create
##########################################

_fil_navn_src = __._sirkel_areal_r_eksponent_input_src_py


##########################################
# Hotkeys
##########################################

# python /Users/krj/Desktop/program/src/_dir_1/bld/data_fil/_exe/python/programmer/matematikk/geometri/sirkel/sirkel_areal_r_eksponent_2_input.py


##########################################
# Fil content
##########################################

_fil_content = f"""
{_._h_top_py}
{_._p_sirkel_areal_r}

{_._c_verdier_L}
{_._v_pi} = {_._v_pi_val}

{_._c_input}
{_._v_r} = input("{_._i_sirkel_r}")

{_._c_fn_sirkel_areal_core}
def {_._f_sirkel_areal}({_._v_r}):

    {_._c_fo_sirkel_areal}
    {_._v_areal} = {_._v_pi} * float({_._v_r})**2

    return {_._v_areal}

{_._c_fnc_sirkel_areal_core}
{_._v_areal} = {_._f_sirkel_areal}({_._v_r})

{_._c_print_legacy}
print(f"{_._r_arealet_er}{_._v_kolon} {{{_._v_areal}}}")
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
