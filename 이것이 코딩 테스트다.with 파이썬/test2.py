import re


def solution(new_id):
    new_id = new_id.lower()
    new_id = re.sub("[^a-z0-9_.-]", "", new_id)
    new_id = list(new_id)
    for i in range(len(new_id)-1):
        if new_id[i] == '.' and new_id[i+1] == '.':
                new_id[i] = ""
    new_id = "".join(map(str, new_id))
    new_id = list(new_id)
    if new_id[0] == ".":
        new_id[0] = ""
    if new_id[-1] == ".":
        new_id[-1] = ""
    new_id = "".join(map(str, new_id))
    if not new_id:
        new_id = 'a'
    if len(new_id) >= 16:
        new_id = list(new_id)
        del new_id[15:]
        if new_id[-1] == ".":
            new_id[-1] = ""
        new_id = "".join(map(str, new_id))
    elif len(new_id) <= 2:
        new_id = list(new_id)
        while True:
            new_id.append(new_id[-1])
            if len(new_id) == 3:
                break
        new_id = "".join(map(str, new_id))

    return new_id
