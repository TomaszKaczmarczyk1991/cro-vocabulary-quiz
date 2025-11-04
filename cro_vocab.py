import random

words = {
    # PODSTAWOWE SŁOWA & ZWROTY
    "da": "tak","ne": "nie","možda": "może","dobro": "dobrze","loše": "źle","molim": "proszę","hvala": "dziękuję",
    "izvoli": "proszę (podając)","oprosti": "przepraszam","oprostite": "przepraszam",
    "bok": "cześć","zdravo": "witaj","dobar dan": "dzień dobry","dobro jutro": "dzień dobry (rano)",
    "dobra večer": "dobry wieczór","laku noć": "dobranoc","kako si?": "jak się masz?","dobro sam": "mam się dobrze",
    "razumijem": "rozumiem","ne razumijem": "nie rozumiem","daj mi": "daj mi","mogu": "mogę","ne mogu": "nie mogę",
    "želim": "chcę","ne želim": "nie chcę","znam": "wiem / umiem","ne znam": "nie wiem","gdje": "gdzie",
    "kada": "kiedy","što": "co","tko": "kto","zašto": "dlaczego","kako": "jak","koliko": "ile","stvarno": "naprawdę",
    "naravno": "oczywiście","polako": "spokojnie / powoli","žao mi je": "przykro mi","volim te": "kocham cię",
    "sada": "teraz","kasnije": "później","uvijek": "zawsze","nikad": "nigdy","još": "jeszcze","dosta": "dość",
    "gotovo": "gotowe","odmah": "natychmiast","možda": "może","super": "super","fantastično": "fantastycznie",
    "tako": "tak","tamo": "tam","ovdje": "tutaj","opet": "znowu","bravo": "brawo",

    # ZAIMKI I LUDZIE
    "ja": "ja","ti": "ty","on": "on","ona": "ona","ono": "ono","mi": "my","vi": "wy","oni": "oni / one",
    "netko": "ktoś","nitko": "nikt","čovjek": "człowiek","osoba": "osoba","prijatelj": "przyjaciel",
    "prijateljica": "przyjaciółka","brat": "brat","sestra": "siostra","majka": "matka","otac": "ojciec",
    "dijete": "dziecko","žena": "kobieta","muškarac": "mężczyzna","djevojka": "dziewczyna","dečko": "chłopak",
    "obitelj": "rodzina","kolega": "kolega","kolegice": "koleżanka","liječnik": "lekarz","radnik": "pracownik",
    "šef": "szef","gost": "gość","susjed": "sąsiad","turist": "turysta","moj": "mój","tvoj": "twój",
    "njegov": "jego","njezin": "jej","naš": "nasz","vaš": "wasz","njihov": "ich","ja sam": "jestem",
    "ti si": "jesteś","on je": "on jest","ona je": "ona jest","mi smo": "my jesteśmy","vi ste": "wy jesteście",
    "oni su": "oni są",

    # DOM
    "kuća": "dom","stan": "mieszkanie","soba": "pokój","kuhinja": "kuchnia","kupaonica": "łazienka",
    "dnevna soba": "salon","hodnik": "korytarz","balkon": "balkon","vrt": "ogród","zgrada": "budynek",
    "vrata": "drzwi","prozor": "okno","krevet": "łóżko","stol": "stół","stolica": "krzesło","ormar": "szafa",
    "lampa": "lampa","televizor": "telewizor","hladnjak": "lodówka","štednjak": "kuchenka","peć": "piekarnik",
    "tuš": "prysznic","kada": "wanna","tepih": "dywan","pod": "podłoga","zid": "ściana","ključ": "klucz",
    "čaša": "szklanka","šalica": "kubek","vilica": "widelec","nož": "nóż","žlica": "łyżka","tanjuŕ": "talerz",
    "polica": "półka","frižider": "lodówka","mikrovalna": "mikrofalówka","perilica": "pralka",
    "sušilica": "suszarka","ručnik": "ręcznik","jorgan": "kołdra","jastuk": "poduszka","plahte": "pościel",

    # JEDZENIE
    "hrana": "jedzenie","voda": "woda","kruh": "chleb","mlijeko": "mleko","kava": "kawa","čaj": "herbata",
    "vino": "wino","pivo": "piwo","meso": "mięso","riba": "ryba","juha": "zupa","salata": "sałatka",
    "povrće": "warzywa","voće": "owoce","šećer": "cukier","sol": "sól","papar": "pieprz","ulje": "olej",
    "sir": "ser","jaje": "jajko","riža": "ryż","tjestenina": "makaron","kolač": "ciasto","sladoled": "lody",
    "sendvič": "kanapka","pizza": "pizza","juha": "zupa","čokolada": "czekolada","keks": "ciastko",
    "med": "miód","brašno": "mąka","pile": "kurczak","govedina": "wołowina","svinjetina": "wieprzowina",
    "krumpir": "ziemniak","mrkva": "marchew","jabuka": "jabłko","banana": "banan","naranča": "pomarańcza",
    "limun": "cytryna","lubenica": "arbuz","grožđe": "winogrona","krastavac": "ogórek",

    # NAPOJE
    "sok": "sok","voda gazirana": "woda gazowana","voda negazirana": "woda niegazowana","rakija": "rakija",
    "čaj": "herbata","kava s mlijekom": "kawa z mlekiem","mlijeko": "mleko",

    # PRZYRODA
    "more": "morze","plaža": "plaża","sunce": "słońce","vrijeme": "pogoda","kiša": "deszcz","snijeg": "śnieg",
    "vjetar": "wiatr","drvo": "drzewo","cvijet": "kwiat","rijeka": "rzeka","jezero": "jezioro",
    "planina": "góra","otok": "wyspa","kamen": "kamień","pijesak": "piasek","šuma": "las",

    # MIASTO
    "grad": "miasto","ulica": "ulica","trg": "plac","park": "park","muzej": "muzeum","trgovina": "sklep",
    "restoran": "restauracja","kafić": "kawiarnia","hotel": "hotel","bolnica": "szpital","luka": "port",
    "stanica": "stacja","autobus": "autobus","vlak": "pociąg","zračna luka": "lotnisko","taksi": "taksówka",
    "auto": "auto","bicikl": "rower","vlak": "pociąg","mobilni": "telefon","računalo": "komputer",

    # CZAS
    "jutro": "rano","poslijepodne": "popołudnie","večer": "wieczór","noć": "noc","dan": "dzień",
    "tjedan": "tydzień","mjesec": "miesiąc","godina": "rok","sat": "godzina","minuta": "minuta",
    "sekunda": "sekunda","danas": "dzisiaj","sutra": "jutro","jučer": "wczoraj","prije": "wcześniej",
    "poslije": "później","brzo": "szybko","sporo": "wolno",

    # CZASOWNIKI PODSTAWOWE (ok. 100)
    "biti": "być","imati": "mieć","ići": "iść","doći": "przyjść","vidjeti": "widzieć","čuti": "słyszeć",
    "govoriti": "mówić","pisati": "pisać","čitati": "czytać","raditi": "pracować","učiti": "uczyć się",
    "jesti": "jeść","piti": "pić","spavati": "spać","gledati": "oglądać","čekati": "czekać",
    "voziti": "prowadzić","hodati": "chodzić","trčati": "biegać","plivati": "pływać","kupiti": "kupić",
    "prodati": "sprzedać","voljeti": "kochać","pomagati": "pomagać","zvati": "dzwonić","slati": "wysyłać",
    "otvoriti": "otworzyć","zatvoriti": "zamknąć","misliti": "myśleć","znati": "wiedzieć","sjetiti se": "pamiętać",
    "zaboraviti": "zapomnieć","početi": "zacząć","završiti": "skończyć","tražiti": "szukać",
    "pronaći": "znaleźć","uzeti": "wziąć","dati": "dać","donijeti": "przynieść","pitati": "pytać",
    "odgovoriti": "odpowiedzieć","voziti": "jeździć","šutjeti": "milczeć","smijati se": "śmiać się",
    "plakati": "płakać",

    # PRZYMIOTNIKI (ok. 80)
    "dobar": "dobry","loš": "zły","lijep": "ładny","ruzan": "brzydki","velik": "duży","mali": "mały",
    "nov": "nowy","star": "stary","topao": "ciepły","hladan": "zimny","brz": "szybki","spor": "wolny",
    "lak": "łatwy","težak": "trudny","jeftin": "tani","skup": "drogi","sretan": "szczęśliwy",
    "tužan": "smutny","umoran": "zmęczony","gladan": "głodny","žedan": "spragniony","čist": "czysty",
    "prljav": "brudny","kratak": "krótki","dug": "długi","visok": "wysoki","nizak": "niski",
    "pametan": "mądry","glup": "głupi",

    # LICZBY
    "jedan": "jeden","dva": "dwa","tri": "trzy","četiri": "cztery","pet": "pięć","šest": "sześć",
    "sedam": "siedem","osam": "osiem","devet": "dziewięć","deset": "dziesięć","sto": "sto","tisuću": "tysiąc",

    # KOLORY
    "crvena": "czerwony","plava": "niebieski","zelena": "zielony","žuta": "żółty","crna": "czarny",
    "bijela": "biały","siva": "szary","smeđa": "brązowy","narančasta": "pomarańczowy","roza": "różowy",

    # EMOCJE
    "sretan": "szczęśliwy","tužan": "smutny","ljut": "zły","uplašen": "przestraszony","zabrinut": "zatroskany",
    "opušten": "zrelaksowany","uzbuđen": "podekscytowany","dosadno mi je": "nudzę się",

    # CIAŁO
    "glava": "głowa","oko": "oko","uho": "ucho","nos": "nos","usta": "usta","zub": "ząb","ruka": "ręka",
    "noga": "noga","srce": "serce","trbuh": "brzuch","leđa": "plecy","prsa": "klatka piersiowa",

    # PODSTAWY GRAMATYCZNE
    "i": "i","ali": "ale","ili": "albo","jer": "bo","da bi": "żeby","bez": "bez","sa": "z",
    "za": "dla / za","od": "od","do": "do","prema": "według","kroz": "przez","oko": "około","na": "na",
    "u": "w","iz": "z (skąd)",

    # TECHNOLOGIA
    "računalo": "komputer","tipkovnica": "klawiatura","miš": "mysz","internet": "internet",
    "aplikacija": "aplikacja","lozinka": "hasło","račun": "konto","wifi": "wifi","ekran": "ekran",
    "slika": "zdjęcie","kamera": "kamera",

    # INSTRUMENTY MUZYCZNE
    "gitara": "gitara","klavir": "fortepian/pianino","violina": "skrzypce","flauta": "flet",
    "truba": "trąbka","saksofon": "saksofon","bubnjevi": "perkusja/bębny","harmonika": "akordeon",
    "ukulele": "ukulele","trombon": "puzon","klarinet": "klarnet","harfa": "harfa","mandolina": "mandolina",
    "tamburica": "tamburica","orgulje": "organy","bas gitara": "gitara basowa","čelo": "wiolonczela",
    "kontrabas": "kontrabas","sintisajzer": "syntezator","električna gitara": "gitara elektryczna",
    "MIDI kontroler": "kontroler MIDI","kalimba": "kalimba",

    # ZDROWIE
    "doktor": "doktor","tableta": "tabletka","čaj": "herbata","bol": "ból","glavobolja": "ból głowy",
    "prehlada": "przeziębienie","kašalj": "kaszel","temperatura": "gorączka",

    # MIEJSCA
    "škola": "szkoła","učionica": "klasa","knjižnica": "biblioteka","kazalište": "teatr","kino": "kino",
    "tržnica": "targ","stanica": "przystanek","crkva": "kościół","plaža": "plaża","more": "morze",

    # RESZTA SŁÓW
    "pravilo": "zasada","primjer": "przykład","poruka": "wiadomość","pitanje": "pytanie","odgovor": "odpowiedź",
    "razlog": "powód","riječ": "słowo","rečenica": "zdanie","tekst": "tekst","priča": "historia",
    "muzika": "muzyka","pjesma": "piosenka","jezik": "język","lekcija": "lekcja","znanje": "wiedza",
    "vježba": "ćwiczenie","posao": "praca","novac": "pieniądze","račun": "rachunek","karta": "bilet",
    "ulaz": "wejście","izlaz": "wyjście","zahod": "toaleta","pomoć": "pomoc","opasno": "niebezpieczne",
    "sigurno": "bezpieczne","pravac": "kierunek","desno": "prawo","lijevo": "lewo","ravno": "prosto",
    "blizu": "blisko","daleko": "daleko","unutra": "w środku","vani": "na zewnątrz","gore": "góra",
    "dolje": "dół","preko": "przez","oko": "około","brzo": "szybko","sporo": "wolno"
}

import random
import unicodedata

def normalize(text):
    return ''.join(
        c for c in unicodedata.normalize('NFD', text.lower())
        if unicodedata.category(c) != 'Mn'
    ).strip()

while True:
    word = random.choice(list(words.keys()))
    correct = words[word]

    answer = input(f"Znaczenie słowa '{word}': ")

    if normalize(answer) == normalize(correct):
        print("✅ Dobrze!\n")
    else:
        print(f"❌ Źle! Poprawna odpowiedź: {correct}\n")