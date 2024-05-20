class A:
    def afficherA(self):
        print('Vous êtes dans Class A')
class B(A):
    def afficherB(self):
        print('Vous êtes dans Class B ')
class C(B):
    def afficherC(self):
        print('Vous êtes dans Class C')
objClass = C()
""""
 la classe C peut invoquer les méthodes 
 de ses classes parentes et grand-parentes.
"""
print('- Class grand-père A')
objClass.afficherA()
print('- Class parent B')
objClass.afficherB()
print('- Lui même')
objClass.afficherC()