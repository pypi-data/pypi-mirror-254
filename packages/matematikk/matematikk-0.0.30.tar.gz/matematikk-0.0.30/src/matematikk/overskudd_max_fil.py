# 🚀 programmering.no | 🤓 matematikk.as

from matematikk import Symbol
from ekstremalpunkt_max_fil import ekstremalpunkt_max

def overskudd_max(variabel = Symbol(""),
                  uttrykk  = Symbol(""),
                  rund     = None,
                  debug    = -1):

    # overskudd_max() er en undergruppe av ekstremalpunkt_max()
    variabel_max = ekstremalpunkt_max(variabel = variabel,
                                      uttrykk  = uttrykk,
                                      rund     = rund,
                                      debug    = debug)

    return variabel_max
