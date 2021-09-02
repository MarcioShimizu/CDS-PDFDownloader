#!/usr/bin/python3
import requests
import os
import argparse
from tqdm import tqdm

def pdfdownloader(url, endereco): #baixa os pdsf
    

    resp = requests.get(url)
    
    if resp.status_code == requests.codes.OK: #pylint: disable=E1101
        
        with open(endereco, 'wb') as new_file:
            new_file.write(resp.content)
            

        resp.raise_for_status()
    else:
        print('Não Encontrado...')
    
def pdfcount(link):
    print('Verificando quantidade de material disponível...')
    link_num = link[-13:-12]
    disponivel = []
    quantidade = 0
    if link_num == 'I' or 'II':
        numero = ['I','II','III','IV','V','VI','VII']
    else:
	    numero = ['1', '2', '3', '4', '5', '6', '7']
     
    for i in tqdm(numero):
        url = link[:-13] + i + link[-12:]
        resp = requests.get(url)
        if resp.status_code == requests.codes.OK: #pylint: disable=E1101
            disponivel.append(i)
            quantidade = quantidade + 1
    print(f'Encontramos {quantidade} livros, preparando Download...')
    return disponivel
             
         
    



if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='')
    parser.add_argument('link1', type=str, help='Primeira parte do link')
    parser.add_argument('nome', type=str, help='nome da materia')
    args = parser.parse_args()
    print("""
          
          
          
          
          
          """)
    print(f"-------- {args.nome} ---------")

    url = args.link1
    numero = pdfcount(url)

    materia = args.nome
    os.mkdir(f'output/{materia}')
    
    for i in tqdm(numero):
        file_name = os.path.join(f'output/{materia}', materia+f' - Unidade {i}.pdf')
        url_download = url[:-13] + i + url[-12:]

        pdfdownloader(url_download, file_name)
    print(f'Download finalizado com sucesso! Verifique na pasta output/{materia}')
            


      
