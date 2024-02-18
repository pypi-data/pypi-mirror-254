from __init__ import Pref, Datafil


##########################################
# Pref
##########################################

__   = Pref()
_  = Datafil()


##########################################
# Create
##########################################

_fil_navn_src = __._variabeltype_var_index_src_html_py


##########################################
# Fil content
##########################################

_fil_content = f"""
{_._v_html_tag_doctype}
{_._v_html_tag_html_1}
	{_._v_html_tag_body_1_dark}
		{_._v_html_tag_id_1}"{_._v_js_eks_var}"{_._v_html_tag_id_2}
		{_._v_html_tag_script_1}"{_._v_html_variabeltype_var_js}"{_._v_html_tag_script_2}
	{_._v_html_tag_body_2}
{_._v_html_tag_html_2}
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
