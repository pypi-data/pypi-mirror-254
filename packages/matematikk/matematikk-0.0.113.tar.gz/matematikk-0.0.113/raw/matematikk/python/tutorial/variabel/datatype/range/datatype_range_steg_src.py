from __init__ import Pref, Datafil


##########################################
# Pref
##########################################

__   = Pref()
_  = Datafil()


##########################################
# Create
##########################################

_fil_navn_src = __._datatype_range_steg_src_py


##########################################
# Hotkeys
##########################################

# python /Users/krj/Desktop/program/src/_dir_1/bld/data_fil/_exe/python/tutorial/variabel/datatype/range/datatype_range_steg.py


##########################################
# Fil content
##########################################

_fil_content = f"""
{_._h_top_py}
{_._p_datatype_range_steg}

{_._c_variabler_L}
{_._v_intervall} = {_._e_range_steg} {_._c_datatype_range_steg_husk}

{_._c_datatype_range_steg}
for {_._v_tall} in {_._v_intervall}:
    print({_._v_tall})
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
