from __init__ import Pref, Datafil


##########################################
# Pref
##########################################

__   = Pref()
_  = Datafil()


##########################################
# Create
##########################################

_fil_navn_src = __._pyramide_src_py


##########################################
# Hotkeys
##########################################

# python /Users/krj/Desktop/program/src/_dir_1/bld/data_fil/_exe/python/programmer/matematikk/tallteori/figurtall/pyramide//pyramide.py


##########################################
# Fil content
##########################################

_fil_content = f"""
{_._h_top_py}
{_._p_pyramide_1}
{_._p_pyramide_2}
{_._p_pyramide_3}
{_._p_pyramide_4}
{_._p_pyramide_5}

{_._c_verdier_L}
{_._v_ant_max}      = {_._e_pyramide_ant_max}    {_._c_pyramide_ant_klosser}
{_._v_ant_fig}      = {_._e_pyramide_ant_fig}        {_._c_pyramide_ant_klosser_fig}
{_._v_ant_totalt}   = {_._e_pyramide_ant_totalt}        {_._c_pyramide_ant_klosser_tot}
{_._v_n}            = {_._e_pyramide_fig_nr}        {_._c_pyramide_fig_nr}

{_._c_pyramide_while}
while {_._v_ant_totalt} <= {_._v_ant_max}:

    {_._c_pyramide_update}
    {_._v_ant_fig}      += {_._v_n}**2
    {_._v_ant_totalt}   += {_._v_ant_fig}

    {_._c_pyramide_print}
    print("")
    print(f"{_._r_pyramide_fig_nr} {_._v_kolon} {{{_._v_n}}}")
    print(f"{_._r_pyramide_i_fig}  {_._v_kolon} {{{_._v_ant_fig}}}")
    print(f"{_._c_totalt_C} {_._v_kolon} {{{_._v_ant_totalt}}}")

    {_._c_pyramide_inc}
    {_._v_n} += 1
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
