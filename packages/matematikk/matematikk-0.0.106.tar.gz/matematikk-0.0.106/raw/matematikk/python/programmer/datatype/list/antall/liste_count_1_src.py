from __init__ import Pref, Datafil


##########################################
# Pref
##########################################

__   = Pref()
_  = Datafil()


##########################################
# Create
##########################################

_fil_navn_src = __._liste_count_src_py


##########################################
# Hotkeys
##########################################

# python /Users/krj/Desktop/program/src/_dir_1/bld/data_fil/_exe/python/programmer/datatype/list/antall/liste_count_1.py


##########################################
# Fil content
##########################################

_fil_content = f"""
{_._h_top_py}
{_._p_list_count}

{_._c_verdier_L}
{_._v_liste}    = {_._e_list_count_arr}
{_._v_karakter} = "{_._e_list_count_val}"

{_._c_antall}
{_._v_antall} = {_._v_liste}.count("{_._e_list_count_val}")

{_._c_print_legacy}
print(f"{_._c_list_C}{_._v_kolon} {{{_._v_liste}}}")
if {_._v_antall} > 0:
    print(f"{{{_._v_antall}}} {_._r_elever_fikk} {_._r_karakter} {{{_._v_karakter}}}")
else:
	print("{_._r_ingen_elever_fikk} {_._r_karakter} {{{_._v_karakter}}}")
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
