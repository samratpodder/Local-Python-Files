# yell_this() yells the string Argument provided
def yell_this(phrase):
    print(phrase.upper() + "!")
    
# call function with a string
yell_this("It is time to save the notebook")
# use a default argument
def say_this(phrase = "Hi"):  
    print(phrase)
        
say_this()
say_this("Bye")