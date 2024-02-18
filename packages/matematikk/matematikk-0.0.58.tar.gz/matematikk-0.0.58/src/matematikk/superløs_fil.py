# 🚀 programmering.no | 🤓 matematikk.as

from matematikk import ConditionSet, core, Eq, FiniteSet, Intersection, nsolve, Reals, solve, solveset, Symbol

def superløs(variabel = Symbol(""),
             vs       = Symbol(""),
             hs       = Symbol(""),
             likning  = list(),
             rund     = -1,
             debug    = -1):

    vis_datatype = True
    losning_set, losning_set_sub = set(), set()
    losning_liste, losning_element, losning_rund_liste, losning_ut = list(), list(), list(), list()
    losning_rund_status, sett_typ, likn_ant, los_ant, _v_avrund_typ = str(), str(), str(), str(), str()
    losning_rund = float()

    if type(likning) != list: likning_tmp = likning; likning = []; likning.append(likning_tmp)

    if len(likning) == 0:
        likn_ant = "En likning"
        if type(variabel) == type(list()): variabel = variabel[0]
        if type(vs) != core.mul.Mul and type(vs) == type(list()): vs = vs[0]
        if type(hs) != core.mul.Mul and type(hs) == type(list()): hs = hs[0]
        _likning = Eq(vs, hs); losning_set = solveset(_likning, variabel, domain = Reals)

        if len(likning) == 0 and type(losning_set) == FiniteSet:
            sett_typ = "FiniteSet";
            if len(losning_set) == 1: los_ant = "en løsning"
            if len(losning_set) > 1: los_ant = str(len(losning_set)) + " " + "løsninger"

        if len(likning) == 0 and type(losning_set) == ConditionSet:
            sett_typ = "ConditionSet"; losning_element = nsolve(_likning, variabel, 1)
            los_ant = "en numerisk løsning"; losning_set = []; losning_set.append(losning_element)

        if len(likning) == 0 and type(losning_set) == Intersection:
            sett_typ = "Intersection"; losning_set_sub = losning_set.args[1]
            losning_element = losning_set_sub.args; losning_set = []; losning_set.append(losning_element); rund = -1
            if len(losning_set_sub) == 1: los_ant = "en løsning som er et uttrykk"
            if len(losning_set_sub) > 1: los_ant = str(len(losning_set_sub)) + " " + "løsninger som er uttrykk"

    if len(likning) > 0:
        sett_typ = ""; likn_ant = "Flere likninger (likningssett)"
        losning_set = solve(likning, variabel, dict=True)
        for i in range(len(losning_set)):
            koordinat_verdi_liste = list(); koordinat_variabel_rund_liste = list()
            for koordinat_variabel, koordinat_verdi in losning_set[i].items():
                koordinat_verdi_liste.append(koordinat_verdi)
                losning_rund = round(float(koordinat_verdi), rund)
                koordinat_variabel_rund_liste.append(losning_rund)
            losning_liste.append(koordinat_verdi_liste); losning_rund_liste.append(koordinat_variabel_rund_liste)

    for losning in losning_set:
        if rund == -1:
            _v_avrund_typ = "(eksakt)"; losning_rund_status = "Nei"; losning_rund_liste = ""
            if len(likning) == 0: losning_liste.append(losning); losning_ut = losning_liste
            if len(likning) > 0: losning_ut = losning_liste

        if rund != -1:
            _v_avrund_typ = "(avrundet)"; losning_rund_status = "Ja"
            if len(likning) == 0:
                losning_liste.append(losning); losning_rund = round(losning, rund)
                losning_rund_liste.append(losning_rund); losning_ut = losning_rund_liste
            if len(likning) > 0: losning_ut = losning_rund_liste

    if len(losning_ut) == 1: losning_ut = losning_ut[0]

    if debug == 1:
        print("")
        print(f"*** Debug ****")
        if vis_datatype == True:
            print(f"Data-type                        :: {sett_typ}")
        print(f"Løsnings-type                    :: {likn_ant} med {los_ant} {_v_avrund_typ}")
        print(f"Løsnings-sett                    :: {losning_set}")
        print(f"Løsnings-element(er)             :: {losning_liste}")
        print(f"Avrunding (ja/nei)               :: {losning_rund_status}")
        print(f"Løsnings-elemente(er) avrundet   :: {losning_rund_liste}")
        print(f"-----------------------------------")
        print(f"Løsning ut (returnert) -----------> {losning_ut}")
        print(f"-----------------------------------")

    return losning_ut


# Alias > Right
los                     = superløs
losning                 = superløs
løs                     = superløs
løsning                 = superløs
superlos                = superløs
super_los               = superløs
super_løs               = superløs

# Alias > Reversed
los_super               = superløs
løs_super               = superløs


##########################################
# Eksempler (kan fjernes)
##########################################

# Variabler
_blokk = 1
x = Symbol("x")
y = Symbol("y")

# Eksempler
if _blokk == 1:

    # Alle eksempler
    if _blokk == 1:

        # En likning
        if _blokk == 1:

            # En løsning (eksakt/ikke avrundet)
            if _blokk == 1:

                # Eksakt løsning for 3x = 1 mhp. x gir 1/3 (se NB om 0.333333333333333 nedenfor)

                # 3x = 1
                if _blokk == -1:

                    # 1/3
                    x_losning = superløs(variabel    = Symbol("x"),
                                         vs          = 3*Symbol("x"),
                                         hs          = 1,
                                         rund        = -1,
                                         debug       = 1)

                # x + 2/3 = 1 (NB)
                if _blokk == -1:

                    # - Her vil "eksakt løsning" for x + 2/3 bli 0.333333333333333 (og ikke x = 1/3)
                    # - Grunnen er at Python runder av 2/3 til 0.666666666666667 før tallet går inn i superløs()
                    # - Når 0.666666666666667 går inn i superløs() løses derfor dette som en float() (desimaltall)
                    # - Prøv derfor å bruke formen over hvis du vil ha helt eksakte løsninger med heltall,
                    #   f.eks. ved å gange opp likningen slik at ingen brøker går inn i superløs()

                    # 0.333333333333333
                    x_losning = superløs(variabel    = Symbol("x"),
                                         vs          = Symbol("x") + (1/3), # NB: Rundes av allerede her
                                         hs          = 1,
                                         rund        = -1,
                                         debug       = 1)

            # En løsning (avrundet)
            if _blokk == 1:

                # Alle avrundings-verdiene til rund-arg for f.eks. 3x = 1

                # Hvis rund = 3 -> 3.667
                if _blokk == -1:

                    # 3.667
                    x_losning = superløs(variabel    = Symbol("x"),
                                         vs          = 3*Symbol("x"),
                                         hs          = 11,
                                         rund        = 3,
                                         debug       = 1)

                # Hvis rund = 2 -> 3.67
                if _blokk == -1:

                    # 3.67
                    x_losning = superløs(variabel    = Symbol("x"),
                                         vs          = 3*Symbol("x"),
                                         hs          = 11,
                                         rund        = 2,
                                         debug       = 1)

                # Hvis rund = 1 -> 3.7
                if _blokk == -1:

                    # 3.7
                    x_losning = superløs(variabel    = Symbol("x"),
                                         vs          = 3*Symbol("x"),
                                         hs          = 11,
                                         rund        = 1,
                                         debug       = 1)

                # Hvis rund = 0 -> 4.00000000000000 (nærmeste "heltall" med alle desimaler)
                if _blokk == -1:

                    # 4.00000000000000
                    x_losning = superløs(variabel    = Symbol("x"),
                                         vs          = 3*Symbol("x"),
                                         hs          = 11,
                                         rund        = 0,
                                         debug       = 1)

                # Hvis rund = None -> 4 (nærmeste heltall, altså slik heltall er uten desimaler)
                if _blokk == -1:

                    # 4
                    x_losning = superløs(variabel    = Symbol("x"),
                                         vs          = 3*Symbol("x"),
                                         hs          = 11,
                                         rund        = None,
                                         debug       = 1)

                # Hvis rund = -1 (default setting) -> 11/3 (runder ikke av, se Type 1.1.1)
                if _blokk == -1:

                    # 11/3
                    x_losning = superløs(variabel    = Symbol("x"),
                                         vs          = 3*Symbol("x"),
                                         hs          = 11,
                                         rund        = -1,
                                         debug       = 1)

                # Hvis rund = "alt annet" -> 0.0 (ikke definert)
                if _blokk == -1:

                    # 0.0
                    x_losning = superløs(variabel    = Symbol("x"),
                                         vs          = 3*Symbol("x"),
                                         hs          = 11,
                                         rund        = -2,
                                         debug       = 1)

            # Flere løsninger (eksakt/ikke avrundet)
            if _blokk == 1:

                # - Flere løsninger for x^2 + x = 1

                # x^2 + x = 1
                if _blokk == -1:

                    # [-1/2 + sqrt(5)/2, -sqrt(5)/2 - 1/2]
                    x_losning = superløs(variabel    = Symbol("x"),
                                         vs          = Symbol("x")**2 + Symbol("x"),
                                         hs          = 1,
                                         rund        = -1,
                                         debug       = 1)

            # Flere løsninger (avrundet)
            if _blokk == 1:

                # - Se "En løsning (eksakt)" for alle eksempler på avrunding
                # - De samme avrundings-eksemplene for flere løsninger er helt like som for
                #   en løsning (eneste forsjell er at løsningene er samlet i en liste)

                # Likning: x^2 + x = 1
                if _blokk == -1:

                    # [-1/2 + sqrt(5)/2, -sqrt(5)/2 - 1/2]
                    x_losning = superløs(variabel    = Symbol("x"),
                                         vs          = Symbol("x")**2 + Symbol("x"),
                                         hs          = 1,
                                         rund        = 2,
                                         debug       = 1)

            # En numerisk løsning (ikke avrundet)
            if _blokk == 1:

                # Merk at numerisk løsning som oftest uansett er avrundet

                # Likning: 1.02^x + 1.03^x = 10
                if _blokk == -1:

                    # 63.31
                    x_losning = superløs(vs          = 1.02**Symbol("x") + 1.03**Symbol("x"),
                                         hs          = 10,
                                         variabel    = Symbol("x"),
                                         rund        = -1)

            # En numerisk løsning (avrundet)
            if _blokk == 1:

                # Likning: 1.02^x + 1.03^x = 10
                if _blokk == -1:

                    # 63.31
                    x_losning = superløs(vs          = 1.02**Symbol("x") + 1.03**Symbol("x"),
                                         hs          = 10,
                                         variabel    = Symbol("x"),
                                         rund        = 2)

            # En løsning som er et uttrykk
            if _blokk == 1:

                # Likning: x + y = 3
                if _blokk == -1:

                    # 3 - y
                    x_losning = superløs(vs          = Symbol("x") + Symbol("y"),
                                         hs          = 3,
                                         variabel    = Symbol("x"),
                                         rund        = 2,
                                         debug       = 1)

                # Likning: x + y = 3
                if _blokk == -1:

                    # 3 - x
                    y_losning = superløs(vs          = Symbol("x") + Symbol("y"),
                                         hs          = 3,
                                         variabel    = Symbol("y"),
                                         rund        = 2,
                                         debug       = 1)

            # Flere løsninger som er uttrykk
            if _blokk == 1:

                # Likning: 3*a*f**2 + 2*b*f = 0
                if _blokk == -1:

                    a = Symbol("a")
                    b = Symbol("b")
                    c = Symbol("c")

                    # (-b/(3*a) - sqrt(-3*a*c + b**2)/(3*a), -b/(3*a) + sqrt(-3*a*c + b**2)/(3*a))
                    x_losning = superløs(vs = 3 * a * x**2 + 2 * b * x + c,
                                         hs          = 0,
                                         variabel    = x,
                                         rund        = 2,
                                         debug       = 1)

            # Lister som argumenter
            if _blokk == 1:

                # Argunementene kan også være en kombinasjon av uttrykk og lister, som for f.eks. 3x = 11
                if _blokk == -1:

                    # 3.67
                    x_losning = superløs(variabel   = [x],
                                        likning    = 3 * x - 11,
                                        rund       = 2,
                                        debug      = 1)

                    print("")
                    print(f"Løsningen til likningen er {x} = {x_losning}")
                    print("")

                # Alle argumentene kan også være lister, som f.eks. 3x = 11
                if _blokk == -1:

                    # 3.67
                    x_losning = superløs(variabel   = [x],
                                        vs         = [3*x],
                                        hs         = [11],
                                        rund       = -1,
                                        debug      = 1)

                    print("")
                    print(f"Løsningen til likningen er {x} = {x_losning}")
                    print("")

        # Flere likninger (likningssett)
        if _blokk == 1:

            # Flere likninger med flere løsninger (eksakt)
            if _blokk == 1:

                # Likningssett: 2x + y - 3 og 8x - 2y + 12
                if _blokk == -1:

                    # [-1/2, 4]
                    losninger = superløs(variabel   = [x, y],
                                         likning     = [2 * x + y - 3, 8 * x - 2 * y + 12],
                                         rund        = -1,
                                         debug       = 1)

            # Flere likninger med flere løsninger (avrundet)
            if _blokk == 1:

                # Likningssett: 2x + y - 3 og 8x - 2y + 12
                if _blokk == -1:

                    # [-0.5, 4.0]
                    losninger = superløs(variabel   = [x, y],
                                         likning     = [2 * x + y - 3, 8 * x - 2 * y + 12],
                                         rund        = 2,
                                         debug       = 1)

    # Bruksansvisning
    if _blokk == 1:

        # - "Enkel avrunding" i Python kan oppleves overraskende krevende (kanskje tom.
        #   "buggy" eller "inkonsekvent"), hvis man ikke har trent en del på dette
        # - Og, med f.eks. numeriske løsninger i CAS (sympy) blir dette enda mer avansert
        # - Se derfor videoen om hvordan man bruker superløs på YouTube
        #   link eller bare søk opp "Matematikk AS", så blir isåfall alt dette
        #   super-enkelt, jeg ❤️!
        # - De viktigste punktene i videoen er
        #   - Du kan fint hacke på superløs(), men dennne funksjonen er laget
        #     - Slik at man skal kunne styre alt med input-argumentene (arg/args), uten
        #       å måtte hacke rundt inne i selve superløs()
        #     - For å dekke alle caser med likninger
        #   - Lær derfor å bruke de args som du trenger når du kaller/bruker superløs()
        #   - superløs() tar inn 5 args
        #     - variabel
        #       - Alle likninger løses med hensyn på (mhp.) "noe"
        #       - Dette "noe" er variabel-arg inn i superløs
        #       - Du må altså alltid presisere hva du løser likningen mhp. f.eks. x
        #       - Dette vil da f.eks. gi en løsning som er x = 2
        #       - Avhengig av hvordan du vil ha svaret ditt, så vil isåfall superløs()
        #         returnere selve verdien, 2
        #     - vs
        #       - Venstre side i likningen
        #     - hs
        #       - Høyre side i likningen
        #     - rund
        #       - Bestem hvor mange desimaler du vil ha i losningen din når du runder av
        #       - Default-avrundingen som alltid står der hvis man ikke selv endrer denne,
        #         er rund = -1
        #       - Default er altså ingen avrunding
        #        -
        # - Avrunding
        #   - Hvordan selve avrundingen fungerer er forklart i eksemplene under "Type 1.1.2 En løsning (avrundet)"
        #   - superløs() bruker Pythons innebygde round()-funksjon)
        # - Eksemplene
        #   - Hvis du vil sjekke et eksempel, bør du kun drille inn i blokken for dette eksempelet og
        #     endre _blokk = -1 til _blokk = 1
        #   - Når du er ferdig med å se på eksempelet, endrer du _blokk tilbake til _blokk = -1
        #   - På denne måten vises alltid kun det eksempelet du sjekker (mindre forvirrerende enn å se mange samtidig)
        pass
