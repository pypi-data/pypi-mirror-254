from __init__ import Pref, Datafil


##########################################
# Pref
##########################################

__   = Pref()
_  = Datafil()


##########################################
# Create
##########################################

_fil_navn_src = __._siffer_antall_divisjon_src_py


##########################################
# Hotkeys
##########################################

# python /Users/krj/Desktop/program/src/_dir_1/bld/data_fil/_exe/python/programmer/matematikk/aritmetikk/siffer/siffer_antall_divisjon_1.py


##########################################
# Fil content
##########################################

_fil_content = f"""
{_._h_top_py}
{_._p_siffer_ant}

{_._c_konstanter}
{_._v_n} = {_._e_siffer_antall_divisjon_val}

{_._c_fn_siffer_antall_core}
{_._f_siffer_antall_def}

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