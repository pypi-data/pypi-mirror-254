# 🚀 programmering.no | 🤓 matematikk.as

from sympy import Symbol, diff
from matematikk import superløs

def overskudd_maks(variabel = Symbol(""),
                       uttrykk  = Symbol(""),
                       rund     = -1,
                       debug    = -1):

    # Deriverer uttrykk mhp. variabel og får df
    df = diff(uttrykk, variabel) # f'(x)

    # Løser likningen df = 0
    variabel_max = superløs(variabel = variabel,
                            vs       = df,
                            hs       = 0,
                            rund     = rund,
                            debug    = debug)

    return variabel_max

"""
from matematikk import ekstremalpunkt_max, Symbol

def overskudd_maks(variabel = Symbol(""),
                  uttrykk  = Symbol(""),
                  rund     = None,
                  debug    = -1):

    # overskudd_max() er en undergruppe av ekstremalpunkt_max()
    variabel_max = ekstremalpunkt_max(variabel = variabel,
                                      uttrykk  = uttrykk,
                                      rund     = rund,
                                      debug    = debug)

    return variabel_max
"""