import json
from unidecode import unidecode


def get_bd():
    with open("bd_musics") as bd_musics:
        musics = bd_musics.read()

    print(len(musics))
    if(len(musics)) < 0:
        print('banco de musicas sem informação')
        return -1
    else:
        return musics

def trata_bd(bd):
    temp = ''
    bd_list = []
    check = 0
    bd_lower_case = bd.lower()

    for music in bd:
        if music == '"':
            check += 1
        elif music == '"':
            check -= 1
        if music == ', ' and check == 0:
            if bd.strip():
                bd_list.append(unidecode(temp))
            temp = ''
        else:
                temp += music

    if temp.strip():
            bd_list.append(unidecode(temp))



    return bd_list_clean

def search_music(search_input, bd_music):
    index = 0
    score = 0
    search_input_split = search_input.split(" ")
    for bd_music_item in bd_music:
        bd_music_item_split_word = bd_music_item.split(" ")
        score = 0
        for word_split in bd_music_item_split_word:
            for search_word in search_input_split:
                if(bd_music_item == search_word):
                    score += 10
                menor_tamanho_string = min(len(bd_music_item),len(search_word))
                for i in range(0,menor_tamanho_string):
                    if(bd_music_item[i] == search_word[i]):
                        score+=1






        for sea

def main():

    musics = get_bd()
    musics_list_clean = trata_bd(musics)

    input_search = input('Digite sua busca:' )






main()