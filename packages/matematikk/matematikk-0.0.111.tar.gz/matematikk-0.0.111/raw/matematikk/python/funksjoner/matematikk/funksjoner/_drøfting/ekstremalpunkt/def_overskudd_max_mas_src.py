from __init__ import Pref, Datafil


##########################################
# Pref
##########################################

__   = Pref()
_  = Datafil()


##########################################
# Create
##########################################

_fil_navn_src = __._def_overskudd_max_mas_src


##########################################
# Hotkeys
##########################################

# python /Users/krj/Desktop/program/src/_dir_1/bld/data_fil/_exe/python/funksjoner/matematikk/funksjoner/_drøfting/ekstremalpunkt/def_overskudd_max_as.py


##########################################
# Fil content
##########################################

_fil_content = f"""
{_._h_top_py}

{_._c_imp_from_matematikk_import_ekstremalpunkt_max_Symbol_C}

{_._f_overskudd_max_def}

# Alias > 1
overskudd_maks          = overskudd_max
overskudd_maksimalt     = overskudd_max
overskudd_mest          = overskudd_max
overskudd_storst        = overskudd_max
overskudd_størst        = overskudd_max

# Alias > 2
maks_overskudd          = overskudd_max
maksimalt_overskudd     = overskudd_max
mest_overskudd          = overskudd_max
storst_overskudd        = overskudd_max
størst_overskudd        = overskudd_max
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