import json
import os

MY_DATA_MEDICO = 'data/'

def nuevo_file(*param):
    with open(MY_DATA_MEDICO,"w") as wf:
        json.dump(param[0],wf,indent=4)

def actualizar_archivo(*param):
    with open(MY_DATA_MEDICO,'w') as fw:
        json.dump(param[0],fw,indent=4)

def agregar_data(*param):
    data = list(param)
    with open(MY_DATA_MEDICO,"r+") as rwf:
        data_file=json.load(rwf)
        if (len(param) > 1):
            data_file[data[0]].update({data[1]:data[2]})
        else:
            data_file.update({param[0]})
        # data_file[llavePrincipal].update({codigo:info})
        rwf.seek(0)
        json.dump(data_file,rwf,indent=4)

def leer_archivo():
    with open(MY_DATA_MEDICO,"r") as rf:
        return json.load(rf)
    
def checkFile(*param):
    data = list(param)
    if(os.path.isfile(MY_DATA_MEDICO)):
        if(len(param)):
            data[0].update(leer_archivo())
    else:
        if(len(param)):
            nuevo_file(data[0])