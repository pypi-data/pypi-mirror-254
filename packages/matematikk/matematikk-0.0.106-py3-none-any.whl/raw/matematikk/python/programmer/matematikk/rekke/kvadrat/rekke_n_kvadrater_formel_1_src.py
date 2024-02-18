from __init__ import Pref, Datafil


##########################################
# Pref
##########################################

__   = Pref()
_  = Datafil()


##########################################
# Create
##########################################

_fil_navn_src = __._rekke_n_kvadrater_formel_src_py


##########################################
# Hotkeys
##########################################

# python /Users/krj/Desktop/program/src/_dir_1/bld/data_fil/_exe/python/programmer/matematikk/rekke/kvadrat/rekke_n_kvadrater_formel_1.py


##########################################
# Fil content
##########################################

_fil_content = f"""
{_._h_top_py}
{_._p_rekke_kvadrat}

{_._c_verdier_L}
{_._v_n} = {_._e_rekke_n_kvadrater_formel_val}

{_._c_fn_rekke_n_kvadrater_sum}
def {_._f_rekke_n_kvadrater_sum}({_._v_n}):

    {_._c_type_cast_str_int}
    {_._v_n} = int({_._v_n})

    {_._c_fo_rekke_kvadrat}
    {_._v_sum} = int(({_._v_n} * ({_._v_n} + 1) * (2 * {_._v_n} + 1)) / 6)

    return {_._v_sum}

{_._c_fnc_rekke_n_kvadrater_sum}
{_._v_sum} = {_._f_rekke_n_kvadrater_sum}({_._v_n})

{_._c_print_legacy}
print(f"{_._r_summen_av_de_n} {{{_._v_n}}} {_._r_first_kvadratene_er}{_._v_kolon} {{{_._v_sum}}}")
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