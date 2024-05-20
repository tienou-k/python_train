class Auto:
	def __init__(self, m, n):
		self.moteur = m
		self.nom = n
	def display(self):
		print("Votre ", self.nom," a une puissance de ", self.moteur,"Chevaux")
		
class Car(Auto):
	def __init__(self):
		self.x= input("Entrer le nom: ")
		self.y= int(input("Puissance: "))
		Auto.__init__(self,self.y,self.x)
c =Car()
c.display()