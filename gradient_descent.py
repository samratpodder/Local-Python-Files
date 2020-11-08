
ALPHA=0.001
def gradient_descent(X,Y,theta):
    """
    Linear Regression with  ONE variable
    The first parameter X is a list of values and second parameter Y is a list of predictions corresponding to Y. Third Parameter  Theta is the parameter which predicts Y for a given X.
    """
    prev=theta 
    curr=0
    while abs(prev-curr)>0.0000000000000000000000000000000000000000001:  #<-------This number cannot be smaller than alpha
        prev=theta #For this loop to work theta cannot be started with zero 0.
        theta = theta-ALPHA*(((theta*X)-Y)*X)
        curr=theta
        print(theta)
    return (theta)

if __name__ == "__main__":
    print("{0:.2f}".format(gradient_descent(5,18.2,1)))