#!/usr/bin/python3

import requests
import os
from requests.models import HTTPBasicAuth
from tqdm import tqdm

def Download(url, name):
    
    progressBarCount = 0
    roman = ['I','II','III','IV','V','VI','VII', 'VIII', 'IX', 'X']
    numeric = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10'] 
    module = url[-13:-12]
    available = []
    module_count = 0
    progress = progressBarCount
    
    if module in roman:
        module_number = roman
    if module in numeric:
      module_number = numeric
    #else: colocar algo aqui para aparecer na interface
    
    for i in tqdm(module_number):
      progress = progress + 10
      url = url[:-13] + i + url[-12:]
      response = requests.get(url, auth= HTTPBasicAuth('24246760', '3mShimizu'))      
      print(response.status_code)
      if response.status_code == requests.codes.OK: #pylint: disable=E1101
        available.append(i)
        
        module_count = module_count + 1
        
      else:  
        progress = 100
        print(progress, module_count, available)
        break
      
      for i in tqdm(available):
        file_name = os.path.join(f'output/{materia}', materia+f' - Unidade {i}.pdf')
        url_download = url[:-13] + i + url[-12:]
        resp = requests.get(url_download)
        if resp.status_code == requests.codes.OK: #pylint: disable=E1101
            with open(file_name, 'wb') as new_file:
                new_file.write(resp.content)
            resp.raise_for_status()
        else:
            print('Não Encontrado...')

    
