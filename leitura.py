import pandas as pd
from listas import Listar
from arquitetura import Moldar
from connection import Db
import os
import re

db = Db()
mo = Moldar()
ls = Listar()

cam = 'Z:\\CONTROLLER\\CAMPANHAS\\AGENTE\\'
carga_inserir = []
for i in ls.lista_anos():
    ano = i
    arquivos = []
    for n in ls.lista_meses():
        mes = n
        cam_completo = (f'{cam}{ano}\\{ano}{mes}')
        try:
            caminhos = os.listdir(cam_completo)
            for i in caminhos:
                if re.search(r'BONUS',i) and not re.search(r'BONUS.09',i) and not re.search(r' REF ',i) and not re.search(r'DIFERENÇA',i) and not re.search(r'_consolidado.',i) and not re.search(r'~',i):
                    arquivos.append(f'{cam_completo}\\{i}')
        except:
            pass
    for i in arquivos:
        anomes = int(str(i).split('\\')[5])
        print(i)
        carga = pd.read_excel(i)
        mo.decode_tip(carga.columns,anomes)
        for index in carga.index:
            colunas = mo.dados()
            for i in colunas:
                carga_inserir.append({
                    'mesBase' : anomes,
                    'cdAgente' : int(str(carga[i['cdAgente']][index]).replace('NaN','0').replace('.0','').replace('nan','0')), 
                    'nmAgente' : str(carga[i['nmAgente']][index]), 
                    'dtProposta' : str(carga[i['dtProposta']][index]), 
                    'nmCliente' : 'NULL',
                    'nuCpf' : str(carga[i['nuCpf']][index]), 
                    'nuProposta' : str(carga[i['nuProposta']][index]).replace('NaN','0').replace('.0','').replace('nan','0').replace('c              ','0'), 
                    'nmBanco' : str(carga[i['nmBanco']][index]), 
                    'nmProduto' : str(carga[i['nmProduto']][index]), 
                    'tpOperacao' : str(carga[i['tpOperacao']][index]), 
                    'qtdPlano' : int(str(carga[i['qtdPlano']][index]).replace('NaN','0').replace('.0','').replace('nan','0')), 
                    'dtCreditoCliente' : str(carga[i['dtCreditoCliente']][index]), 
                    'dtBaixa' : str(carga[i['dtBaixa']][index]), 
                    'vrBaseCalculo' : float(carga[i['vrBaseCalculo']][index]), 
                    'pcBonus' : float(carga[i['pcBonus']][index]), 
                    'vrBonus' : float(carga[i['vrBonus']][index]),
                    'id_proposta' : 0
                })

carga = [i for i in carga_inserir]

for i in range(0,len(carga),10):
    data = carga[i:(i+10)]
    print(data)
    db.inserir(data)

print('PROCESSO FINALIZADO')
