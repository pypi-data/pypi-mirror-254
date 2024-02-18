from __init__ import Pref, Datafil


##########################################
# Pref
##########################################

__   = Pref()
_  = Datafil()


##########################################
# Create
##########################################

_fil_navn_src = __._variabeltype_var_src_js_py


##########################################
# Fil content
##########################################

_fil_content = f"""
{_._h_js_top}
{_._p_js_var_def}

{_._c_js_variabler}
{_._v_js_var} {_._v_min_variabel} = 42{_._v_semikolon}

{_._c_js_sett_vari}
{_._v_js_docu_gebi_1}"{_._v_js_eks_var}"{_._v_js_docu_gebi_2} = {_._v_min_variabel}
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
