import numpy as np
from scipy import stats

#is a test to check if 2 item are related or not
#use ScyPy library, and it is on top of Numpy which means it uses numpy array and functions



#A store sales many types of snacks , the owner wants to know if men and womem chose snacks in a different way
#It counts ho many men buy chips cookies and chocolate and how many women buy them
#Chi-square tells if the difference is real or if it just happened by chance
#p-value<0.05 = Real
#p-value>=0.05 = By Chance
table = np.array([[30,10],[20,40]])


chi2, p, dof, expected = stats.chi2_contingency(table)

#chi2 - how big is the difference between observed data and expected data
#p-probability like the difference to be random
#dof - grade de libertate = (randuri-1)*(coloane-1)
#expected - normal value if there would be no difference between gender

print("Chi square value: ", chi2)
print("p value: ", p)
print("Degrees of freedom : ", dof)
print("expected values: ", expected)


#Interpretation p<0.05 =>Diferenta este semnificatva. Genul influenteaza alegerea snackului