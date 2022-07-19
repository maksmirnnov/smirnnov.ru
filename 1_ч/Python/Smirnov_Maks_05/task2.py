''' Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке. '''

with open('txts/text2.txt') as txt:
    line_count = 0
    for ind, line in enumerate(txt):
        line_text = line.split(' ')
        print(f'В строке № {ind + 1}: {len(line_text)} слов(о/а)')
        line_count = (ind + 1)
    print(f'всго строк: {line_count}')
