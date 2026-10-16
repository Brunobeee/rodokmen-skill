#!/usr/bin/env python3
"""Hledání svazků na portálu ARON (SOA Zámrsk, fond Sbírka matrik Východočeského kraje).
Použití: aron_search.py "<text v popisu, např. obec>" [filtr názvu fondu] [max]
Vypíše: apu_id | signatura, druh a roky | popis (obce, které svazek pokrývá)."""
import json, sys, urllib.request

API = "https://aron.vychodoceskearchivy.cz/api/aron"

def post(path, body):
    req = urllib.request.Request(API + path, data=json.dumps(body).encode(),
                                 headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=90) as r:
        return json.load(r)

def search(desc, name="Sbírka matrik Východočeského kraje", maxn=500):
    out, offset = [], 0
    while True:
        d = post("/apu/listview?listType=SEARCH", {
            "filters": [{"field": "type", "operation": "EQ", "value": "ARCH_DESC"},
                        {"operation": "FTXF", "field": "name", "value": name},
                        {"operation": "FTXF", "field": "description", "value": desc}],
            "sort": [], "offset": offset, "size": 100, "aggregations": []})
        items = d.get("items", [])
        out += items
        offset += len(items)
        if not items or offset >= min(d.get("count", 0), maxn):
            return out, d.get("count")

if __name__ == "__main__":
    desc = sys.argv[1]
    name = sys.argv[2] if len(sys.argv) > 2 and sys.argv[2] else "Sbírka matrik Východočeského kraje"
    maxn = int(sys.argv[3]) if len(sys.argv) > 3 else 500
    items, cnt = search(desc, name, maxn)
    print("count", cnt)
    for i in items:
        n = i["name"].split(": ", 1)[-1]
        print(i["id"], "|", n.replace("Sbírka matrik Východočeského kraje, ", ""), "|", (i.get("description") or "")[:220])
