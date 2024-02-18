# 🚀 programmering.no | 🤓 matematikk.as
# vekstfaktor() finner vekstfaktoren (Matematikk AS)
# Andre navn vekst_faktor()

from matematikk import Symbol

def vekstfaktor_cas(fortegn = str(), p = Symbol("")):

    # Vekstfaktor er definert som V = 1 ± p / 100
    if fortegn == "+": return 1 + p / 100 # "+": Øker, "-": Minker
    if fortegn == "-": return 1 - p / 100 # p: Prosentvis vekst [%]

v = vekstfaktor_cas(fortegn = "+", p = Symbol("p"))
  
print(v)
