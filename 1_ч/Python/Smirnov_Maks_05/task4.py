''' Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные. При этом английские
числительные должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл. '''

def translater():
    with open('txts/text4-1.txt') as txt:
        for line in txt:
            string = line.split(" ")[1:]
            if line.split(' ')[0] == 'One':
                with open('txts/text4-2.txt', 'w') as ru_txt:
                    ru_txt.write(' '.join(['Один ', *string]))
            elif line.split(' ')[0] == 'Two':
                with open('txts/text4-2.txt', 'a') as ru_txt:
                    ru_txt.write(' '.join(['Два ', *string]))
            elif line.split(' ')[0] == 'Three':
                with open('txts/text4-2.txt', 'a') as ru_txt:
                    ru_txt.write(' '.join(['Три ', *string]))
            elif line.split(' ')[0] == 'Four':
                with open('txts/text4-2.txt', 'a') as ru_txt:
                    ru_txt.write(' '.join(['Четыре ', *string]))
translater()
