compt=0

class ABR:
      def __init__(self,value=0,gauche=None,droite=None):
          self.value=value
          self.gauche=gauche
          self.droite=droite


      def insertion(self,valeur):
          if valeur>self.value:
              if self.droite==None:
                  self.droite=ABR(valeur)
              else:
                  self.droite.insertion(valeur)
          elif valeur<self.value:
              if self.gauche==None:
                  self.gauche=ABR(valeur)
              else:
                  self.gauche.insertion(valeur)



      def recherche(self,valeur):
          global compt
          if valeur==self.value:
              return compt
          if valeur>self.value:
              compt+=1
              self.droite.recherche(valeur)
              return compt
          elif valeur < self.value:
              compt+=1
              self.gauche.recherche(valeur)
              return compt

      def hauteur(self):
          pass

      def affichage_console(self,arbre):
          pass

if __name__=="__main__":
   ag=ABR(3)
   ad=ABR(6)
   arbre=ABR(5,ag,ad)
   arbre.insertion(10)
   arbre.insertion(4)
   print(arbre.recherche(10))
