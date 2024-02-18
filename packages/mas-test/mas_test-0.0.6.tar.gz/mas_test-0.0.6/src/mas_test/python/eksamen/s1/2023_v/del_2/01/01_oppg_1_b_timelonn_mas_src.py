# 🚀 programmering.no | 🤓 matematikk.as
# S1 - Eksamen - 2023 Vår (Matematikk AS)
# Oppgave 2 b) Timelønnen til yrkesgruppe" - Eksponentialfunksjon (regresjon) 
# - Løser oppgaven med CAS i Python
# - Prosentvis vekst er en eksponentialfunksjon som f.eks. kan skrives på formenene
#   - f(x) = a * b^x, b > 0, b: vekstfaktor, f(0) = a
#   - g(x) = g_0 * V^x, V = 1 ± p / 100, g: Timelønn, g_0: Startverdi, V: Vekstfaktor, x: perioder

from sympy import ConditionSet, core, diff, Eq, FiniteSet, Intersection, limit, nsolve, oo, Reals, solve, solveset, Symbol

# Konstanter og CAS-variabler (symbol)
_blokk             = 1                 # 0: Av, 1: På, Skjul/debug deler av koden med if-blokker
G                  = Symbol("G")       # Timelonn x år etter 2008
G_0                = Symbol("G_0")     # Timelønnen i 2008-2022, [kr]
G_liste            = [                 # Timelønnen (tabell), [kr]
    272.55,
    285.50,
    307.30,
    314.00,
    327.60,
    340.10]
V                  = Symbol("V")       # Vekstfaktor
x                  = Symbol("x")       # Antall år med lønnsvekst
x_liste            = [                 # Perioden 2008-2022, [år]
    2008,
    2010,
    2013,
    2015,
    2019,
    2022
]
p                  = Symbol("p")       # Årlig vekst i prosent, [%]

# Definerer funksjoner
def vekstfaktor(p, fortegn):

    # Vekstfaktor er definert som V = 1 ± p / 100
    if fortegn == "+": return 1 + p / 100 # "+": Øker, "-": Minker
    if fortegn == "-": return 1 - p / 100 # p: Vekst [%]

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
            losning_element = losning_set_sub.args; losning_set = [];
            for el in losning_element: losning_set.append(el); rund = -1
            if len(losning_set) == 1: los_ant = "en løsning som er et uttrykk"
            if len(losning_set) > 1: los_ant = str(len(losning_set)) + " " + "løsninger som er uttrykk"

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

# a) Gjennomsnittlig årlig prosentvekst
if _blokk == 1:

    # Definerer uttrykket for vekstfaktoren, V = 1 + p / 100
    V = vekstfaktor(p, "+")

    # Definerer uttrykket for årlig gjennomsnittlig vekst, f(x) = a * b^x
    G = G_0 * V**x

    # Regner ut antall år for perioden 2008–2022 
    x_periode = x_liste[-1] - x_liste[0]

    # Setter x = x_periode inn i G og definerer det nye uttrykket som G_periode 
    G_periode = G.subs(x, x_periode)

    # Setter G_0 = G_liste[0] inn i G_periode og oppdaterer uttrykket
    G_periode = G_periode.subs(G_0, G_liste[0])

    # Regner ut p = 1.6
    p_periode = superløs(variabel = p,
                         vs       = G_periode,
                         hs       = G_liste[-1],
                         rund     = 1,
                         debug    = -1)[1]

    svar_a_liste = list()
    svar_a_liste.append(f"")
    svar_a_liste.append(f"Oppg c)")
    svar_a_liste.append(f"")
    svar_a_liste.append(f"- I årene 2008-2022 var den gjennomsnittlige årlige")
    svar_a_liste.append(f"  prosentvise veksten ca. {p_periode} %")

    # Print svar-setninger
    for svar in svar_a_liste: print(svar)
