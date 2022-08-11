import os


def mkdir(path):
    if not os.path.exists(path):
        os.makedirs(path)


def fit_url(url: str):
    lurl = list(url)
    for i in range(len(lurl)):
        if lurl[i] == '/' or lurl[i] == ':':
            lurl[i] = '_'
    return "".join(lurl)


# store namelist at local/base_url(: and / become _)
def id_store(all_stud_id, base_url):
    folder = "local/" + fit_url(base_url)
    mkdir(folder)
    namelist = set()
    file_name = folder + "/namelist.txt"
    if os.path.isfile(file_name):  # load data
        fp = open(file_name, "r")
        names = fp.read().split("\n")
        if len(names):
            if (names[-1] == ""):
                names.pop()
        namelist = set(names)
        fp.close()
    namelist = namelist.union(map(str, all_stud_id))
    fp = open(file_name, "w")
    for line in namelist:
        fp.write(line+"\n")
    fp.close()
