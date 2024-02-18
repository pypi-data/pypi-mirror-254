# 🚀 programmering.no | 🤓 matematikk.as

from matematikk import superløs, Symbol, diff

def overskudd_max(variabel = Symbol(""),
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

# Alias > Right
overskudd_maks          = overskudd_max
overskudd_maksimalt     = overskudd_max
overskudd_mest          = overskudd_max
overskudd_storst        = overskudd_max
overskudd_størst        = overskudd_max

# Alias > Reversed
maks_overskudd          = overskudd_max
maksimalt_overskudd     = overskudd_max
mest_overskudd          = overskudd_max
storst_overskudd        = overskudd_max
størst_overskudd        = overskudd_max


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
