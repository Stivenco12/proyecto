import os
import modules.ejecuto_data_cita as edc
import modules.ejecuta_data_medico as edm
import modules.ejecuta_data_usuario as edu
import registros.globales as g
import ui.medicos as me
import ui.mai as m
def administradorpri():
    class adminis :
        def __init__(self, nom, pwd):
            self.nom = nom
            self.pwd = pwd
    AD = adminis("jorverl", "89123")
    administrador = [AD]
    n = input ("ingrese su nombre de administrador")
    p = input ("Ingrese su contraseña de administrador")
    k = 0
    for i in range (len(administrador)):
        if administrador[i].nom == n and administrador[i].pwd == p:
            print (administrador[i].nom, "bienvenido al menu admid")
            k = 1
            m.menuprincipal(0)
            break
            
    if k==0:
        print("intente nueva mente")
        if(bool(input("deseas intentarlo de nuevo S(si) o Enter(no)"))):
            administradorpri()
        else:
            menuprincipal(0)

def medicoadmid():
    class medic :
        def __init__(self,contraseña):
            self.contraseña = contraseña
    ME = medic("78123")
    medico = [ME]
    c = input ("ingrese la contraseña global de los medicos")
    k = 0
    for i in range (len(medico)):
        if medico[i].contraseña == c:
            print (medico[i].contraseña, "bienvenido al menu admid")
            k = 1
            break
    if k==0:
        print("intente nueva mente")
        if(bool(input("deseas intentarlo de nuevo S(si) o Enter(no)"))):
            medicoadmid()
        else:
            menuprincipal(0)
def menuprincipal(op):
    os.system("cls")
    title = """
    🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦
    🟦      MENU DE OPCIONES DE INICIO        🟦
    🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦
    """
    menuprincipalop = "1. opciones de administrador \n2 opciones de medico  \n3 usuarios \n4 salir "
    if (op !=4):
        print (title)
        print (menuprincipalop)
        try:
            opcion = int(input(":) "))
        except ValueError:
            print ("error en la opccion ingresada")
            menuprincipal(0)
        else: 
            match (opcion):
                case 1:
                    administradorpri()
                    m.menuprincipal(0)
                case 2:
                    medicoadmid()
                    me.menumedicos(0)
                case 3:
                    import ui.usuarios as us
                    us.menuusuarios(0)
                case 4:
                    print ("hasta luego")
if __name__ == "__main__":
    edc.MY_DATA_CITA = "proyecto/data/data_cita.json"
    edm.MY_DATA_MEDICO = "proyecto/data/medico.json"
    edu.MY_DATA_USUARIO = "proyecto/data/usuario.json"
    menuprincipal(0)                     