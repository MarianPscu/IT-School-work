rezultate_campionat = [
    {"echipa": "CFR Cluj", "meciuri_jucate": 36, "victorii": 22, "egaluri": 9, "infrangeri": 5},
    {"echipa": "FCSB", "meciuri_jucate": 36, "victorii": 21, "egaluri": 7, "infrangeri": 8},
    {"echipa": "Universitatea Craiova", "meciuri_jucate": 36, "victorii": 18, "egaluri": 11, "infrangeri": 7},
    {"echipa": "Sepsi Sfântu Gheorghe", "meciuri_jucate": 36, "victorii": 15, "egaluri": 11, "infrangeri": 10},
    {"echipa": "Astra Giurgiu", "meciuri_jucate": 36, "victorii": 14, "egaluri": 11, "infrangeri": 11},
    {"echipa": "CS Mioveni", "meciuri_jucate": 36, "victorii": 13, "egaluri": 12, "infrangeri": 11},
    {"echipa": "FC Argeș Pitești", "meciuri_jucate": 36, "victorii": 13, "egaluri": 9, "infrangeri": 14},
    {"echipa": "FC Botoșani", "meciuri_jucate": 36, "victorii": 12, "egaluri": 10, "infrangeri": 14},
    {"echipa": "Gaz Metan Mediaș", "meciuri_jucate": 36, "victorii": 11, "egaluri": 12, "infrangeri": 13},
    {"echipa": "FC Voluntari", "meciuri_jucate": 36, "victorii": 12, "egaluri": 8, "infrangeri": 16},
    {"echipa": "Academica Clinceni", "meciuri_jucate": 36, "victorii": 10, "egaluri": 12, "infrangeri": 14},
    {"echipa": "FC Hermannstadt", "meciuri_jucate": 36, "victorii": 10, "egaluri": 11, "infrangeri": 15}
]

list_totals = []
list_draws = []

for team in rezultate_campionat:
    totalitate = (team["victorii"] * 3) + (team["egaluri"] * 1)
    list_totals.append(totalitate)
    list_draws.append(team["egaluri"])
    team.update(({"puncte": totalitate}))

#Campioana

for team in rezultate_campionat:
    if max(list_totals) == team["puncte"]:
        print(team["echipa"])

#Lider pe egaluri

for team in rezultate_campionat:
    if max(list_draws) == team["egaluri"]:
        print(team["echipa"])

#Podium
sorted_points = sorted(rezultate_campionat, key = lambda x: x["puncte"], reverse= True)

pointer = 0

for team in sorted_points:
    
        print(team["echipa"], team["puncte"])
        pointer += 1
        if pointer == 3:
             break
        
        


