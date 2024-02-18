# 🚀 programmering.no | 🤓 matematikk.as

# 1: SUPER --> from sympy import Symbol, diff
# 1: SUPER --> from matematikk import superløs

# 2: test
from sympy import diff
from matematikk import superløs, Symbol


def ekstremalpunkt_max(variabel = Symbol(""),
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
ekstremalpunkt_maks             = ekstremalpunkt_max
ekstremalpunkt_maksimalt        = ekstremalpunkt_max
toppunkt                        = ekstremalpunkt_max

# Alias > Reversed > ...