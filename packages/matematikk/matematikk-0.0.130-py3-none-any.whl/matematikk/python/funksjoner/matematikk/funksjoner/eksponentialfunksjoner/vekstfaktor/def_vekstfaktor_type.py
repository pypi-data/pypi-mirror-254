# 🚀 programmering.no | 🤓 matematikk.as
# vekstfaktor() finner vekstfaktoren (Matematikk AS)
# Andre navn vekst_faktor()

def vekstfaktor_type(fortegn = str(), p = float()):

    # Vekstfaktor er definert som V = 1 ± p / 100
    if fortegn == "+": return 1 + p / 100 # "+": Øker, "-": Minker
    if fortegn == "-": return 1 - p / 100 # p: Prosentvis vekst [%]

v = vekstfaktor_type(fortegn = "+", p = 3.1)

print(v)
