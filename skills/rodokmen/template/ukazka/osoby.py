# UKÁZKOVÁ DATA – vymyšlená rodina Novákových. Slouží jen k vyzkoušení webu; formát viz template/data/osoby.py.
P = {
 1: dict(n="Petr Novák", y="* 1980", st="fam", sex="M", f=["* 1980 Pardubice"], note="Žijící – údaje jen základní."),
 2: dict(n="Josef Novák", y="* 1952", st="fam", f=["* 1952"], note="Žijící – údaje jen základní."),
 3: dict(n="Eva Dvořáková", y="* 1955", st="fam", f=["provd. Nováková"], note="Žijící – údaje jen základní."),
 4: dict(n="František Novák", y="1921–1990", st="fam", f=["* 3. 5. 1921 Holice", "zámečník", "× 1948 Marie Králová", "† 1990 Pardubice"]),
 5: dict(n="Marie Králová", y="1925–2011", st="fam", f=["* 1925 Holice", "švadlena"]),
 6: dict(n="Karel Dvořák", y="1927–1999", st="fam", f=["* 1927 Chrudim", "železničář"]),
 7: dict(n="Anna Šimková", y="1930–2015", st="fam", f=["* 1930 Chrudim"]),
 8: dict(n="Jan Novák", y="1890–1944", st="doc", f=["* 14. 2. 1890 Holice čp. 112", "kovář v Holicích", "× 20. 6. 1919 Holice Josefa Pokorná", "† 1944 Holice"],
         r=["ukazka_krest_jan_novak_1890", "ukazka_snatek_jan_novak_josefa_pokorna_1919"]),
 9: dict(n="Josefa Pokorná", y="* 1895", st="doc", f=["* 1895 Dolní Roveň čp. 7", "× 20. 6. 1919 Holice Jan Novák"], r=["ukazka_snatek_jan_novak_josefa_pokorna_1919"]),
 10: dict(n="Václav Král", y="asi 1893 – ?", st="prob", f=["rolník v Holicích"], note="Jen ze zápisu sňatku dcery; vlastní křest zatím nenalezen."),
 12: dict(n="Antonín Dvořák", y="* 1899", st="mh", f=["* 1899 Chrudim"], note="Jen z cizího rodokmenu na internetu – neověřeno."),
 16: dict(n="Václav Novák", y="1858–1921", st="doc", f=["* 1858 Holice čp. 112", "kovář", "× 1884 Holice Barbora Malá", "† 1921 Holice"], r=["ukazka_krest_jan_novak_1890"]),
 17: dict(n="Barbora Malá", y="1862–1930", st="doc", f=["* 1862 Ostřetín čp. 23"], r=["ukazka_krest_jan_novak_1890"]),
 18: dict(n="Josef Pokorný", y="* 1865", st="doc", f=["sedlák v Dolní Rovni čp. 7"], r=["ukazka_snatek_jan_novak_josefa_pokorna_1919"]),
 32: dict(n="Jan Novák", y="asi 1825–1880", st="prob", f=["kovář v Holicích čp. 112"], note="Pravděpodobný otec Václava – stejný dům a řemeslo, křest zatím nenalezen."),
}

LINES = {
 8: ("Novákové", "Kováři z Holic, čtyři generace v domě čp. 112."),
 9: ("Pokorní", "Sedláci z Dolní Rovně."),
 10: ("Králové", "Rolníci z Holic."),
 12: ("Dvořákové", "Železničáři z Chrudimi."),
}

SIDE = [
 dict(k=8, n="Marie Nováková (1892–1970)", t="Sestra Jana, provdaná do Ostřetína.", r=[]),
]

ISSUES = [
 ("Odkud přišli Novákové do Holic?", "Otevřené: první doložený je kovář Jan (asi 1825); starší holické matriky jsme zatím neprošli."),
 ("Kdo byl otec Václava Krále?", "Hypotéza: rolník z Ostřetína – shoda jména a doby, zatím bez zápisu."),
]

HYPOTEZY = [
 dict(rod=8, nadpis="Hypotéza: Novákové z Ostřetína", text="Ve vedlejším Ostřetíně žili kováři Novákové už kolem roku 1780. Vazba na holické Nováky zatím chybí.",
      polozky=[("Matěj Novák", "kovář v Ostřetíně, kmotr 1781")], zaznamy=[]),
]

SAME = {}
