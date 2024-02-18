from __init__ import Pref, Datafil


##########################################
# Pref
##########################################

__   = Pref()
_  = Datafil()


##########################################
# Create
##########################################

_fil_navn_src = __._matrise_subtraksjon_src_py


##########################################
# Hotkeys
##########################################

# python /Users/krj/Desktop/program/src/_dir_1/bld/data_fil/_exe/python/programmer/matematikk/matrise/subtraksjon/matrise_subtraksjon.py


##########################################
# Fil content
##########################################

_fil_content = f"""
{_._h_top_py}
{_._p_list_matrise_subtraksjon}

import numpy as np

{_._c_verdier_L}
{_._v_matrise_A} = np.array({_._e_matrise_subtraksjon_matrise_A_val})
{_._v_matrise_B} = np.array({_._e_matrise_subtraksjon_matrise_B_val})

{_._c_print_legacy}
print("")
print("{_._r_matrise_A}{_._v_kolon}")
print({_._v_matrise_A})
print("")
print("{_._r_matrise_B}{_._v_kolon}")
print({_._v_matrise_B})

{_._c_matrise_subtraksjon_A_B}
{_._v_matrise_differanse} = np.subtract({_._v_matrise_A}, {_._v_matrise_B})

{_._c_print_legacy}
print("")
print("{_._r_matrise_subtraksjon}{_._v_kolon}")
print({_._v_matrise_differanse})
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
