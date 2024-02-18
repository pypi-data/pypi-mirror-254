from __init__ import Pref, Datafil


##########################################
# Pref
##########################################

__   = Pref()
_  = Datafil()


##########################################
# Create
##########################################

_fil_navn_src = __._datatype_bool_none_src_py


##########################################
# Hotkeys
##########################################

# python /Users/krj/Desktop/program/src/_dir_1/bld/data_fil/_exe/python/tutorial/variabel/datatype/bool/datatype_bool_none.py


##########################################
# Fil content
##########################################

_fil_content = f"""
{_._h_top_py}
{_._p_datatype_bool_none}

{_._c_variabler_L}
{_._v_solskinn} = {_._e_solskinn_none}

{_._c_print_legacy}
print(f"{_._r_datatype_bool_solskinn_tomorrow}{_._v_kolon} {{{_._v_solskinn}}}")
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
