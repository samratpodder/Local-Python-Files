from math import exp,log

ALPHA = 0.001


def hypothesis(weights,featurex):
    """Let featurex be a measure or quantity that shows that by how much our example has a feature as compared to a proven example that has our correct prediction. for example, featurex is a quantity which shows by what degree our email is a spam as compared to an email which is already proven to be a spam."""
    z=(weights[0]+(weights[1]*featurex))
    g_of_z = 1/(1+exp(-z)) #we can do these with such simplicity because it is single variable regression
    # Activation Function
    if(g_of_z>=0.5):
        return (1,g_of_z)
    else:
        return (0,g_of_z)
def cost(weights,featurex,expeectation):
    if expeectation==1:
        return -log(hypothesis(weights,featurex),exp(1))
    if expeectation==0:
        return -log(1-hypothesis(weights,featurex),exp(1))
def adjustweights(weights,featurex,expectation):
    theta0 = 0
    theta1 = 0
    while(abs(weights[0]-theta0)>0.001 and abs(weights[1]-theta1)>0.001):
        theta0 = weights[0]
        theta1 = weights[1]
        # print(weights[0]-theta0)
        newhypo,__ = hypothesis(weights,featurex)
        weights[0] = weights[0] - (ALPHA* (newhypo-expectation))
        weights[1] = weights[1] - (ALPHA* ((newhypo-expectation)*featurex))
    return weights
def prediction(value):
    return (value==1)
if __name__ == "__main__":
    x=5
    y=1
    weights = [1,1]
    weights = adjustweights(weights=weights,featurex=x,expectation=y)


    print(weights)

    testfeature = int(input("Enter a feature to test: "))
    testresult = int(input("Enter expectation for the feature: "))
    result,prob = hypothesis(weights=weights,featurex=testfeature)
    print("we expect that according to data "+str(testfeature)+" the spam email classification would be "+str(prediction(result))+" with percentage probability "+str(prob*100)+" %")
