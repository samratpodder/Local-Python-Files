import os
print("\nShowing Existing Environment Variables ---->\n")
print("Variable = Value")
for var in os.environ:
    print(f"{var} = {os.environ[var]}")
print(f"\nNow Showing PATH VARIABLES -------->\n")
for paths in os.environ["PATH"].split(";"):
    print(paths)
newpath = input("\nInput New Path to be added to be added as environment variable:\n")
name = input("Give a Name for the Path")
os.environ[name]=newpath