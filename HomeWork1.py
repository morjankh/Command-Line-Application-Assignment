def menu():

    threshold = 15
    while True:
        try:
            print("The available operations are:")
            print("1 - palindrome: check if the input is palindrome")
            print("2 - Lower: check if all characters in the input are lowercase")
            print("3 - Digit: check if all characters in the input are digits")
            print("4 - Long: check if the iput length is longer than 15 ")
            print("5 - Empty: check if the iput is empty")
            print("6 - Exit: Exit successfully from the application")
            choice = input("please enter the number of the operation you choose: ")
            if choice not in ['1', '2', '3', '4', '5', '6']:
               raise ValueError("Invalid choice, Please enter a number from 1 to 6")
            str_input = input("Enter an input:")

            if choice == '1':
                if str_input == str_input[::-1]:
                     print ("The answer is True")
                else:
                     print("The answer is False")    
                     
            elif choice =='2':
                islower= isLower(str_input)     
                if islower:
                     print ("The answer is True")
                else:
                     print("The answer is False")  

            elif choice =="3":  
                 if str_input.isdigit():
                      print ("The answer is True")
                 else:
                     print("The answer is False")  

            elif choice =="4":
                 if len(str_input) > threshold:
                      print("The answer is True")
                 else:    
                      print("The answer is False")  

            elif choice =="5":
                 if str_input=="":
                        print("The answer is True")
                 else:    
                      print("The answer is False")  

            elif choice =="6": 
                 print("Exit successfully") 
                 break   

        except ValueError as ve:
            print(f"ValueError: {ve}. Please try again.")

                                                              
def isLower(str_input):
    for c in str_input:
         if c.isupper():
              return False
    return True  
   
menu()    