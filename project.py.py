import pandas as pd
HH={"Food Item":["Vada Pav","Pav Bhaji","Cheese Pav Bhaji","Delhi Chat",
                 "Aloo Paratha","Bread Pakode"," Chole Bhature",
                 " Masala Papad","Maharashtrian Thali","Masala Dosa",
                 " Pani Puri"," Sev Puri","Bhel Puri"," Kacchori","Masala chat"],
   "Price":[15,90,100,45,35,50,110,30,180,90,30,35,30,30,35]}
l1=[1001,1002,1003,1004,1005,1006,1007,1008,1009,1010,1011,1012,1013,1014,1015]
Hunger_Hackers=pd.DataFrame(HH,index=[l1])
Hunger_Hackers.to_csv('C:\\Users\\hp\\OneDrive\\Desktop\\hh.csv',mode='a',sep=",")

CP={"Food Item":["Fried Noodles","Hakka Noodles","Paneer Chopper Noodles"," Freid Rice",
                 "Schezwan Rice","Bombay Rice"," Hong Kong Rice"," Chilly Garlic Rice",
                 "Veg.Manchurian Dry","Veg.Manchurian Gravy","Paneer Dry","Paneer Gravy",
                 " Manchow Soup"," Schezwan Soup"," Manchurian Soup"],
    "Price":[150,160,170,180,150,155,170,185,180,200,190,210,200,200,140]}
l2=[2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015]
Chattar_Pattar=pd.DataFrame(CP,index=[l2])
Chattar_Pattar.to_csv('C:\\Users\\hp\\OneDrive\\Desktop\\cp.csv',mode='a',sep=",")

LPP={"Food Item":["Paneer Pizza","Italian Veg Pizza","Double Cheese Pizza",
                  "Veggies Mini Pizza","Fresh Veggies Pizza","Cheese Onion Pizza",
                  "Mushroom Pizza","Classic Pizza","Cheese Corn Pizza"," Mozerella Pizza",
                  "Tomato Baugette Pizza","Greek Style Pizza","Canadian Pizza",
                  "Tacoos Style Pizza","Spinach Pizza"],
     "Price":[150,160,170,180,150,155,170,185,180,200,190,210,200,200,140]}
l3=[3001,3002,3003,3004,3005,3006,3007,3008,3009,3010,3011,3012,3013,3014,3015]
La_Pinnoz_Pizza=pd.DataFrame(LPP,index=[l3])
La_Pinnoz.to_csv('C:\\Users\\hp\\OneDrive\\Desktop\\lp.csv',mode='a',sep=",")

BB={"Food Item":["Double Cheese Burger","Chilly Burger","Plain Burger","Vegetable Burger","Crunchy Burger",
                 "Mushroom Burger","Potato Corn Burger","Masala Burger","Cheese Corn Burger",
                 "Masala Corn Burger","Masala Cheese Burger","Paneer Tikka Burger",
                 "Mayo Cheese Burger","Schezwan Open Burger","Open Spicy Burger"],
    "Price":[140,100,70,75,80,90,90,80,80,75,85,95,110,115,180]}
l4=[4001,4002,4003,4004,4005,4006,4007,4008,4009,4010,4011,4012,4013,4014,4015]
Biggies_Burger=pd.DataFrame(BB,index=[l4])
Biggies_Burger.to_csv('C:\\Users\\hp\\OneDrive\\Desktop\\bb.csv',mode='a',sep=",")

SS={"Food Item":["Veg.Toast Sandwich"," Veg.Cheese Sandwich","Veg.Mini Cheese Grill Sandwich",
                 "Paneer Cheese Sandwich"," Onion Tamato Sandwich","Onion Capsi Sandwich",
                "Mayo Grilled Sandwich","Club Mayo SandWich","Pasta Cheese Sandwich",
                 "Paneer Corn Sandwich" ,"BBQ Paneer Sandwich","Pnr Cheese Sandwich",
                " Mashroom Sandwich","Club Sandwich","Onion Sandwich"],
    "Price":[40,50,50,70,65,65,80,90,90,95,90,85,90,75,90]}
l5=[5001,5002,5003,5004,5005,5006,5007,5008,5009,5010,5011,5012,5013,5014,5015]
Sandwich_Story=pd.DataFrame(SS,index=[l5])
Sandwich_Story.to_csv('C:\\Users\\hp\\OneDrive\\Desktop\\ss.csv',mode='a',sep=",")

KK={"Food Item":["Choco Nutty Ice Cream"," Choco Browne Ice Cream","Kesar Pista Ice Cream",
                "Btr Scotch Ice Cream","Strawberry Ice Cream","Mango Ice Cream",
                "Choco Truffle","Almond Mocha","Tripple Chocolate","Cookie Cream", 
                "Crunchy Chocobar","Choco Brownie Ice Cream","American Nuts Ice Cream",
                "Oreo Ice Cream","Purple Pico Ice Cream"],
    "Price":[45,55,45,55,45,65,65,75,75,65,65,55,65,75,80]}
l6=[6001,6002,6003,6004,6005,6006,6007,6008,6009,6010,6011,6012,6013,6014,6015]
Kream_Kulfi=pd.DataFrame(KK,index=[l6])
Kream_Kulfi.to_csv('C:\\Users\\hp\\OneDrive\\Desktop\\kk.csv',mode='a',sep=",")
while True: 
      print("1.Order")
      print("2.Manage")
      print("3.Help")
      print("4.Exit")
      choice=int(input("Choice: "))
#Module1
      if choice==1:
          print("ORDER: ")
          Name=input("Name: ")
          phoneno=int(input("Phone Number: "))
          email=input("Email Id: ")
          address=input("Residential Address: ")
          print()
          
          print("Franchisees:")
          print("1.Hunger Hackers") 
          print("2.Chattar Pattar")
          print("3.La Pinnoz Pizza")
          print("4.Biggies Burger")
          print("5.Sandwich Story")
          print("6.Kream Kulfi")
          choice=int(input("Choice:"))
          if choice==1:
                print("1.Hunger Hackers:") 
                Hunger_Hackers=pd.read_csv('C:\\Users\\hp\\OneDrive\\Desktop\\hh.csv',sep=",")
                print(Hunger_Hackers) 
          if choice==2:
                print("2.Chattar Pattar:")
                Chattar_Pattar=pd.read_csv('C:\\Users\\hp\\OneDrive\\Desktop\\cp.csv',sep=",")
                print(Chattar_Pattar)    
          if choice==3:
                print("3.La Pinnoz Pizza:")
                La_Pinnoz_Pizza=pd.read_csv('C:\\Users\\hp\\OneDrive\\Desktop\\lp.csv',sep=",")
                print(La_Pinnoz_Pizza)
          if choice==4:
                print("4.Biggies Burger:")
                Biggies_Burger=pd.read_csv('C:\\Users\\hp\\OneDrive\\Desktop\\bb.csv',,sep=",")
                print(Biggies_Burger)
          if choice==5:
                print("5.Sandwich Story:")
                Sandwich_Story=pd.read.csv('C:\\Users\\hp\\OneDrive\\Desktop\\ss.csv',sep=",")
                print(Sandwich_Story)
          if choice==6:
                print("6.Kream Kulfi:")
                Kream_Kulfi=pd.read_csv('C:\\Users\\hp\\OneDrive\\Desktop\\kk.csv',sep=",")
                print(Kream_Kulfi)
                
          if choice==1:
                 sum=0
                 dict={1001:15,1002:90,1003:100,1004:45,1005:35,1006:50,1007:110,
                         1008:30,1009:180,1010:90,1011:30,1012:35,1013:30,1014:30,1015:35}
                 dict1={1001:"Vada Pav",1002:"Pav Bhaji",1003:"Cheese Pav Bhaji",1004:"Delhi Chat",
                 1005:"Aloo Paratha",1006:"Bread Pakode",1007:" Chole Bhature",
                 1008:" Masala Papad",1009:"Maharashtrian Thali",1010:"Masala Dosa",
                  1011:"Pani Puri",1012:"Sev Puri",1013:"Bhel Puri",1014:" Kacchori",1015:"Masala chat"}
                 
          if choice==2:
                 sum=0
                 dict={2001:150,2002:160,2003:170,2004:180,2005:150,2006:155,2007:170,
                       2008:185,2009:180,2010:200,2011:190,2012:210,2013:200,2014:200,2015:140}
                 dict1={1001:"Fried Noodles",1002:"Hakka Noodles",1003:"Paneer Chopper Noodles",
                        1004:" Freid Rice",1005:"Schezwan Rice",1006:"Bombay Rice",
                        1007:" Hong Kong Rice",1008:" Chilly Garlic Rice",1009:"Veg.Manchurian Dry",
                        1010:"Veg.Manchurian Gravy",1011:"Paneer Dry",1012:"Paneer Gravy",
                        1013:" Manchow Soup",1014:" Schezwan Soup",1015:" Manchurian Soup"}
                                  
          if choice==3:
                 sum=0
                 dict={3001:150,3002:160,3003:170,3004:180,3005:150,3006:155,3007:170,3008:185,
                       3009:180,3010:200,3011:190,3012:210,3013:200,3014:200,3015:140}
                 dict1={3001:"Paneer Pizza",3002:"Italian Veg Pizza",3003:"Double Cheese Pizza",
                  3004:"Veggies Mini Pizza",3005:"Fresh Veggies Pizza",3006:"Cheese Onion Pizza",
                  3007:"Mushroom Pizza",3008:"Classic Pizza",3009:"Cheese Corn Pizza",
                  3010:" Mozerella Pizza",3011:"Tomato Baugette Pizza",3012:"Greek Style Pizza",
                  3013:"Canadian Pizza",3014:"Tacoos Style Pizza",3015:"Spinach Pizza"}
            
          if choice==4:
                 sum=0
                 dict={4001:140,4002:100,4003:70,4004:75,4005:80,4006:90,4007:90,4008:80,
                       4009:80,4010:75,4011:85,4012:95,4013:110,4014:115,4015:180}
                 dict1={4001:"Double Cheese Burger",4002:"Chilly Burger",4003:"Plain Burger",
                        4004:"Vegetable Burger",4005:"Crunchy Burger",4006:"Mushroom Burger",
                        4007:"Potato Corn Burger",4008:"Masala Burger",4009:"Cheese Corn Burger",
                        4010:"Masala Corn Burger",4011:"Masala Cheese Burger",4012:"Paneer Tikka Burger",
                        4013:"Mayo Cheese Burger",4014:"Schezwan Open Burger",4015:"Open Spicy Burger"}
             
          if choice==5:
                 sum=0
                 dict={5001:40,5002:50,5003:50,5004:70,5005:65,5006:65,5007:80,5008:90,
                       5009:90,5010:95,5011:90,5012:85,5013:90,5014:75,5015:90}
                 dict1={5001:"Veg.Toast Sandwich",5002:" Veg.Cheese Sandwich",5003:"Veg.Mini Cheese Grill Sandwich",
                        5004:"Paneer Cheese Sandwich",5005:" Onion Tamato Sandwich",5006:"Onion Capsi Sandwich",
                        5007:"Mayo Grilled Sandwich",5008:"Club Mayo SandWich",5009:"Pasta Cheese Sandwich",
                        5010:"Paneer Corn Sandwich" ,5011:"BBQ Paneer Sandwich",5012:"Pnr Cheese Sandwich",
                        5013:" Mashroom Sandwich",5014:"Club Sandwich",5015:"Onion Sandwich"}
             
          if choice==6:
                 sum=0
                 dict={6001:45,6002:55,6003:45,6004:55,6005:45,6006:65,6007:65,6008:75,
                       6009:75,6010:65,6011:65,6012:55,6013:65,6014:75,6015:80}
                 dict1={6001:"Choco Nutty Ice Cream",6002:" Choco Browne Ice Cream",6003:"Kesar Pista Ice Cream",
                        6004:"Btr Scotch Ice Cream",6005:"Strawberry Ice Cream",6006:"Mango Ice Cream",
                        6007:"Choco Truffle",6008:"Almond Mocha",6009:"Tripple Chocolate",6010:"Cookie Cream", 
                        6011:"Crunchy Chocobar",6012:"Choco Brownie Ice Cream",6013:"American Nuts Ice Cream",
                        6014:"Oreo Ice Cream",6015:"Purple Pico Ice Cream"}
          while True: 
                 order=int(input(" Order:"))
                 quantity=int(input(" Plates:"))
                 print("0 if Ordered")
                 if order in dict:
                    sum=sum+dict[order]*quantity
                    order=pd.DataFrame({
                        'Name':[Name],
                        'Phone Number':[phoneno],
                        'Email Id':[email],
                        'Residential_Address':[address],
                        'Order':[dict1[order]],
                        'Plates':[quantity],
                        'Bill':[sum]
                         })
                    order.to_csv('C:\\Users\\hp\\OneDrive\\Desktop\\order.csv',mode='a',
                                 index=False,header=0,sep=",")
                 elif order==0:
                     order=pd.read_csv('C:\\Users\\hp\\OneDrive\\Desktop\\order.csv',sep=",")
                     order=order[order['Name']==Name]
                     order=order[['Order','Plate']]
                     print(order,ignore_index=True)
                     print("Total Bill:",sum) 
                     print(Name,"your order on the way!")
                     print("Contact for Help: 9876543210")
                     break
                 else:
                    print("Enter Correctly") 
                    break
    
#Module2
      elif choice==2:
          print("MANAGE: ")
          pswrd=str(input("Enter Password: "))
          if pswrd=='FoodLove':
              print("Manage Your Franchisees and Menus!")
              print("1.Adding Food Items!")
              print("2.Remove Food item!")
              print("3.Customer Information!")
              choice=int(input())
              print()
              print("1.Hunger Hackers:") 
              print("2.Chattar Pattar:")     
              print("3.La Pinnoz Pizza:")
              print("4.Biggies Burger:")
              print("5.Sandwich Story:")
              print("6.Kream Kulfi:")
              print("Add New Food Items")
              if choice==1:
                 choice=int(input("Choice: "))
                 if choice==1:
                  print(Hunger_Hackers) 
                  index=input("Food Code: ")
                  fooditem=input("Food Item: ")
                  price=input("Price : ")
                  dict={"Food Item":[fooditem],
                        "Price":[price]}
                  df1=pd.DataFrame(dict,index=[index])
                  Hunger_Hackers=Hunger_Hackers.append(df1)
                  Hunger_Hackers.to_csv('C:\\Users\\hp\\OneDrive\\Desktop\\hh.csv',mode='a',sep=",")                 
                
                  
            
                 elif choice==2:
                  print(Chattar_Pattar)
                  index=input("Food Code: ")
                  fooditem=input("Food Item: ")
                  price=input("Price : ")
                  dict={"Food Item":[fooditem],
                        "Price":[price]}
                  df1=pd.DataFrame(dict,index=[index])
                  Chattar_Pattar=Chattar_Pattar.append(df1)
                  Chattar_Pattar.to_csv('C:\\Users\\hp\\OneDrive\\Desktop\\cp.csv',mode='a',sep=",")
                 
                  
                 elif choice==3:
                  print(La_Pinnoz_Pizza)
                  index=input("Food Code: ")
                  fooditem=input("Food Item: ")
                  price=input("Price : ")
                  dict={"Food Item":[fooditem],
                        "Price":[price]}
                  df1=pd.DataFrame(dict,index=[index])
                  La_Pinnoz_Pizza=La_Pinnoz_Pizza.append(df1)
                  La_Pinnoz.to_csv('C:\\Users\\hp\\OneDrive\\Desktop\\lp.csv',mode='a',sep=",")
                  
            
                 elif choice==4:
                  print(Biggies_Burger)
                  index=input("Food Code: ")
                  fooditem=input("Food Item: ")
                  price=input("Price : ")
                  dict={"Food Item":[fooditem],
                        "Price":[price]}
                  df1=pd.DataFrame(dict,index=[index])
                  Biggies_Burger=Biggies_Burger.append(df1)
                  Biggies_Burger.to_csv('C:\\Users\\hp\\OneDrive\\Desktop\\bb.csv',mode='a',sep=",")
                  
            
                 elif choice==5:
                  print(Sandwich_Story)
                  index=input("Food Code: ")
                  fooditem=input("Food Item: ")
                  price=input("Price : ")
                  dict={"Food Item":[fooditem],
                        "Price":[price]}
                  df1=pd.DataFrame(dict,index=[index])
                  Sandwich_Story=Sandwich_Story.append(df1)
                  Sandwich_Story.to_csv('C:\\Users\\hp\\OneDrive\\Desktop\\ss.csv',mode='a',sep=",")
                  
            
                 elif choice==6:
                  print(Kream_Kulfi) 
                  index=input("Food Code: ")
                  fooditem=input("Food Item: ")
                  price=input("Price : ")
                  dict={"Food Item":[fooditem],
                        "Price":[price]}
                  df1=pd.DataFrame(dict,index=[index])
                  Kream_Kulfi=Kream_Kulfi.append(df1)
                  Kream_Kulfi.to_csv('C:\\Users\\hp\\OneDrive\\Desktop\\kk.csv',mode='a',sep=",")
                  
                 else:
                  print("No Franchisee for your entered choice!")
                  
              elif choice==2:
                 choice=int(input("Choice: "))
                 if choice==1:
                  print(Hunger_Hackers) 
                  index=input("Food Code: ")
                  fooditem=input("Food Item: ")
                  price=input("Price : ")
                  dict={"Food Item":[fooditem],
                        "Price":[price]}
                  df1=pd.DataFrame(dict,index=[index])
                  Hunger_Hackers=Hunger_Hackers.remove(df1)
                  Hunger_Hackers.to_csv('C:\\Users\\hp\\OneDrive\\Desktop\\hh.csv',mode='a',sep=",") 
              
                  
            
                 elif choice==2:
                  print(Chattar_Pattar)
                  index=input("Food Code: ")
                  fooditem=input("Food Item: ")
                  price=input("Price : ")
                  dict={"Food Item":[fooditem],
                        "Price":[price]}
                  df1=pd.DataFrame(dict,index=[index])
                  Chattar_Pattar=Chattar_Pattar.remove(df1)
                  Chattar_Pattar.to_csv('C:\\Users\\hp\\OneDrive\\Desktop\\cp.csv',mode='a',sep=",")
                 
                  
                 elif choice==3:
                  print(La_Pinnoz_Pizza)
                  index=input("Food Code: ")
                  fooditem=input("Food Item: ")
                  price=input("Price : ")
                  dict={"Food Item":[fooditem],
                        "Price":[price]}
                  df1=pd.DataFrame(dict,index=[index])
                  La_Pinnoz_Pizza=La_Pinnoz_Pizza.remove(df1)
                  La_Pinnoz.to_csv('C:\\Users\\hp\\OneDrive\\Desktop\\lp.csv',mode='a',sep=",")
              
            
                 elif choice==4:
                  print(Biggies_Burger)
                  index=input("Food Code: ")
                  fooditem=input("Food Item: ")
                  price=input("Price : ")
                  dict={"Food Item":[fooditem],
                        "Price":[price]}
                  df1=pd.DataFrame(dict,index=[index])
                  Biggies_Burger=Biggies_Burger.remove(df1)
                  Biggies_Burger.to_csv('C:\\Users\\hp\\OneDrive\\Desktop\\bb.csv',mode='a',sep=",")
                  
            
                 elif choice==5:
                  print(Sandwich_Story)
                  index=input("Food Code: ")
                  fooditem=input("Food Item: ")
                  price=input("Price : ")
                  dict={"Food Item":[fooditem],
                        "Price":[price]}
                  df1=pd.DataFrame(dict,index=[index])
                  Sandwich_Story=Sandwich_Story.remove(df1)
                  Sandwich_Story.to_csv('C:\\Users\\hp\\OneDrive\\Desktop\\ss.csv',mode='a',sep=",")
               
            
                 elif choice==6:
                  print(Kream_Kulfi) 
                  index=input("Food Code: ")
                  fooditem=input("Food Item: ")
                  price=input("Price : ")
                  dict={"Food Item":[fooditem],
                        "Price":[price]}
                  df1=pd.DataFrame(dict,index=[index])
                  Kream_Kulfi=Kream_Kulfi.remove(df1)
                  Kream_Kulfi.to_csv('C:\\Users\\hp\\OneDrive\\Desktop\\kk.csv',mode='a',sep=",")
                
                 else:
                  print("No Franchisee for your entered choice!")
                  
              elif choice==3:
                  order=pd.read_csv('C:\\Users\\hp\\OneDrive\\Desktop\\order.csv',sep=",")
                  print(order)
              else:
                  print("Incorrect choice")
        
#Module3
      elif choice==3:
          print("HELP DESK: ")
          print("1.Unable to Order Food")
          print("2.Delay Of Order")
          print("3.Cancellation Of Orders")
          print("4.Forgot Password")
          print("5.Other Problems")
          choice=int(input("Choice: "))
          if choice==1:
              print("UNABLE TO ORDER:")
              print("Please try with another Name /Phone number/Email")
              print("Contact for Help: 9876543210")
              print("Email for Queries: foodordermanagement@yahoo.com")
          elif choice==2:
              print("DELAY OF ORDER:")
              print("Your order must have stuck somewhere it may be while ordering or delivering your food.")
              print("Wait for a while")
              print("Contact for Help: 9876543210")
              print("Email for Queries: foodordermanagement@yahoo.com")
          elif choice==3:
              print("CANCELLATION OF ORDER: ")
              print("You cannot cancel your order after 30 minutes",
                    ",as it is already unpacked and you may get delivery any time")
              print("If you have ordered few minutes ago your order may be cancelled", 
                    "if we get your honest respond")
              print("Contact for Help: 9876543210")
              print("Email for Queries: foodordermanagement@yahoo.com")
          elif choice==4:
              print("FORGOT PASSWORD: ")
              print("You cannot access manage option if your an user. ")
              print("If your the manager please mail ")
              print("Contact for Help: 9876543210")
              print("Email for Queries: foodordermanagement@yahoo.com")
          elif choice==5:
              print("OTHER PROBLEM: ")
              print("Contact for Help: 9876543210")
              print("Email for Queries: foodordermanagement@yahoo.com")
        
#Module4
      elif choice==4:
          print("EXIT: ")
          print("Visit Again!!!")
          break
        
      else:
          ("Enter Choice Correctly!")
          break
        
        
    

        