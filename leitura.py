import pandas as pd
from listas import Listar
from leitura import Moldar
import os
import re

mo = Moldar()
ls = Listar()

cam = 'Z:\\CONTROLLER\\CAMPANHAS\\AGENTE\\'
for i in ls.lista_anos():
    ano = i
    arquivos = []
    for n in ls.lista_meses():
        mes = n
        cam_completo = (f'{cam}{ano}\\{ano}{mes}')
        try:
            caminhos = os.listdir(cam_completo)
            for i in caminhos:
                if re.search(r'BONUS',i) and not re.search(r'DIFERENÇA',i) and not re.search(r'_consolidado.',i) and not re.search(r'~',i):
                    arquivos.append(f'{cam_completo}\\{i}')
        except:
            pass
    for i in arquivos:
        print(i)
        carga = pd.read_excel(i)
        print(carga)
