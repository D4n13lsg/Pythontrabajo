class alumno:
  def __init__(self):
    self.nombre=input("ingrese su nombre: ")
    self.nota=int(input("ingrese la nota: "))

class nota(alumno):
  def __init__(self):
    super().__init__()
    
  def notatotal(self):
    if self.nota >= 3:
      print("usted aprobo con: ",self.nota,self.nombre)
    else:
      print("usted perdio con: ",self.nota,self.nombre)

nota1=nota()
nota1.notatotal()
