from __init__ import Pref, Datafil


##########################################
# Pref
##########################################

__   = Pref()
_  = Datafil()


##########################################
# Create
##########################################

_fil_navn_src = __._datatype_nonetype_def_src_py


##########################################
# Hotkeys
##########################################

# python /Users/krj/Desktop/program/src/_dir_1/bld/data_fil/_exe/python/tutorial/variabel/datatype/nonetype/datatype_nonetype_def.py


##########################################
# Fil content
##########################################

_fil_content = f"""
{_._h_top_py}
{_._p_datatype_nonetype_def}

{_._c_variabler_L}
{_._v_bruker_aktiv} = {_._e_nonetype_val}

{_._c_datatype_nonetype_print}
if {_._v_bruker_aktiv} == None:
    print("{_._r_datatype_nonetype_print_none}")
if {_._v_bruker_aktiv} == True:
    print("{_._r_datatype_nonetype_print_true}")
if {_._v_bruker_aktiv} == False:
    print("{_._r_datatype_nonetype_print_false}")
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
