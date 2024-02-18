from __init__ import Pref, Datafil


##########################################
# Pref
##########################################

__   = Pref()
_  = Datafil()


##########################################
# Create
##########################################

_fil_navn_src = __._ascii_input_src_py


##########################################
# Hotkeys
##########################################

# python /Users/krj/Desktop/program/src/_dir_1/bld/data_fil/_exe/python/programmer/datatype/str/ascii/ascii_2_input.py


##########################################
# Fil content
##########################################

_fil_content = f"""
{_._h_top_py}
{_._p_ascii}

{_._c_input}
{_._v_string} = input("{_._i_string}")

{_._c_fn_ascii_print}
def {_._f_ascii_print}({_._v_string}):

    {_._c_print_legacy}
    print("{_._r_ascii_strek}")
    print("{_._r_ascii_char_ascii}")
    print("{_._r_ascii_strek}")

    {_._c_ascii_char}
    for {_._v_char} in {_._v_string}:
        {_._v_ascii} = ord({_._v_char})
        print(f"{{{_._v_char}}} {_._v_arrow_slim_dobbel} {{{_._v_ascii}}}")

{_._c_fnc_ascii_print}
{_._f_ascii_print}({_._v_string})
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
