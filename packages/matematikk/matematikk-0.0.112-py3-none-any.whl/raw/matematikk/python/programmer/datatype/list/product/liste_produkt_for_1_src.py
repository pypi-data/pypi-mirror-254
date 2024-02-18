from __init__ import Pref, Datafil


##########################################
# Pref
##########################################

__   = Pref()
_  = Datafil()


##########################################
# Create
##########################################

_fil_navn_src = __._liste_produkt_for_src_py


##########################################
# Hotkeys
##########################################

# python /Users/krj/Desktop/program/src/_dir_1/bld/data_fil/_exe/python/programmer/datatype/list/product/liste_produkt_for_1.py


##########################################
# Fil content
##########################################

_fil_content = f"""
{_._h_top_py}
{_._p_list_product}

{_._c_verdier_L}
{_._v_liste} = {_._e_list_product_for_arr}

{_._c_fn_product_arr}
def {_._f_product_arr}({_._v_liste}):

	{_._c_startverdi_1}
	{_._v_produkt} = 1

	{_._c_oppdater_sum_for_hver_iter}
	for {_._v_el} in {_._v_liste}:
		{_._v_produkt} *= {_._v_el}

	return({_._v_produkt})

{_._c_fnc_sum_core}
{_._v_produkt} = {_._f_product_arr}({_._v_liste})

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
