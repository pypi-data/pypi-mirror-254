from __init__ import Pref, Datafil


##########################################
# Pref
##########################################

__   = Pref()
_  = Datafil()


##########################################
# Create
##########################################

_fil_navn_src = __._datatype_set_remove_src_py


##########################################
# Hotkeys
##########################################

# python /Users/krj/Desktop/program/src/_dir_1/bld/data_fil/_exe/python/tutorial/variabel/datatype/set/datatype_set_remove.py


##########################################
# Fil content
##########################################

_fil_content = f"""
{_._h_top_py}
{_._p_datatype_set_remove}

{_._c_variabler_L}
{_._v_sett} = {_._e_sett}

{_._c_datatype_set_print_original}
print(f"{_._r_datatype_set_originalt}{_._v_kolon} {{{_._v_sett}}}")

{_._c_datatype_set_remove}
{_._v_sett}.remove("{_._e_sett_el_bil}")

{_._c_datatype_set_print_updated}
print(f"{_._r_datatype_set_updated}{_._v_kolon} {{{_._v_sett}}}")
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
