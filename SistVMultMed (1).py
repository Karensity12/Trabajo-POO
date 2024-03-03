from datetime import datetime
class Medicamento:
    def __init__(self): #constructor
        #Encapsulamiento de datos
        self.__nombre = "" 
        self.__dosis = 0 
    
    #getters
    def verNombre(self):
        return self.__nombre 
    def verDosis(self):
        return self.__dosis 
    #setters
    def asignarNombre(self,med):
        self.__nombre = med 
    def asignarDosis(self,med):
        self.__dosis = med 
        
class Mascota:
    
    def __init__(self): #constructor
        #Encapsulamiento
        self.__nombre= " "
        self.__historia=0
        self.__tipo=" "
        self.__peso=" "
        self.__fecha_ingreso=" "
        self.__lista_medicamentos=[]

    #getters 
    def verNombre(self):
        return self.__nombre
    def verHistoria(self):
        return self.__historia
    def verTipo(self):
        return self.__tipo
    def verPeso(self):
        return self.__peso
    def verFecha(self):
        return self.__fecha_ingreso
    def verLista_Medicamentos(self):
        return self.__lista_medicamentos 

    #setters     
    def asignarNombre(self,n):
        self.__nombre=n
    def asignarHistoria(self,nh):
        self.__historia=nh
    def asignarTipo(self,t):
        self.__tipo=t
    def asignarPeso(self,p):
        self.__peso=p
    def asignarFecha(self,f):
        self.__fecha_ingreso=f
    def asignarLista_Medicamentos(self,n):
        self.__lista_medicamentos = n 
    
    def verificarMedicamentos(self,medicamento):
        for m in self.__lista_medicamentos:
            if medicamento.verNombre() == m.verNombre():
                print("Medicamento ya registrado en la base de datos")
                return False
        self.__lista_medicamentos.append(medicamento)
        return True
            
    def eliminarMedicamento(self,nm):
        for med in self.__lista_medicamentos:
            if med.verNombre() == nm:
                self.__lista_medicamentos.remove(med)
                return True
            return False
    
class sistemaV:
    def __init__(self): #constructor
        self.__felinos = {}
        self.__caninos = {}
    
    def verificarExiste(self,historia):
        if historia in self.__felinos or historia in self.__caninos:
            return True
        return False
    
    def verNumeroMascotas(self):
        return len(self.__felinos) + len(self.__caninos)
    
    def ingresarMascota(self,mascota):
        if mascota.verTipo().lower() == "canino": #Se hace uso del lower para evitar problemas cuando el usuario escribe el tipo de mascota a ingresar en el sistema
            self.__caninos[mascota.verHistoria()] = mascota #historia clinica: key
        elif mascota.verTipo().lower() == "felino":
            self.__felinos[mascota.verHistoria()] = mascota
        else:
            print("Ingrese un tipo de mascota valido")
    
    def verFechaIngreso(self,historia):
        if historia in self.__caninos:
            return self.__caninos[historia].verFecha()
        elif historia in self.__felinos:
            return self.__felinos[historia].verFecha()
        else:
            print("No se encontro la mascota")
            return None

    #Se repite la misma logica que en la anterior funcion
    def verMedicamento(self,historia):
        if historia in self.__caninos:
            return self.__caninos[historia].verLista_Medicamentos()
        elif historia in self.__felinos:
            return self.__felinos[historia].verLista_Medicamentos()
        else:
            print("No se encontro")
            return None
    
    
    def eliminarMascota(self, historia):
        if historia in self.__caninos:
            del self.__caninos[historia]
            return True
        elif historia in self.__felinos:
            del self.__felinos[historia]
            return True
        else:
            return False
    
def validarFecha(fecha_str):
    try:
        datetime.strptime(fecha_str,"%d/%m/%Y")
        return True
    except ValueError:
        return False
#No se hace uso de la herencia, se podria implementar con una clase animal de la que hereden las clases Felino y Canino
#El polimorfismo no esta explicitamente implementado, sin embargo se podria hacer uso si se agregan metodos que definen comportamientos segun si es felino o canino.
    
def main():
    servicio_hospitalario = sistemaV()
    # sistma=sistemaV()
    while True:
        menu=int(input('''\nIngrese una opción: 
                       \n1- Ingresar una mascota 
                       \n2- Ver fecha de ingreso 
                       \n3- Ver número de mascotas en el servicio 
                       \n4- Ver medicamentos que se están administrando
                       \n5- Eliminar mascota 
                       \n6- Salir 
                       \nUsted ingresó la opción: ''' ))
        if menu==1: # Ingresar una mascota 
            if servicio_hospitalario.verNumeroMascotas() >= 10:
                print("No hay espacio ...") 
                continue
            historia=int(input("Ingrese la historia clínica de la mascota: "))
            #   verificacion=servicio_hospitalario.verDatosPaciente(historia)
            if servicio_hospitalario.verificarExiste(historia) == False:
                nombre=input("Ingrese el nombre de la mascota: ")
                tipo=input("Ingrese el tipo de mascota (felino o canino): ")
                peso=int(input("Ingrese el peso de la mascota: "))
                fecha=input("Ingrese la fecha de ingreso (dia/mes/año): ")
               
               #Verificar formato correcto de la fecha para ingresar medicamentos
                if validarFecha(fecha):
                    nm = int(input("Ingrese la cantidad de medicamentos: "))
                    lista_med = []

                    for i in range(nm):
                        nombre_m = input("Ingrese el nombre del medicamento: ")
                        dosis = int(input("Ingrese la dosis: "))
                        #objeto tipo Medicamento
                        medicamento = Medicamento()
                        medicamento.asignarNombre(nombre_m)
                        medicamento.asignarDosis(dosis)
                        lista_med.append(medicamento)
                    
                    #objeto mascota con los datos ingresados por el user
                    mas= Mascota() 
                    mas.asignarNombre(nombre)
                    mas.asignarHistoria(historia)
                    mas.asignarPeso(peso)
                    mas.asignarTipo(tipo)
                    mas.asignarFecha(fecha)

                    for med in lista_med:
                        mas.verificarMedicamentos(med)
                    
                    #agregar la mascota al sistema
                    servicio_hospitalario.ingresarMascota(mas)

                else:
                    print("Fecha ingresada no valida")
            else:
                print("Ya existe una mascota registrada con dicha historia clinica")


        elif menu==2: # Ver fecha de ingreso
            q = int(input("Ingrese la historia clínica de la mascota: "))
            fecha = servicio_hospitalario.verFechaIngreso(q)
            # if servicio_hospitalario.verificarExiste == True
            if fecha != None:
                print("La fecha de ingreso de la mascota es: " + fecha)
            else:
                print("La historia clínica ingresada no corresponde con ninguna mascota en el sistema.")
            
        elif menu==3: # Ver número de mascotas en el servicio 
            numero=servicio_hospitalario.verNumeroMascotas()
            print("El número de pacientes en el sistema es: " + str(numero))

        elif menu==4: # Ver medicamentos que se están administrando
            q = int(input("Ingrese la historia clínica de la mascota: "))
            medicamento = servicio_hospitalario.verMedicamento(q) 
            if medicamento != None: 
                print("Los medicamentos suministrados son: ")
                for m in medicamento:   
                    print(f"\n- {m.verNombre()}")
            else:
                print("La historia clínica ingresada no corresponde con ninguna mascota en el sistema.")

        
        elif menu == 5: # Eliminar mascota
            q = int(input("Ingrese la historia clínica de la mascota: "))
            resultado_operacion = servicio_hospitalario.eliminarMascota(q) 
            if resultado_operacion == True:
                print("Mascota eliminada del sistema con exito")
            else:
                print("No se encuentra una mascota con dicha historia clinica")
        
        elif menu==6:
            print("Usted ha salido del sistema de servicio de hospitalización...")
            break
        
        else:
            print("Usted ingresó una opción no válida, intentelo nuevamente...")

if __name__=='__main__':
    main()





            

                

