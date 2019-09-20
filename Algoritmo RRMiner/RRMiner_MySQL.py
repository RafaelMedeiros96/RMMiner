import glob
import nltk
from nltk.util import ngrams
import MySQLdb
import FiltroDados

db = MySQLdb.connect(host="localhost",    # seu host
                     user="root",    # seu user
                     passwd="",      # sua senha
                     db="tcc")      # nome do seu banco de dados
c = db.cursor()
cont=0


for i in glob.glob("Pasta do corpus"):

    raw=FiltroDados.filtro(i)
    print(i)

    token = nltk.word_tokenize(raw)

    #Solução para criação de novos NGRAM com mais de 3 palavras
    #bgs = ngrams(token, 1) #Word List
    #bgs = ngrams(token, 2)
    #bgs = ngrams(token, 3)
    bgs = ngrams(token, 4)


    #Computar a frequencia dos NGRAM e exibi o Token
    fdist = nltk.FreqDist(bgs)
    #print(fdist)
    #freq=0
    # Variavel "X" guarda a palavra, Variavel "Y" guarda a frequencia. Serão salvas no BD.

    #for x1, y2 in fdist.items():
        #freq=freq+y2

    for x,y in fdist.items():

        palavra=str(x).replace("'","").replace(")", "").replace("(", "").replace(",", "")

        #Salvar informações no BD
        c.execute("INSERT INTO termo (palavra, freq, conj)VALUES(%s,%s,%s)", (palavra,int(y),4))
        db.commit()

#Fecha o BD
db.close
print("*** FIM ***")
