from __init__ import Pref, Datafil


##########################################
# Pref
##########################################

__   = Pref()
_  = Datafil()


##########################################
# Create
##########################################

_fil_navn_src = __._liste_rotasjon_str_input_src_py


##########################################
# Hotkeys
##########################################

# python /Users/krj/Desktop/program/src/_dir_1/bld/data_fil/_exe/python/programmer/datatype/list/rotate/liste_rotasjon_str_2_input.py


##########################################
# Fil content
##########################################

_fil_content = f"""
{_._h_top_py}
{_._p_list_rotate}
{_._p_list_rotate_def_1}
{_._p_list_rotate_def_2}
{_._p_list_rotate_def_3}
{_._p_list_rotate_eks}

{_._c_input}
{_._v_liste} = input("{_._i_list_rotate}") {_._c_input_husk_par_square_str}
{_._v_rotate_retning} = input("{_._i_list_rotate_retning}")
{_._v_rotate_antall} = input("{_._i_list_rotate_antall}")

{_._c_fn_str_til_int_arr}
{_._f_str_til_str_liste_def}

{_._c_fn_rotate_arr}
def {_._f_rotate_arr}({_._v_liste}, {_._v_rotate_retning}, {_._v_rotate_antall}):

	{_._v_liste}          = {_._f_str_til_str_liste}({_._v_liste})
	{_._v_rota_ant}       = int({_._v_rotate_antall})
	{_._v_rotate_arr_1} = list()
	{_._v_rotate_arr_2} = list()
	{_._v_ferdig_liste}   = list()

	{_._v_i} = 0
	while {_._v_i} < len({_._v_liste}):

        {_._c_eks_list_rotate_1}
		if {_._v_rotate_retning} == "{_._v_v}":
			if {_._v_i} <  {_._v_rota_ant}: 			   {_._v_rotate_arr_1}.append({_._v_liste}[{_._v_i}]) {_._c_eks_list_rotate_1_1}
			if {_._v_i} >= {_._v_rota_ant}: 			   {_._v_rotate_arr_2}.append({_._v_liste}[{_._v_i}]) {_._c_eks_list_rotate_1_2}

        {_._c_eks_list_rotate_2}
		if {_._v_rotate_retning} == "{_._v_h}":
			if {_._v_i} >= len({_._v_liste}) - {_._v_rota_ant}: {_._v_rotate_arr_2}.append({_._v_liste}[{_._v_i}]) {_._c_eks_list_rotate_2_1}
			if {_._v_i} <  len({_._v_liste}) - {_._v_rota_ant}: {_._v_rotate_arr_1}.append({_._v_liste}[{_._v_i}]) {_._c_eks_list_rotate_2_2}

        {_._c_inc_i}
		{_._v_i} += 1

	{_._c_list_rotate_arr_add}
	{_._v_ferdig_liste} =  {_._v_rotate_arr_2} + {_._v_rotate_arr_1}

	return {_._v_ferdig_liste}

{_._c_fnc_rotate_arr}
{_._v_rotate_left_arr} = {_._f_rotate_arr}({_._v_liste}, "{_._v_v}", {_._v_rotate_antall}) {_._c_eks_list_rotate_1_call}
{_._v_rotate_right_arr} = {_._f_rotate_arr}({_._v_liste}, "{_._v_h}", {_._v_rotate_antall})

{_._c_print_legacy}
print(f"{_._r_list_rotate_pre}   	         {_._v_kolon} {{{_._v_liste}}}")
if {_._v_rotate_retning} == "{_._v_v}":
	print(f"{_._r_list_rotate_pre_left} ({{{_._v_rotate_antall}}}) {_._v_kolon} {{{_._v_rotate_left_arr}}}")
if {_._v_rotate_retning} == "{_._v_h}":
	print(f"{_._r_list_rotate_pre_right}   ({{{_._v_rotate_antall}}}) {_._v_kolon} {{{_._v_rotate_right_arr}}}")
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
