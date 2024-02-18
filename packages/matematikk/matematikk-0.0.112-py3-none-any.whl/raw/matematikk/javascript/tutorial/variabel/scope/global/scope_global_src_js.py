from __init__ import Pref, Datafil


##########################################
# Pref
##########################################

__   = Pref()
_  = Datafil()


##########################################
# Create
##########################################

_fil_navn_src = __._scope_global_src_js_py


##########################################
# Fil content
##########################################

_fil_content = f"""
{_._h_js_top}
{_._p_js_scope_global}

{_._c_js_scope_global_vari}
{_._v_js_var} {_._v_epler_store}       = "30"{_._v_semikolon}
{_._v_js_const} {_._v_epler_medium}    = "20"{_._v_semikolon}
{_._v_js_let} {_._v_epler_liten}       = "10"{_._v_semikolon}

{_._c_js_sett_vari}
{_._v_js_docu_gebi_1}"{_._v_js_eks_scope_global}"{_._v_js_docu_gebi_2}
= {_._v_epler_store} + {_._v_epler_medium} + {_._v_epler_liten}
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
