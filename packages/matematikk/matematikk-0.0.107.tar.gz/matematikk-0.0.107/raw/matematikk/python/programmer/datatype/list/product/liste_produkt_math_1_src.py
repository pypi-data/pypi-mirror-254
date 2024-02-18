from __init__ import Pref, Datafil


##########################################
# Pref
##########################################

__   = Pref()
_  = Datafil()


##########################################
# Create
##########################################

_fil_navn_src = __._liste_produkt_math_src_py


##########################################
# Hotkeys
##########################################

# python /Users/krj/Desktop/program/src/_dir_1/bld/data_fil/_exe/python/programmer/datatype/list/product/liste_produkt_math_1.py


##########################################
# Fil content
##########################################

_fil_content = f"""
{_._h_top_py}
{_._p_list_product_math}

import math

{_._c_verdier_L}
{_._v_liste} = {_._e_list_product_for_numpy_arr}

{_._c_list_product_math}
{_._v_produkt} = math.prod({_._v_liste})

{_._c_print_legacy}
print(f"{_._c_list_C}                   {_._v_kolon} {{{_._v_liste}}}")
print(f"{_._r_list_product_el} {_._v_kolon} {{{_._v_produkt}}}")
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
