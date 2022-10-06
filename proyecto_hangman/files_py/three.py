from .matrix import matrix


def three():
    words = []
    with open("./files_py/files_txt/spanish_verbs.txt","r",encoding="utf-8") as f:
        for line in f:
            words.append(str(line))

    matrix(words,3)
