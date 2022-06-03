class Persona:
    def __init__(self):
        self.num1=int(input("Ingrese el numero: "))
        self.num2=int(input("Ingrese el numero: "))
      
        print("la suma es: ",self.num1+self.num2)
        print("la resta es: ",self.num1-self.num2)
        print("la multiplicacion es: ",self.num1*self.num2)
        print("la divicion es: ",self.num1/self.num2)

persona1=Persona()
