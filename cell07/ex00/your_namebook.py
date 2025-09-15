def array_of_names(dic):
    result = []
    for k, v in dic.items():
        result.append(f"{k[0].upper()}{k[1:]} {v[0].upper()}{v[1:]}")
    return(result)
    
persons = {
    "jean": "valjean",
    "grace": "hopper",
    "xavier": "niel",
    "fifi": "brindacier"
}

print(array_of_names(persons))