def read_csv(path, limit=100, sep=","):
    datalist = []
    n = 1
    with open(path) as file:
        for line in file:
            if n > limit:
                break
            datalist.append(line.split("\n")[0].split(sep))
            n += 1
    return datalist
