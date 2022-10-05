import unicodedata

def one():
    words = []
    with open("./files_py/files_txt/data.txt","r",encoding="utf-8") as f:
        for line in f:
            trans_tab = dict.fromkeys(map(ord, u'\u0301\u0308'), None)
            line = unicodedata.normalize('NFKC', unicodedata.normalize('NFKD', str(line)).translate(trans_tab))
            words.append(str(line))

    
        
