from __init__ import Pref, Datafil


##########################################
# Pref
##########################################

__   = Pref()
_  = Datafil()


##########################################
# Create
##########################################

_fil_navn_src = __._matrise_transponering_array_src_py


##########################################
# Hotkeys
##########################################

# python /Users/krj/Desktop/program/src/_dir_1/bld/data_fil/_exe/python/programmer/matematikk/matrise/transpose/matrise_transponering_array.py


##########################################
# Fil content
##########################################

_fil_content = f"""
{_._h_top_py}
{_._p_list_matrise_transpose}

import numpy

{_._c_matrise_datatype}
{_._v_matrise} = {_._e_matrise_transpose_array}

{_._c_print_legacy}
print("")
print("{_._r_matrise_datatype}{_._v_kolon}")
print({_._v_matrise})

{_._c_matrise_matematisk}
{_._v_matrise} = numpy.array({_._v_matrise})

{_._c_print_legacy}
print("")
print("{_._r_matrise_matematisk}{_._v_kolon}")
print({_._v_matrise})

{_._c_print_legacy}
print("")
print("{_._r_matrise_transpose}{_._v_kolon}")
print({_._v_matrise}.T)
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
