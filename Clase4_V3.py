class Paciente:
    def __init__(self): #constructor
        #encapsulamiento (atributos privados), no podemos acceder a ellos fuera de la clase Paciente.
        self.__nombre = '' 
        self.__apellido = ''
        self.__cedula = 0 
        self.__genero = '' 
        self.__servicio = '' 
              
    #metodos get   
    #Todos estos metodos son publicos para acceder a los atributos de manera "controlada"
    def verNombre(self):
        return self.__nombre 
    def verApellido(self):
        return self.__apellido
    def verCedula(self):
        return self.__cedula 
    def verGenero(self):
        return self.__genero 
    def verServicio(self):
        return self.__servicio 
    # metodos set
    def asignarNombre(self,n):
        self.__nombre = n 
    def asignarApellido (self,a):
        self.__apellido = a
    def asignarCedula(self,c):
        self.__cedula = c 
    def asignarGenero(self,g):
        self.__genero = g 
    def asignarServicio(self,s):
        self.__servicio = s 
        
class Sistema:    
    def __init__(self): #constructor
        self.__lista_pacientes = [] 
        
    def verificarPaciente(self,buscar,opcion_busqueda):
        for p in self.__lista_pacientes:
            if opcion_busqueda ==1 and str(buscar) ==str(p.verCedula()): 
                return p
            elif opcion_busqueda == 2 and str(buscar).lower() in p.verNombre().lower():
                return p
            elif opcion_busqueda == 3 and str(buscar).lower() in p.verApellido().lower():
                return p
        return None
    
    def ingresarPaciente(self,pac):
        self.__lista_pacientes.append(pac)
        return True
    
    def verDatosPaciente(self, buscar,opcion_busqueda):
        if opcion_busqueda == 1:
            pac = self.verificarPaciente(buscar,1)
            if pac:
                return pac
        elif opcion_busqueda == 2:
            pac = self.verificarPaciente(buscar,2)
            if pac:
                return pac
        elif opcion_busqueda == 3:
            pac = self.verificarPaciente(buscar,3)
            if pac:
                return pac
            
        #No implementé esta parte
        else:
            partes_nombre = buscar.split()
            nombre = partes_nombre[0]
            apellido = partes_nombre[1] if len(partes_nombre) > 1 else None
            pac = self.verificarPaciente(nombre, 2) if apellido is None else self.verificarPaciente(nombre + " " + apellido, 2)
            if pac:
                return pac
        return None
        
        #No se hace uso de la herencia, las clases paciente y sistema no heredan de otras clases.
        #Tampoco se ve una implementacion clara de polimorfismo. Se podria implementar por ejemplo si se agregan mas metodos a la clase paciente o subclases para definir comportamientos especificos.
    def verNumeroPacientes(self):
        print("En el sistema hay: " + str(len(self.__lista_pacientes)) + " pacientes") 

def main():
    sis = Sistema() 
    #probemos lo que llevamos programado
    while True:
        #TAREA HACER EL MENU
        opcion = int(input("\nIngrese \n0 para salir, \n1 para ingresar nuevo paciente, \n2 ver Paciente\n\t--> ")) 
        
        if opcion == 1:
            #ingreso pacientes
            print("A continuacion se solicitaran los datos ...") 
            #1. Se solicitan los datos
            cedula = int(input("Ingrese la cedula: ")) 
            if sis.verificarPaciente(cedula,1):
                print("\n<< Ya existe un paciente con esa cedula >>".upper()) 
            else:    
                # 2. se crea un objeto Paciente
                pac = Paciente() 
                # como el paciente esta vacio debo ingresarle la informacion
                pac.asignarNombre(input("Ingrese el nombre: ")) 
                pac.asignarCedula(cedula) 
                pac.asignarGenero(input("Ingrese el genero: ")) 
                pac.asignarServicio(input("Ingrese servicio: ")) 
                #3. se almacena en la lista que esta dentro de la clase sistema
                r = sis.ingresarPaciente(pac)             
                if r:
                    print("Paciente ingresado") 
                else:
                    print("No ingresado") 
        elif opcion == 2:
            #Para simplificar el problema, pregunto al usuario el parametro de busqueda.
            opcion_busqueda = int(input("Ingrese 1 para buscar por cédula, 2 por nombre, 3 por apellido: "))
            if opcion_busqueda in [1,2,3]:
                buscar = input("Ingrese la informacion del paciente: ")
                pac = sis.verDatosPaciente(buscar,opcion_busqueda)
                if pac:
                    print("Nombre:",pac.verNombre())
                    print("Cedula:",str(pac.verCedula()))
                    print("Genero:",pac.verGenero())
                    print("Servicio:",pac.verServicio())
                else:
                    print("paciente no encontrado")
            else:
                print("opcion no valida,intente nuevamente")
                

        elif opcion ==0:
            break
        else:
            print("opcion invalida, intente nuevamente")

#aca el python descubre cual es la funcion principal
if __name__ == "__main__":
    main() 
        
        
        
        
        
        
        
        
