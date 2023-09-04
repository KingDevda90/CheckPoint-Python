#!/usr/bin/env python
# coding: utf-8

# In[ ]:


Shop = []
while True : 
    print("Appuyer sur 1 pour ajouter sur la liste : \nAppuyer sur 2 pour suprimer de la liste : \nAppuyer sur 3 pour afficher la liste : \nAppuyer sur 4 pour quitter : " )
    choice = input("Quelle action souhaitez vous faire : ")
    if choice == "1" :
        element = input("Ajouter l'element : ")
        Shop.append(element)
        print(f"{element} a bien été ajouté.")
    elif choice == "2" :
        if len(Shop) == 0 :
            print("La liste est vide")
        else :
            element = input("Entrer l'element à supprimer : ")
            Shop.remove(element)
            print(f"{element} a bien ètè supprimer ")
    elif choice == "3" :
        if len(Shop) == 0 :
            print("La liste est vide! ")
        else : 
            print("La liste est : ",Shop)
    elif choice == "4" :
        print("Au revoir")
        break
    else :
        print("Choix invalide : Veuillez entrer le bon numero")
        


# In[ ]:




