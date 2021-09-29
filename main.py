import sys

def compara_palavra(subtring_a , subtring_b):
    menor_tamanho = min(len(subtring_a),len(subtring_b))
    for i in range(0,menor_tamanho):
        if((subtring_a[i] != subtring_b[i])):
            return subtring_a[0:i]
    else:
        return subtring_a[0:menor_tamanho]


def verifica_final_duplicado(entrada):
    entrada_split = entrada.split(" ")
    lista_finais_duplicados = []

    for palavra in entrada_split:
        maior_substring = ""
        tamanho_palavra = len(palavra)
        for i in range(0,tamanho_palavra):
            for j in range(i+1, tamanho_palavra):
                return_compara_palavra = compara_palavra(palavra[i:tamanho_palavra],palavra[j:tamanho_palavra])    

                if(len(return_compara_palavra) > len(maior_substring)):
                    palavra_temp = palavra[i:tamanho_palavra].replace(return_compara_palavra,"",1)
                    if(return_compara_palavra in palavra_temp):
                        maior_substring = return_compara_palavra
        lista_finais_duplicados.append(maior_substring)
                    
    return lista_finais_duplicados

def remove_duplicacao(entrada,lista_finais_duplicados):
    entrada_split = entrada.split(" ")
    entrada_sem_duplicacao = ''
    for i in range(0,len(entrada_split)):
        if(lista_finais_duplicados[i] == ''):
            entrada_sem_duplicacao = entrada + "."
            break

        entrada_sem_duplicacao = entrada_sem_duplicacao + entrada_split[i].replace(lista_finais_duplicados[i],"",1)
        if(i < len(entrada_split)-1):
            entrada_sem_duplicacao = entrada_sem_duplicacao + " "
        else:
            entrada_sem_duplicacao = entrada_sem_duplicacao + "."

    return entrada_sem_duplicacao



def main():

    # entrada = "oo ratoato roeuoeu aa roupaoupa dodo reiei dee romaoma"
    # entrada = "a bananeira tem banana"
    # entrada = "banana"

    entrada = input()

    lista_finais_duplicados = verifica_final_duplicado(entrada)
    entrada_sem_duplicacao = remove_duplicacao(entrada,lista_finais_duplicados)
    print(entrada_sem_duplicacao)


    


main()




