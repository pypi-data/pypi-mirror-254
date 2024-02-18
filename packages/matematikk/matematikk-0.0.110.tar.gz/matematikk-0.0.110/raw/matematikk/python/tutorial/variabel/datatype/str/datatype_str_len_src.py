from __init__ import Pref, Datafil


##########################################
# Pref
##########################################

__   = Pref()
_  = Datafil()


##########################################
# Create
##########################################

_fil_navn_src = __._datatype_str_len_src_py


##########################################
# Hotkeys
##########################################

# python /Users/krj/Desktop/program/src/_dir_1/bld/data_fil/_exe/python/tutorial/variabel/datatype/str/datatype_str_len.py


##########################################
# Fil content
##########################################

_fil_content = f"""
{_._h_top_py}
{_._p_datatype_str_len}

{_._c_variabler_L}
{_._v_hei}      = "{_._e_variabel_def}"
{_._v_char_ant} = len({_._v_hei})

{_._c_print_legacy}
print(f"{_._r_datatype_str_len_string}{_._v_kolon} {{{_._v_hei}}}")
print(f"{_._r_datatype_str_len}{_._v_kolon} {{{_._v_char_ant}}}")
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
