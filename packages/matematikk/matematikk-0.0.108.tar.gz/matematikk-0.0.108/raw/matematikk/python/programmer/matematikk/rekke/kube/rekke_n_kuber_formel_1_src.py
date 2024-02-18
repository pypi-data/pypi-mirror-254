from __init__ import Pref, Datafil


##########################################
# Pref
##########################################

__   = Pref()
_  = Datafil()


##########################################
# Create
##########################################

_fil_navn_src = __._rekke_n_kuber_formel_src_py


##########################################
# Hotkeys
##########################################

# python /Users/krj/Desktop/program/src/_dir_1/bld/data_fil/_exe/python/programmer/matematikk/rekke/kube/rekke_n_kuber_formel_1.py


##########################################
# Fil content
##########################################

_fil_content = f"""
{_._h_top_py}
{_._p_rekke_kube}

{_._c_verdier_L}
{_._v_n} = {_._e_rekke_n_kuber_formel_val}

{_._c_fn_rekke_n_kuber_sum}
def {_._f_rekke_n_kuber_sum}({_._v_n}):

    {_._c_fo_rekke_kube}
    {_._v_sum} = int(({_._v_n} * ({_._v_n} + 1) / 2)**2)

    return {_._v_sum}

{_._c_fnc_rekke_n_kube_sum}
{_._v_sum} = {_._f_rekke_n_kuber_sum}({_._v_n})

{_._c_print_legacy}
print(f"{_._r_summen_av_de_n} {{{_._v_n}}} {_._r_first_kubene_er}{_._v_kolon} {{{_._v_sum}}}")
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
