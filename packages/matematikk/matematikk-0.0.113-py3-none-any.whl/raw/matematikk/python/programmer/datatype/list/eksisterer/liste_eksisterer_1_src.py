from __init__ import Pref, Datafil


##########################################
# Pref
##########################################

__   = Pref()
_  = Datafil()


##########################################
# Create
##########################################

_fil_navn_src = __._liste_eksisterer_src_py

##########################################
# Hotkeys
##########################################

# python /Users/krj/Desktop/program/src/_dir_1/bld/data_fil/_exe/python/programmer/datatype/list/eksisterer/liste_eksisterer_1.py


##########################################
# Fil content
##########################################

_fil_content = f"""
{_._h_top_py}
{_._p_list_eksisterer}

{_._c_verdier_L}
{_._v_liste} = {_._e_list_eksisterer_arr}
{_._v_dyr}   = "{_._e_list_eksisterer_val}"

{_._c_list_eksisterer_if}
print(f"{_._c_list_C}{_._v_kolon} {{{_._v_liste}}}")
if {_._v_dyr} in {_._v_liste}:
    print(f"{_._r_Ja}{_._v_komma} {{{_._v_dyr}}} {_._r_list_eksisterer_i_arr}")
else:
	print("{_._r_Nei}{_._v_komma} {_._r_list_eksisterer_not_i_arr_el}")
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
