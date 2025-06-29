
#create the input section and collect the number from the user
user_input= input ("enter a positive number:")
#check if the input from the user is a number and convert it afterwards

while True:
 if user_input.isdigit(): #check if the input contains a number or a digit 
        number= int(user_input) #convert the input to an integer
    
        if number > 0:
           break
        else:
            user_input=input ("the number must be a positive number. enter again:")
    
 else:    
          user_input=input("invalid input. Please enter a positive number: ")
 print ("Collatz sequence:")
 while number !=1:
     print (number, end= "-->")
     if number %2 ==0:
         number = number //2
     else:
             number = 3 * number + 1 