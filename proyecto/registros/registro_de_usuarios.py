import json
import os
import registros.globales as g
import modules.ejecuta_data_usuario as es
import ui.usuarios as uiu
def registrar_usuario(op):
        title = """
        ***********************
        * REGISTRO DE USUARIO *
        ***********************
        """
        g.borrar_pantalla()
        print(title)
        try:        
            cedula = int(input ("ingrese Nmr de la cedula"))
            nombre = input ("ingrese su nombre")
            apellido = input ("ingrese su apellido")
            celular = int(input ("ingrese su numero telefonico"))
            correo = input ("ingrese su correo por favor")
            edad = int(input("ingrese su edad"))
            menutipo = ("cual es su genero \n1 HOMBRE \n2 MUJER \n3 OTRO")
            if (op !=3):
                print (title)
                print (menutipo)
                try:
                    opcion = int(input(":) "))
                except ValueError:
                    print ("error en la opcion ingresada")
                    registrar_usuario(0)
                else:
                    match (opcion):
                        case 1:
                            genero = ("hombre")
                        case 2: 
                            genero = ("mujer")
                        case 3:
                            genero = ("otro")
                        case _:
                            print ("opciones ingresada no pertence al menu del centro medico")
                            registrar_usuario(0)
            fechanacimiento = input("ingrese la fecha de su nacimiento dia/mes/año")
        except ValueError:
            print ("error en la opccion ingresada")
            registrar_usuario(0)
        usuario = {
        "cedula" : cedula,
        "nombre" : nombre,
        "apellido" : apellido,
        "correo" : correo,
        "celular" : celular,
        "genero" : genero,
        "edad" : edad,
        "fechanacimiento" : fechanacimiento,
        }
        es.agregar_data("/proyecto/data/usuario.json",cedula,usuario)
        g.usuario.get("/proyecto/data/usuario.json")
        if(bool(input("desea registrar otro usuario S(si) o Enter(no)"))):
            registrar_usuario(0)
        else:
            uiu.menuusuarios(0)


def buscar_data_usuarios():
    criterio = input('Ingrese el Nro Identificacion del estudiante: ')
    data =g.usuario.get('datos_usuario').get(criterio)
    return data
    
def modificar_data_usuarios():
    datausuario = buscar_data_usuarios()
    identificacion,codStudent,nombreStudent,notas = datausuario.values()
    for key in datausuario.keys():
        if (key != 'identificacion' and key != 'notas'):
            if(bool(input(f'Desea modificar el {key} s(si) o Enter No'))):
                datausuario[key] = input(f'Ingrese el nuevo valor para {key} :')
    g.usuario.get('data').update({identificacion:datausuario})
    es.actualizar_archivo(g.usuario)
    uiu.menuusuarios(0)