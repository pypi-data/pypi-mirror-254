from __init__ import Pref, Datafil


##########################################
# Pref
##########################################

__   = Pref()
_  = Datafil()


##########################################
# Create
##########################################

_fil_navn_src = __._matrise_transponering_src_py


##########################################
# Hotkeys
##########################################

# python /Users/krj/Desktop/program/src/_dir_1/bld/data_fil/_exe/python/programmer/matematikk/matrise/transpose/matrise_transponering.py


##########################################
# Fil content
##########################################

_fil_content = f"""
{_._h_top_py}
{_._p_list_matrise_transpose}

import numpy

{_._c_verdier_L}
{_._v_matrise} = {_._e_matrise_transpose}

{_._c_matrise_transpose}
{_._v_matrise_transpose} = numpy.transpose({_._v_matrise})

{_._c_print_legacy}
print("")
print("{_._r_matrise}{_._v_kolon}")
print({_._v_matrise})

print("")
print("{_._r_matrise_transposed}{_._v_kolon}")
print({_._v_matrise_transpose})
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
