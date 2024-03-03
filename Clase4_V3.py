class Paciente:
    def __init__(self):
        self.__nombre = '' 
        self.__apellido = ''
        self.__cedula = 0 
        self.__genero = '' 
        self.__servicio = '' 
              
    #metodos get    
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
    def __init__(self):
        self.__lista_pacientes = [] 
        
    def verificarPaciente(self,buscar):
        for p in self.__lista_pacientes:
            if buscar == p.cedula or buscar.lower() in p.nombre.lower():
                return p
            return None
        
    def ingresarPaciente(self,pac):
        self.__lista_pacientes.append(pac)
        return True
    
    def verDatosPaciente(self, n,c,a):
        pac = self.verificarPaciente(n)
        if pac: #¿Se encontró el paciente?
            return pac
        
        pac = self.verificarPaciente(c)
        if pac:
            return pac
        
        pac = self.verificarPaciente(a)
        if pac:
            return pac
        
        nombre_apellido = n + " " + a 
        pac = self.verificarPaciente(nombre_apellido.strip())
        if pac:
            return pac
        
        return None

  
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
            if sis.verificarPaciente(cedula):
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
            buscar = input("Ingrese la cedula, nombre o apellido del paciente: ")
            pac = sis.verDatosPaciente(buscar)
            if pac:
                print("Nombre:",pac.verNombre())
                print("Cedula: ", str(pac.verCedula()))
                print("Genero: ", pac.verGenero())
                print("Servicio:", pac.verServicio())
            else:
                print("No existe un paciente con ese dato")
        elif opcion !=0:
            continue 
        else:
            break 

#aca el python descubre cual es la funcion principal
if __name__ == "__main__":
    main() 
        
        
        
        
        
        
        
        
