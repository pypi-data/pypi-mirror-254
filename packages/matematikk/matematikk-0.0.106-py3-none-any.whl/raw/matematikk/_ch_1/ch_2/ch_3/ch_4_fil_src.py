from __init__ import Pref, Datafil


##########################################
# Pref
##########################################

__   = Pref()
_  = Datafil()


##########################################
# Create
##########################################

_fil_navn_src = __._chain_5_fil


##########################################
# Hotkeys
##########################################

# python /Users/krj/Desktop/program/src/_dir_1/bld/matematikk/src/matematikk/_ch_1/ch_2/ch_3/ch_4_fil.py


##########################################
# Fil content
##########################################

_fil_content = f"""
{_._h_top_py}
{_._c_s1_e_2023h_del_1_oppg_5_udir_i}
{_._c_s1_e_2023h_del_1_oppg_5_ii}

def ch_5_fn():
    print("Dette er en vellykket chain 5-test!")

# Calling-test
# print("Kaller ch_5_fn() ...")
# ch_5_fn()
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
