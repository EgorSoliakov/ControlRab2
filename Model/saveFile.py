import Model.Note as Note

def saveFile(array, mode):
    file = open("note.txt", mode = 'w', encoding='utf-8')
    file.seek(0)
    file.close()
    file = open("note.txt", mode=mode, encoding='utf-8')
    for notes in array:
        file.write(Note.Note.to_string(notes))
        file.write('\n')
    file.close    

