from __init__ import Pref, Datafil


##########################################
# Pref
##########################################

__   = Pref()
_  = Datafil()


##########################################
# Create
##########################################

_fil_navn_src = __._siffer_antall_divisjon_input_src_py


##########################################
# Hotkeys
##########################################

# python /Users/krj/Desktop/program/src/_dir_1/bld/data_fil/_exe/python/programmer/matematikk/aritmetikk/siffer/siffer_antall_divisjon_2_input.py


##########################################
# Fil content
##########################################

_fil_content = f"""
{_._h_top_py}
{_._p_siffer_ant}

{_._c_input}
{_._v_n} = input("{_._i_tall}")

{_._c_fn_siffer_antall_core}
def {_._f_siffer_antall_divisjon_C}({_._v_n}):

    {_._c_type_cast_str_int}
    {_._v_n} = int({_._v_n})

    {_._c_nullstill}
    {_._v_siffer_ant} = 0

    {_._c_iterer_frem_sifrene_stop}
    while {_._v_n} != 0:
        {_._v_siffer_ant} += 1   {_._c_siffer_ant_div_inc}
        {_._v_n} = int({_._v_n} / 10)   {_._c_eks_siffer_del_10_iter}

    return {_._v_siffer_ant}

{_._c_fnc_siffer_antall_core}
{_._v_siffer_ant} = {_._f_siffer_antall_divisjon_C}({_._v_n})

{_._c_print_legacy}
print(f"{_._r_ant_siffer_i} {{{_._v_n}}} {_._r_er}{_._v_kolon} {{{_._v_siffer_ant}}}")
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