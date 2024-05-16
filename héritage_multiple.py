class A:
    def afficherA(self):
        print('Class 1')
class B:
    def afficherB(self):
        print('Class 2')
class C(A, B):
    """"
    Il est à noter que l’objet de C (classe enfant) 
    peut appeler les méthodes de ses classes parentes A et B. 
    Par conséquent, vous pouvez dire que C hérite de tout ce qui est A et B.   
    """
    def afficherC(self):
        print('Class 3')
objClass = C()
objClass.afficherA()
objClass.afficherB()
objClass.afficherC()