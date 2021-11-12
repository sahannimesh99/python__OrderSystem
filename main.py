print("\n" * 1)                  

import datetime                    
import os                          

list_foods = []                    
list_drinks = []                   
                

list_item_price = [0] * 100        
                                  
var_discount_1 = 200                      
var_discount_2 = 1000                     
var_discount_3 = 5000                     
var_discount_1_rate = 0.05                
var_discount_2_rate = 0.10                
var_discount_3_rate = 0.15                

navigator_symbol = "/" 
if os.name == "nt":
    navigator_symbol = "\\" 

def def_user():                                                                               
    while True:                                             
        print("*" * 31 + "LOGIN AND SING UP PAGE" + "*" * 31 + "\n"    
              "\t(S) SING UP\n"
              "\t(L) LOGIN\n"
              "\t(E) EXIT\n" +
              "_" * 72)

        input_1 = str(input("Please Select Your Wish: ")).upper() 
        if len(input_1) == 1:
            if (input_1 == 'S'):  
                print("\n" * 1)
                def_register()
                break
            elif (input_1 == 'L'):
                print("\n" * 1)
                def_login() 
                break
            elif (input_1 == 'E'):
                print("*" * 32 + "THANK YOU COME AGAIN" + "*" * 31 + "\n")
                break
            else:
                print("\n" * 1 + "ERROR: Invalid Input (" + str(input_1) + "). Something Went Wrong ,Try again!") 
        else:
            print("\n" * 1 + "ERROR: Invalid Input (" + str(input_1) + "). Something Went Wrong ,Try again!")

def def_register():
    n = input("Name: ")
    p = input("Password: ")
    success = True
    print(" ")
    file = open('files'+navigator_symbol+'list_users', 'a')
    file.write(n+" - "+p+"\n")
    print(" ")
    if(success):
        print("-" * 20 + " Hey " + n + "-" * 20)
        print(" ")
        def_main()
    else:
        print("Something Went Wrong ,Try again!")
    
def def_login():
    u = input("Username: ")
    p = input("Password: ")
    success = False
    file = open('files'+navigator_symbol+'list_users', 'r')
    for i in file:
        a,b = i.split(" - ")
        b = b.strip()
        if(a==u and b==p):
            success = True
            break
    file.close()
    if(success):
        print("-" * 20 + "Login Successful" + "-" * 20)
        print()
        def_main()
    else:
        print("Incorrect username or password")


def def_default():
    global list_drinks, list_foods, list_item_order, list_item_price    
    list_item_order = [0] * 100                    
def_default()                                      
                                                   

def def_main():
   while True:
        print("*" * 28 + "FOOD ORDERING SYSTEM" + "*" * 24 + "\n") 
        print("*" * 31 + "MAIN MENU" + "*" * 32 + "\n"     
              "\t(O) ORDER\n"                              
              "\t(L) ITEM LIST\n"
              "\t(P) PAYMENT\n"
              "\t(E) EXIT\n" +
              "_" * 72)

        input_1 = str(input("Please Select Your Operation: ")).upper()    
        if (len(input_1) == 1):                                           
            if (input_1 == 'O'):                                          
                print("\n" * 1)                                        
                def_order_menu()                                          
                break                                                     
            elif (input_1 == 'L'):                                        
                print("\n" * 1)                                        
                def_view()                                              
                break                                                     
            elif (input_1 == 'P'):                                        
                print("\n" * 1)                                         
                def_payment()                                             
                break                                                     
            elif (input_1 == 'E'):                                        
                print("*" * 32 + "THANK YOU COME AGAIN" + "*" * 31 + "\n")           
                break                                                     
            else:                                                                                 
                print("\n" * 1 + "ERROR: Invalid Input (" + str(input_1) + ").Something Went Wrong ,Try again!")     
        else:                                                                                     
            print("\n" * 1 + "ERROR: Invalid Input (" + str(input_1) + "). Something Went Wrong ,Try again!")        


def def_order_menu():                                                                               
    while True:                                             
        print("*" * 31 + "ORDER PAGE" + "*" * 31 + "\n"    
              "\t(F) FOODS AND DRINKS\n"
              "\t(M) MAIN MENU\n"
              "\t(E) EXIT\n" +
              "_" * 72)

        input_1 = str(input("Please Select Your Wish: ")).upper() 
        if len(input_1) == 1:
            if (input_1 == 'F'):  
                print("\n" * 1)
                def_food_drink_order()
                break
            elif (input_1 == 'M'):
                print("\n" * 1)
                def_main() 
                break
            elif (input_1 == 'E'):
                print("*" * 32 + "THANK YOU COME AGAIN" + "*" * 31 + "\n")
                break
            else:
                print("\n" * 1 + "ERROR: Invalid Input (" + str(input_1) + "). Something Went Wrong ,Try again!") 
        else:
            print("\n" * 1 + "ERROR: Invalid Input (" + str(input_1) + "). Something Went Wrong ,Try again!")

def def_full_file_reader():                                                                        
    file_foods = open('files'+navigator_symbol+'list_foods', 'r') 
    for i in file_foods: 
        list_foods.append(str(i.strip())) 
    file_foods.close()

    file_drinks = open('files'+navigator_symbol+'list_drinks', 'r') 
    for i in file_drinks:
        list_drinks.append(str(i.strip()))
    file_drinks.close()


    i = 0
    while i <= (len(list_foods) - 1): 
        if 'Rs' in list_foods[i]:
            list_foods[i] = str(list_foods[i][:list_foods[i].index('Rs') - 1]) + ' ' * (40 - (list_foods[i].index('Rs') - 1)) + str(list_foods[i][list_foods[i].index('Rs'):])
        i += 1

    i = 0
    while i <= (len(list_drinks) - 1):
        if 'Rs' in list_drinks[i]:
            list_drinks[i] = str(list_drinks[i][:list_drinks[i].index('Rs') - 1]) + ' ' * (40 - (list_drinks[i].index('Rs') - 1)) + str(list_drinks[i][list_drinks[i].index('Rs'):])
        i += 1

    
def_full_file_reader()

def def_file_sorter(): 
    global list_foods, list_drinks
    list_foods = sorted(list_foods)
    list_drinks = sorted(list_drinks)
    

    i = 0
    while i < len(list_foods):
        list_item_price[i] = float(list_foods[i][int(list_foods[i].index("Rs") + 2):]) 
        i += 1

    i = 0
    while i < len(list_drinks):
        list_item_price[40 + i] = float(list_drinks[i][int(list_drinks[i].index("Rs") + 2):]) 
        i += 1

   
def_file_sorter()

def def_food_drink_order():    
    while True:
            print("*" * 50 + "ORDER FOODS & DRINKS" + "*" * 50)
            print("-" * 140)
            print(" |NO| |FOOD NAME|                             |PRICE|    ||  |NO| |DRINK NAME|                           |PRICE|")
            print("-" * 140)

            i = 0
            while i < len(list_foods) or i < len(list_drinks):
                var_space = 1
                if i <= 8:                      
                    var_space = 2

                if i < len(list_foods):
                    food = " (" + str(i + 1) + ")" + " " * var_space + str(list_foods[i]) + "  || " 
                else:
                    food = " " * 36 + "|| " 
                if i < len(list_drinks):
                    drink = "(" + str(41 + i) + ")" + " " + str(list_drinks[i])
                else:
                    drink = ""
                print(food, drink)
                i += 1

            print("\n (M) MAIN MENU                   (P) PAYMENT                   (E) EXIT\n" + "_" * 72)


            input_1 = input("Please Select Your Wish: ").upper() 
            if (input_1 == 'M'):
                print("\n" * 1)
                def_main() 
                break
            if (input_1 == 'E'):
                print("*" * 32 + "THANK YOU COME AGAIN" + "*" * 31 + "\n") 
                break
            if (input_1 == 'P'):
                print("\n" * 1)
                def_payment() 
                break
            try:        
                int(input_1)
                if ((int(input_1) <= len(list_foods) and int(input_1) > 0) or (int(input_1) <= len(list_drinks) + 40 and int(input_1) > 40)):
                     try:
                        print("\n" + "_" * 72 + "\n" + str(list_foods[int(input_1) - 1])) 
                     except:
                        pass
                     try:
                         print("\n" + "_" * 72 + "\n" + str(list_drinks[int(input_1) - 41])) 
                     except:
                        pass

                     input_2 = input("Enter the quantity you want?: ").upper() 
                     if int(input_2) > 0:
                        list_item_order[int(input_1) - 1] += int(input_2) 
                        print("\n" * 1)
                        print("Successfully Ordered!")
                        def_food_drink_order() 
                        break
                     else:
                        print("\n" * 1 + "ERROR: Invalid Input (" + str(input_2) + "). Something Went Wrong ,Try again!")
            except:
                print("\n" * 1 + "ERROR: Invalid Input (" + str(input_1) + "). Something Went Wrong ,Try again!")

def def_view():  
   
    while True:
            print("*" * 50 + " FOODS & DRINKS" + "*" * 50)
            print("-" * 140)
            print(" |NO| |FOOD NAME|                             |PRICE|    ||  |NO| |DRINK NAME|                           |PRICE|")
            print("-" * 140)

            i = 0
            while i < len(list_foods) or i < len(list_drinks):
                var_space = 1
                if i <= 8:                      
                    var_space = 2

                if i < len(list_foods):
                    food = " (" + str(i + 1) + ")" + " " * var_space + str(list_foods[i]) + "  || " 
                else:
                    food = " " * 36 + "|| " 
                if i < len(list_drinks):
                    drink = "(" + str(41 + i) + ")" + " " + str(list_drinks[i])
                else:
                    drink = ""
                print(food, drink)
                i += 1

            print("\n (M) MAIN MENU         (A) ADD           (O) Order            (E) EXIT\n" + "_" * 72)


            input_1 = input("Please Select Your Wish: ").upper() 
            if (input_1 == 'M'):
                print("\n" * 1)
                def_main() 
                break
            if (input_1 == 'A'):
                print("\n" * 1)
                def_item_add() 
                break
            if (input_1 == 'E'):
                print("*" * 32 + "THANK YOU COME AGAIN" + "*" * 31 + "\n") 
                break
            if (input_1 == 'O'):
                print("\n" * 1)
                def_order_menu() 
                break
            try:        
                int(input_1)
                if ((int(input_1) <= len(list_foods) and int(input_1) > 0) or (int(input_1) <= len(list_drinks) + 40 and int(input_1) > 40)):
                     try:
                        print("\n" + "_" * 72 + "\n" + str(list_foods[int(input_1) - 1])) 
                     except:
                        pass
                     try:
                         print("\n" + "_" * 72 + "\n" + str(list_drinks[int(input_1) - 41])) 
                     except:
                        pass

                     
                     else:
                        print("\n" * 1 + "ERROR: Invalid Input ")
            except:
                print("\n" * 1 + "ERROR: Invalid Input (" + str(input_1) + "). Something Went Wrong ,Try again!")

def def_item_add():
    print(" ")
    f = input("Food Name : ")
    s = input("selling Price : ")
    print(" " + "\n")
    
    success = True
    file = open("D:\Python\python_OrderSystem\Files\list_foods","a")
    file.write("\n"+f+" ""Rs"+s+"\n")
    print(" ")
    file.close()
    if(success):
        print("----------------Item add Successful----------------")
        def_main()
    else:
        print("Wrong input")


def def_payment():
    while True:
        print("*" * 32 + "PAYMENT" + "*" * 33 + "\n") 
        total_price = 0 

        report_new = "\n\n\n" + " " * 17 + "*" * 35 + "\n" + " " * 17 + "DATE: " + str(datetime.datetime.now())[:19] + "\n" + " " * 17 + "-" * 35 
        i = 0
        while i < len(list_item_order): 
            if(list_item_order[i] != 0):
                if (i >= 0) and (i < 40):
                    report_new += "\n" + " " * 17 + str(list_foods[i]) + "  x  " + str(list_item_order[i]) 
                    print(" " * 17 + str(list_foods[i]) + "  x  " + str(list_item_order[i])) 
                    total_price += list_item_price[i] * list_item_order[i] 
                if (i >= 40) and (i < 80):
                    report_new += "\n" + " " * 17 + str(list_drinks[i - 40]) + "  x  " + str(list_item_order[i])
                    print(" " * 17 + str(list_drinks[i - 40]) + "   x  " + str(list_item_order[i]))
                    total_price += list_item_price[i] * list_item_order[i] 
                i += 1
            else:
                i += 1
        
        if total_price > var_discount_3: 
            total_price -= total_price * var_discount_3_rate 
            report_new += "\n" + " " * 17 + "-" * 35 + "\n" \
                "" + " " * 17 + "DISCOUNT RATES:      % " + str(var_discount_3_rate * 100) + "\n" \
                "" + " " * 17 + "DISCOUNT AMOUNTS:   Rs " + str(round(total_price * var_discount_3_rate, 2)) + "\n" + " " * 17 + "_" * 35 + "\n" \
                "" + " " * 17 + "TOTAL PRICES:       Rs " + str(round(total_price, 2)) + "\n" + " " * 17 + "*" * 35 
            print(" " * 17 + "-" * 35 + "\n"
                "" + " " * 17 + "DISCOUNT RATES:      % " + str(var_discount_3_rate * 100) + "\n"
                "" + " " * 17 + "DISCOUNT AMOUNTS:   Rs " + str(round(total_price * var_discount_3_rate, 2)) + "\n" + " " * 17 + "_" * 35 + "\n"
                "" + " " * 17 + "TOTAL PRICES:       Rs " + str(round(total_price, 2)))
        elif total_price > var_discount_2: 
            total_price -= total_price * var_discount_2_rate 
            report_new += "\n" + " " * 17 + "-" * 35 + "\n" \
                "" + " " * 17 + "DISCOUNT RATES:      % " + str(var_discount_2_rate * 100) + "\n" \
                "" + " " * 17 + "DISCOUNT AMOUNTS:   Rs " + str(round(total_price * var_discount_2_rate, 2)) + "\n" + " " * 17 + "_" * 35 + "\n" \
                "" + " " * 17 + "TOTAL PRICES:       Rs " + str(round(total_price, 2)) + "\n" + " " * 17 + "*" * 35 
            print(" " * 17 + "-" * 35 + "\n"
                "" + " " * 17 + "DISCOUNT RATES:      % " + str(var_discount_2_rate * 100) + "\n"
                "" + " " * 17 + "DISCOUNT AMOUNTS:   Rs " + str(round(total_price * var_discount_2_rate, 2)) + "\n" + " " * 17 + "_" * 35 + "\n"
                "" + " " * 17 + "TOTAL PRICES:       Rs " + str(round(total_price, 2)))
        elif total_price > var_discount_1: 
            total_price -= total_price * var_discount_1_rate 
            report_new += "\n" + " " * 17 + "-" * 35 + "\n" \
                "" + " " * 17 + "DISCOUNT RATES:      % " + str(var_discount_1_rate * 100) + "\n" \
                "" + " " * 17 + "DISCOUNT AMOUNTS:   Rs " + str(round(total_price * var_discount_1_rate, 2)) + "\n" + " " * 17 + "_" * 35 + "\n" \
                "" + " " * 17 + "TOTAL PRICES:       Rs " + str(round(total_price, 2)) + "\n" + " " * 17 + "*" * 35 
            print(" " * 17 + "-" * 35 + "\n"
                "" + " " * 17 + "DISCOUNT RATES:      % " + str(var_discount_1_rate * 100) + "\n"
                "" + " " * 17 + "DISCOUNT AMOUNTS:   Rs " + str(round(total_price * var_discount_1_rate, 2)) + "\n" + " " * 17 + "_" * 35 + "\n"
                "" + " " * 17 + "TOTAL PRICES:       Rs " + str(round(total_price, 2)))
        else:
            report_new += "\n" + " " * 17 + "-" * 35 + "\n" + " " * 17 + "TOTAL PRICES:       Rs " + str(round(total_price, 2)) + "\n" + " " * 17 + "*" * 35
            print(" " * 17 + "_" * 35 + "\n" + " " * 17 + "TOTAL PRICES:       Rs " + str(round(total_price, 2)))

        print("\n (P) PAY           (M) MAIN MENU               (E) EXIT\n" + "_" * 72)
        input_1 = str(input("Please Select Your Operation: ")).upper()
        if (input_1 == 'P'):
            print("\n" * 1)
            print("Paid Successfully !")
            print("THANK YOU COME AGAIN !")
             
        elif (input_1 == 'M'):
            print("\n" * 1)
            def_main() 
            break
        
        elif ('E' in input_1) or ('e' in input_1):
            print("*" * 32 + "THANK YOU COME AGAIN" + "*" * 31 + "\n")
            break
        else:
            print("\n" * 1 + "ERROR: Invalid Input (" + str(input_1) + "). Something Went Wrong ,Try again!")



def_user() 
