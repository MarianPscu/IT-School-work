auto = {
    "marca": "Audi",
    "model": "A4",
    "usi": 4
}


OWNERSHIP_TEMPLATE = "Detin o masina marca {}, model {} si are {} usi"


print(OWNERSHIP_TEMPLATE.format(auto["marca"], auto["model"], auto["usi"]))