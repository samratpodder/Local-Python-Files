#Allergy Check
input_test = input("Enter food that you have eaten last 24 hours: ")
print("It is",'diary'.lower() in input_test.lower() ,"that",input_test,"contains diary")
print("It is",'nuts'.lower() in input_test.lower() ,"that",input_test,"contains nuts")
print("It is",'seafood'.upper() in input_test.upper() ,"that",input_test,"contains seafood")
print("It is",'chocolate'.lower() in input_test.lower() ,"that",input_test,"contains chocolate")