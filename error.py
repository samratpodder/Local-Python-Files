x=420
y=0
print
try:
    print(x/y)  
except ZeroDivisionError as e:
    print("Divide by zero")
else:
    print("Something else went wrong")
finally:
    print("Cleanup Code Here")