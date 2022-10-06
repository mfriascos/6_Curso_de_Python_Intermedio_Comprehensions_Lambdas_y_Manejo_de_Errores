from .matrix import matrix


def four():
    words = []
    with open("./files_py/files_txt/programation.txt","r",encoding="utf-8") as f:
        for line in f:
            words.append(str(line))

    matrix(words,4)
