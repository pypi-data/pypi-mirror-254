from __init__ import Pref, Datafil


##########################################
# Pref
##########################################

__   = Pref()
_  = Datafil()


##########################################
# Create
##########################################

_fil_navn_src = __._matrise_produkt_src_py


##########################################
# Hotkeys
##########################################

# python /Users/krj/Desktop/program/src/_dir_1/bld/data_fil/_exe/python/programmer/matematikk/matrise/produkt/matrise_produkt.py


##########################################
# Fil content
##########################################

_fil_content = f"""
{_._h_top_py}
{_._p_list_matrise_produkt}

import numpy as np

{_._c_matrise_A_3x3}
{_._v_matrise_A} = np.array({_._e_matrise_produkt_matrise_A_val})

{_._c_matrise_B_3x4}
{_._v_matrise_B} = np.array({_._e_matrise_produkt_matrise_B_val})

{_._c_matrise_produkt_A_B}
{_._v_matrise_produkt} = np.dot({_._v_matrise_A}, {_._v_matrise_B})

{_._c_matrise_produkt_A_B_radene}
for {_._v_r} in {_._v_matrise_produkt}:

    {_._c_matrise_produkt_A_B_rad}
	print({_._v_r})
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
