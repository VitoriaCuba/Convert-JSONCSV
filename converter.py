import os
import csv
import json
from collections import OrderedDict

print ( "Bem-vindo ao Conversor JSON-CSV." )
print ( "Este script converterá um arquivo JSON para CSV ou um arquivo CSV para JSON" )


# SELECIONE E ABRA UM ARQUIVO CSV OU JSON
try:
    prin ( "Qual arquivo você deseja converter?" )
    filename = input("Nome do arquivo: ")
    extension = filename.split(".")[-1].lower()
    
    f = open(nomedoarquivo)

    if extension == "csv":
        # carrega o arquivo csv
        data = list(csv.reader(f))
        print("Arquivo CSV carregado")
    elif extension == "json":
        # carrega o arquivo json
        data = json.load(f,object_pairs_hook=OrderedDict)
        print("Arquivo JSON carregado")
    else:
        print("tipo de arquivo não suportado ... saindo")
        exit()
except Exception as e:
    # erro ao carregar arquivo
    print("Erro ao carregar arquivo ... saindo:",e)
    exit()
else:
    # CONVERTER CSV PARA JSON
    if extension == "csv":
        keys = data[0]
        converted = []

        for i in range(1, len(data)):
            obj = OrderedDict()
            for j in range(0,len(keys)):
                if len(data[i][j]) > 0:
                    obj[keys[j]] = data[i][j]
                else:
                    obj[keys[j]] = None
            converted.append(obj)
        
    # CONVERTER JSON PARA CSV
    if extension == "json":

        # obtém todas as chaves em objetos json
        keys = []
        for i in range(0,len(data)):
            for j in data[i]:
                if j not in keys:
                    keys.append(j)
        
         # mapeia dados em cada linha para o índice de chave
        converted = []
        converted.append(keys)

        for i in range(0,len(data)):
            row = []
            for j in range(0,len(keys)):
                if keys[j] in data[i]:
                    row.append(data[i][keys[j]])
                else:
                    row.append(None)
            converted.append(row)

   # CRIAR ARQUIVO DE SAÍDA
    converted_file_basename = os.path.basename(nomedoarquivo).split(".")[0]
    converted_file_extension = ".json" if extension == "csv" else ".csv"

    if(os.path.isfile(converted_file_basename + converted_file_extension)):
        counter = 1
        while os.path.isfile(converted_file_basename + " (" + str(counter) + ")" + converted_file_extension):
            counter += 1
        converted_file_basename = converted_file_basename + " (" + str(counter) + ")"
    
    try:
        if converted_file_extension == ".json":
            with open(converted_file_basename + converted_file_extension, 'w') as outfile:
                json.dump(converted, outfile)
        elif converted_file_extension == ".csv":
            with open(converted_file_basename + converted_file_extension, 'w') as outfile:
                writer = csv.writer(outfile)
                writer.writerows(converted)
    except:
        print("Erro ao criar arquivo... saindo")
    else:
        print("Arquivo criado:",converted_file_basename + converted_file_extension)
