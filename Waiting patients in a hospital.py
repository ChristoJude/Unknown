# -*- coding: utf-8 -*-
"""
Created on Wed Dec  8 11:54:56 2021

@author: chris
"""
#Empty list
l=[]                       
c=1
#To loop the print statements and the other functions
while (c>=1):
    print("")
    print("OPTIONS")
    print("1.Add")
    print("2.Delete")
    print("3.Display")
    print("4.Exit")
    print("")
    choice=int(input("Enter a option:"))
    #To add tokens to teh lsit
    if choice==1:
        b=int(input("How many tokens?:"))
        for b in range(1,b+1):
           a=int(input("Enter Value:"))
           l.append(a)
    #To remove the token
    elif choice==2:
        print("Deleted token:",l.pop(0))
    #To display teh list in reverse order   
    elif choice==3:
        d=len(l)
        for i in range(d-1,-1,-1):
            print(l[i])
    #To exit the function
    elif choice==4:
        break
    #Error 
    else:
        print("OPTION UNAVAILABLE!")
        