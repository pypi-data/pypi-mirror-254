from __init__ import Pref, Datafil


##########################################
# Pref
##########################################

__   = Pref()
_  = Datafil()


##########################################
# Create
##########################################

_fil_navn_src = __._def_superlos_mas_src


##########################################
# Hotkeys
##########################################

# python /Users/krj/Desktop/program/src/_dir_1/bld/data_fil/_exe/python/funksjoner/matematikk/likninger/superlos/def_superlos_mas.py


##########################################
# Fil content
##########################################

_fil_content = f"""
{_._h_top_py}

{_._c_imp_from_sympy_import_ConditionSet_core_Eq_FiniteSet_Intersection_nsolve_Reals_solve_solveset_Symbol_C}

{_._f_superlos_def}
"""

"""
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
                    print(f"Løsningen til likningen er {{x}} = {{x_losning}}")
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
                    print(f"Løsningen til likningen er {{x}} = {{x_losning}}")
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
"""

"""
    # Tre raske eksempeler (en likning og ett likningssett)
    if _blokk == 1:

        # En likning, f.eks. 3x = 11
        if _blokk == -1:

            # 3.67
            x_losning = superløs(variabel   = x,
                                 vs          = 3*x,
                                 hs          = 11,
                                 rund        = -1,
                                 debug       = 1)

            print("")
            print(f"Løsningen til likningen er {{x}} = {{x_losning}}")
            print("")

        # Likningssett (linært), f.eks. 2x + y = 3 og 8x - 2y = -12
        if _blokk == -1:

            # Likningssett steg-for-steg (3 enkle steg)
            # 1. Likningssettet må først ordnes (ha 0 på hs i begge likningene)
            #      8x - 2y = -12     ->  8x - 2y + 12 = 0
            #      2x +  y =  3      ->  2x +  y - 3  = 0
            # 2. Deretter legges begge likningene i en liste, adskilt med komma
            #    [8 * x - 2 * y + 12, 2 * x + y - 3]
            # 3. Det samme gjøres med variablene
            #    [x, y]

            # x^2 +2x + 2
            # -x^2+4x + 1
            losninger = superløs(variabel   = [x, y],
                                 likning     = [8 * x - 2 * y + 12, 2 * x + y - 3],
                                 rund        = 2,
                                 debug       = 1)

            print("")
            print(f"Løsningen til likningssettet er {{x}} = {{losninger[0]}} og {{y}} = {{losninger[1]}}")
            print("")

        # Likningssett (ikke-linært), f.eks. x^2 + 2x + 2 og -x^2 - 4x + 1
        if _blokk == -1:

            # Likningssett steg-for-steg (3 enkle steg)
            # 1. Legg alle variablene i en liste
            #    variabel = [x, y]
            # 2. Deretter må likningssettet være ordnet (0 på høyre side i begge likningene)
            #      I    y =  x**2 + 2*x + 2  ->   y - x**2 - 2 * x - 2  = 0
            #      II   y = -x**2 - 4*x + 1  ->   y + x**2 + 4 * x - 1  = 0
            # 3  Legg alle likningene i en liste (husk Python-notasjon), adskilt med komma
            #    likning = [y - x**2 - 2 * x - 2, - 2, y + x**2 + 4 * x - 1]

            losninger = superløs(variabel   = [x, y],
                                 likning   = [y - x**2 - 2 * x - 2, y + x**2 + 4*x - 1],
                                 rund        = 2,
                                 debug       = 1)

            print("")
            print(f"Løsningen er ({{losninger[0][0]}}, {{losninger[0][1]}}) og ({{losninger[1][0]}}, {{losninger[1][1]}})")
            print("")
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