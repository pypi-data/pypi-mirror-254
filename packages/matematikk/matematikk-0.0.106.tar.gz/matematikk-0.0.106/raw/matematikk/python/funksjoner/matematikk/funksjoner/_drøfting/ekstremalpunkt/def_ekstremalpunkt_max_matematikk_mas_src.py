from __init__ import Pref, Datafil


##########################################
# Pref
##########################################

__   = Pref()
_  = Datafil()


##########################################
# Create
##########################################

_fil_navn_src = __._def_ekstremalpunkt_max_matematikk_mas_src


##########################################
# Hotkeys
##########################################

# python /Users/krj/Desktop/program/src/_dir_1/bld/data_fil/_exe/python/funksjoner/matematikk/funksjoner/_drøfting/ekstremalpunkt/def_ekstremalpunkt_max_matematikk_as.py


##########################################
# Fil content
##########################################

_fil_content = f"""
{_._h_top_py}

{_._c_imp_from_matematikk_import_superlos_diff_Symbol_C}

{_._f_ekstremalpunkt_max_def}


# Alias > Right
ekstremalpunkt_maks             = ekstremalpunkt_max
ekstremalpunkt_maksimalt        = ekstremalpunkt_max
toppunkt                        = ekstremalpunkt_max

# Alias > Reversed > ...
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