def famous_births(dic):
    births = [(v["date_of_birth"], v["name"]) for v in dic.values()]
    births.sort()
    for year, name in births:
        print(f"{name} is a great scientist born in {year}.")


women_scientists = {
    "ada": { "name": "Ada Lovelace", "date_of_birth": "1815" },
    "cecilia": { "name": "Cecila Payne", "date_of_birth": "1900" },
    "lise": { "name": "Lise Meitner", "date_of_birth": "1878" },
    "grace": { "name": "Grace Hopper", "date_of_birth": "1906" }
}

famous_births(women_scientists)