import os
import modules.ejecuto_data_cita as edc
import modules.ejecuta_data_medico as edm
import modules.ejecuta_data_usuario as edu
import registros.globales as g
def menuprincipal(op):
    os.system("cls")
    title = """
    🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦
    🟦MENU DE ADMINISTRADOR🟦🟦    
    🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦
    """
    print("bienvenido administrador jorverl,aqui esta su contraseña 89123")
    menuprincipalop = "1. gestion de citas \n2 registro de pacientes \n3 registrar medicos \n4 ver historial de algun paciente o medico\n5 salir "
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
                    import ui.citas as c
                    c.menucitas(0)
                case 2:
                    import ui.usuarios as u
                    u.menuusuarios(0)
                case 3:
                    import ui.medicos as m
                    m.menumedicos(0)
                case 4:
                    import ui.historial as h
                    h.menuhistorial(0)
                case _:
                    print ("opciones ingresada no pertence al menu del centro medico")
                    menuprincipal(0)
if __name__ == "__main__":
    edc.MY_DATA_CITA = "proyecto/data/data_cita.json"
    edm.MY_DATA_MEDICO = "proyecto/data/medico.json"
    edu.MY_DATA_USUARIO = "proyecto/data/usuario.json"
    menuprincipal(0)                        