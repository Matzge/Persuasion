#!/usr/bin/python3
"""
Finding optimal precision of Signal given some posterior threshold
"""
import matplotlib.pyplot as plt
list_precision = []
list_posteriors = []
prior = int(input("Enter the Prior: "))


def find_precision(prior, posterior):
    """
    This function calculates optimal precision given a target posterior.
    """
    if posterior < prior:
        raise Exception("Your Posterior should be higher than your prior")
    else:
        precision = ((prior / posterior) - prior ) / (1-prior)     
        precision = 1-precision             
    return(precision)             

    
    
for posterior in range (prior, 101):
    list_posteriors.append((posterior)/100)
    precision = find_precision(prior/100, posterior/100)
    list_precision.append(precision)

print(list_precision)
plt.plot(list_posteriors,list_precision)
plt.xlabel("Posterior")
plt.ylabel("Required Precision")
plt.title("Precision as a Function of a Target Posterior")
plt.show()
print(find_precision(0.8,0.5))
