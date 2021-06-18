#!/usr/bin/python3

import requests
import os
import argparse


def pdfdownloader(url, endereco):
    

    resp = requests.get(url)
    
    if resp.status_code == requests.codes.OK: #pylint: disable=E1101
        
        with open(endereco, 'wb') as new_file:
            new_file.write(resp.content)
            print(f"Download finalizado com sucesso! \n")
            

        resp.raise_for_status()
    

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='')
    parser.add_argument('link1', type=str, help='Primeira parte do link')
    parser.add_argument('numero_do_modulo', help='Numero do Módulo')
    parser.add_argument('link2', type=str, help='Segunda parte do link')
    parser.add_argument('nome', type=str, help='nome da materia')
    args = parser.parse_args()
    print(f"-------- {args.nome} ---------")

    url = args.link1
    url2 = args.link2
    if args.numero_do_modulo == 'I' or 'II':
        numero = ['I','II','III','IV','V','VI','VII']
    else:
	    numero = ['1', '2', '3', '4', '5', '6', '7']

    materia = args.nome
    os.mkdir(f'output/{materia}')
    for i in numero:
        file_name = os.path.join(f'output/{materia}', materia+f' - Unidade {i}.pdf')
        print(f'baixando {materia} - Unidade {i}.pdf ...')
        pdfdownloader(url+i+url2, file_name)
            


      
