from __init__ import Pref, Datafil


##########################################
# Pref
##########################################

__   = Pref()
_  = Datafil()


##########################################
# Create
##########################################

_fil_navn_src = __._datatype_dict_felt_src_py


##########################################
# Hotkeys
##########################################

# python /Users/krj/Desktop/program/src/_dir_1/bld/data_fil/_exe/python/tutorial/variabel/datatype/dict/datatype_dict_felt.py


##########################################
# Fil content
##########################################

_fil_content = f"""
{_._h_top_py}
{_._p_datatype_dict_change}

{_._c_variabler_L}
{_._v_obj} = {_._e_obj_key_value}

{_._c_datatype_print_obj}
print({_._v_obj})

{_._c_datatype_dict_felt}
{_._v_obj}["{_._e_obj_key_emo}"] = "{_._e_obj_key_emo_sym}"

{_._c_datatype_print_obj_updated}
print({_._v_obj})
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
