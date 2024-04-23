compt=0
l_total=[]

class ABR:
      def __init__(self,value=0,gauche=None,droite=None):
          self.value=value
          self.gauche=gauche
          self.droite=droite
      

      """
      def __repr__(self) -> str:
        global l_total
        l_total.append(self.value)
        self.droite.__repr__()
        self.gauche.__repr__()
        print(l_total)
        init=l_total[0]
        l_constru=[]
        a=0
        for i in range(len(l_total)):
            if l_total[i]==init:
                l_constru.append(l_total[i])
                a+=1
            elif l_total[i]>init:
                l_constru.append(l_total[i])
                a+=1
                while l_total[a]>init:
                    pass
      """

      def __repr__(self) -> str:
        global l_total
        l_total.append(self.value)
        self.droite.__repr__()
        self.gauche.__repr__()


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

def identif_enfants():
    init=l_total[0]
    parent_droite=None
    parent_gauche=None
    block_gauche=False
    block_droite=False
    for i in range(len(l_total)):
        #print(l_total[i])

        if l_total[i]>init and block_droite==False:
            parent_droite=(l_total[i],i)
            block_droite=True
        if l_total[i]<init and block_gauche==False:
            parent_gauche=(l_total[i],i)
            block_gauche=True

    return(parent_droite,parent_gauche)


def suite():
    parent_droite,parent_gauche=identif_enfants()
    print(l_total)
    print(parent_droite,parent_gauche)
    liste_1=l_total[parent_droite[1]:parent_gauche[1]]
    print(liste_1)



if __name__=="__main__":
   ag=ABR(3)
   ad=ABR(7)
   arbre=ABR(5,ag,ad)
   arbre.insertion(10)
   arbre.insertion(2)
   arbre.insertion(4)
   arbre.insertion(6)
   arbre.insertion(1)
   #print(arbre.recherche(10))
   print(arbre.__repr__())
   print(suite())
