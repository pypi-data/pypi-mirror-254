# 🚀 programmering.no | 🤓 matematikk.as
# vekstfaktor() finner vekstfaktoren (Matematikk AS)
# Andre navn vekst_faktor()

def vekstfaktor(p, fortegn):

    # Vekstfaktor er definert som V = 1 ± p / 100
    if fortegn == "+": return 1 + p / 100 # "+": Øker, "-": Minker
    if fortegn == "-": return 1 - p / 100 # p: Prosentvis vekst [%]

v = vekstfaktor(fortegn = "+", p = 3.1)

print(v)
