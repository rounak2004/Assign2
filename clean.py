def writing_contents_to_newfile():
    w = []
    words = []
    file = open("word5Dict.txt","r")
    f = file.read()
    w.append(f)
    for i in w:
        replace_contents = i.replace("#"," ")
        splitting_lines = replace_contents.split()
        for j in splitting_lines:
            words.append(j)
    file = open("scrabble5.txt","w")
    for i in words:
        file.write(i+'\n')
    file.close()
writing_contents_to_newfile()    