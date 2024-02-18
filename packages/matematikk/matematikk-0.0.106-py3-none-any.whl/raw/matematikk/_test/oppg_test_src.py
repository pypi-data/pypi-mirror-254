from __init__ import Pref, Datafil


##########################################
# Pref
##########################################

__   = Pref()
_  = Datafil()


##########################################
# Create
##########################################

_fil_navn_src = __._oppg_test_tmp


##########################################
# Hotkeys
##########################################

# python /Users/krj/Desktop/program/src/_dir_1/bld/matematikk/src/matematikk/_test/oppg_test.py


##########################################
# Fil content
##########################################

_fil_content = f"""
{_._h_top_py}
{_._c_s1_e_2023h_del_2_oppg_1_mas_i}
{_._c_s1_e_2023h_del_2_oppg_1_b_ii}
{_._c_python_cas}
{_._c_s1_e_2023h_del_2_oppg_1_b_5_mas_cmd}

{_._c_imp_from_matematikk_import_overskudd_max_reggis_Symbol_C}

{_._c_s1_e_2023h_del_2_oppg_1_a_oppg_tit}
{_._v_K} = {_._f_reggis_C}({_._v_variabel} = {_._c_s1_e_2023h_del_2_oppg_1_a_val_x_C},
           {_._v_grad}     = {_._c_s1_e_2023h_del_2_oppg_1_a_val_grad_C},
           {_._v_x_liste}  = {_._c_s1_e_2023h_del_2_oppg_1_a_val_x_ls_C},
           {_._v_y_liste}  = {_._c_s1_e_2023h_del_2_oppg_1_a_val_y_ls_C},
           {_._v_rund}     = {_._c_rund_default_2})
print({_._v_K})

{_._c_s1_e_2023h_del_2_oppg_1_b_oppg_tit}
{_._v_x_max} = {_._c_s1_e_2023h_del_2_oppg_1_b_7_call}
print({_._v_x_max})
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