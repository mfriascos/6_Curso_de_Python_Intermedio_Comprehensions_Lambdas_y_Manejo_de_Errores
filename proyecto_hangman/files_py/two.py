from .matrix import matrix


def two():
    words = []
    with open("./files_py/files_txt/english_verbs.txt","r",encoding="utf-8") as f:
        for line in f:
            words.append(str(line))

    matrix(words,2)
