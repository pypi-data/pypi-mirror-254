from __init__ import Pref, Datafil


##########################################
# Pref
##########################################

__   = Pref()
_  = Datafil()


##########################################
# Create
##########################################

_fil_navn_src = __._rente_opptjent_src_py


##########################################
# Hotkeys
##########################################

# python /Users/krj/Desktop/program/src/_dir_1/bld/data_fil/_exe/python/programmer/economics/rente/rente_opptjent_1.py


##########################################
# Fil content
##########################################

_fil_content = f"""
{_._h_top_py}
{_._p_rente_opptjent}

{_._c_verdier_L}
{_._v_belop_start}   = {_._e_rente_opptjent_belop_grunn_val}   {_._c_belop_start}
{_._v_perioder_ant}  = {_._e_rente_opptjent_perioder_ant_val}     {_._c_periode_ant}
{_._v_rente_prosent} = {_._e_rente_opptjent_rente_fot_val}    {_._c_rente_prosent}

{_._c_Vekstfaktor}
{_._v_vekstfaktor} = 1 + ({_._v_rente_prosent} / 100)
{_._v_belop_total} = {_._v_belop_start} * {_._v_vekstfaktor}**{_._v_perioder_ant}

{_._c_rente_opptjent}
{_._v_rente_opptjent} = {_._v_belop_total} - {_._v_belop_start}

{_._c_print_legacy}
print(f"{_._r_belop_start}      {_._v_kolon} {{{_._v_belop_start}}}")
print(f"{_._r_periode_ant} {_._v_kolon} {{{_._v_perioder_ant}}}")
print(f"{_._r_rente_prosent}       {_._v_kolon} {{{_._v_rente_prosent}}} {_._v_prosent_sym}")
print(f"{_._r_vekstfaktor}     {_._v_kolon} {{{_._v_vekstfaktor}}}")
print(f"{_._r_rente_opptjent}  {_._v_kolon} {{{_._v_rente_opptjent}}}")
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
