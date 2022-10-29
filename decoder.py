import os

# function to return key for any value
def get_key(val):
    for key, value in my_dict.items():
        if val == value:
            return key
 
    return "key doesn't exist"

def decode(word):
    lista = ""
    for i in range(len(word)):
        if word[i] == ".":
            lista = lista + "1"
        elif word[i] == '-':
            lista = lista +"0"

    return get_key(lista)

my_dict = {"T":"0","M":"00","O":"000","-":"0000","0":"00000","E":"1","I":"11"
           ,"S":"111","H":"1111","5":"11111","K":"010","Y":"0100","C":"0101"
           ,"D":"011","X":"0110","B":"0111","6":"01111","A":"10","W":"100"
           ,"J":"1000","P":"1001","1":"10000","R":"101","L":"1011","U":"110","F":"1101"
           ,"V":"1110","2":"11000","3":"11100","4":"11110","7":"00111"
           ,"G":"001","Q":"0010","Z":"0011","9":"00001","N":"01",
           "?":"110011",".":"10101"," ":"1111111",".":"101010"}
palavras = []
cod_bin = []
frase = ""
with open('morse.txt') as f:
    linhas = f.readlines()
    print(linhas)
for i in range(len(linhas)):
    palavras.append(linhas[i].split())
for j in range(len(palavras)):
    for k in range(len(palavras[j])):
        frase = frase + decode(palavras[j][k])
print(frase)
with open('Decoded.txt','x') as decoded:
    decoded.write(frase)
    
    
