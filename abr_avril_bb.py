
class ABR:
      def __init__(self,value=0,gauche=None,droite=None):
          self.value=value
          self.gauche=gauche
          self.droite=droite


      def insertion(self,valeur):
          if valeur>self.value:




             courant=self.droite
             while courant.droite!=None:
                   if valeur>self.value:
                      courant=self.droite.droite

             if courant.droite==None:
                self.droite=ABR(valeur)
          """
          elif valeur<self.value:




          elif valeur<self.value and self.droite==None:
               arbre.gauche=ABR(valeur)
          """


if __name__=="__main__":
   ag=ABR(3)
   ad=ABR(6)
   arbre=ABR(5,ag,ad)
   arbre.insertion(10)
