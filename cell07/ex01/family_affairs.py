def find_the_redheads(dic):
    result = []
    for k,v in dic.items():
        if v == "red":
            result.append(k)
    return result

dupont_family = {
    "florian": "red",
    "marie": "blond",
    "virginie": "brunette",
    "david": "red",
    "franck": "red"
}

print(find_the_redheads(dupont_family))