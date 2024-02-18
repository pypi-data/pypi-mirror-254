from __init__ import Pref, Datafil


##########################################
# Pref
##########################################

__   = Pref()
_  = Datafil()


##########################################
# Create
##########################################

_fil_navn_src = __._datatype_oversikt_src_py


##########################################
# Hotkeys
##########################################

# python /Users/krj/Desktop/program/src/_dir_1/bld/data_fil/_exe/python/tutorial/variabel/datatype/_def/datatype_oversikt.py


##########################################
# Fil content
##########################################

_fil_content = f"""
{_._h_top_py}
{_._p_datatype_oversikt}

{_._c_variabler_L}
{_._v_eks_str}          = str()
{_._v_eks_int}          = int()
{_._v_eks_float}        = float()
{_._v_eks_complex}      = complex()
{_._v_eks_list}         = list()
{_._v_eks_tuple}        = tuple()
{_._v_eks_range}        = range(0, 10) {_._c_datatype_range}
{_._v_eks_dict}         = dict()
{_._v_eks_set}          = set()
{_._v_eks_fronzenset}   = frozenset()
{_._v_eks_bool}         = bool()
{_._v_eks_bytes}        = bytes()
{_._v_eks_bytearray}    = bytearray()
{_._v_eks_memoryview}   = memoryview({_._v_eks_bytearray}) {_._c_datatype_memoryview}
{_._v_eks_none}         = None

{_._c_print_datatype}
print("{_._r_datatype_python}{_._v_kolon}")
print(type({_._v_eks_str}))
print(type({_._v_eks_int}))
print(type({_._v_eks_float}))
print(type({_._v_eks_complex}))
print(type({_._v_eks_list}))
print(type({_._v_eks_tuple}))
print(type({_._v_eks_range}))
print(type({_._v_eks_dict}))
print(type({_._v_eks_set}))
print(type({_._v_eks_fronzenset}))
print(type({_._v_eks_bool}))
print(type({_._v_eks_bytes}))
print(type({_._v_eks_bytearray}))
print(type({_._v_eks_memoryview}))
print(type({_._v_eks_none}))
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
