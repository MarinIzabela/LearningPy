import numpy as np

#Gauss/Clopotul lui Gauss
normal_data=np.random.normal(loc=50, scale =10, size=5) #loc = media distr(centru), scale(abaterea standard-cat se imprastie valorile), size=cate val generezi
print("Normal data distribution: ", normal_data)

#numarul de succesuri in n incercari independente.
#am 10 incercari, probabilitatea de succes 0.5.
#returneaza cate reusite ai obtinut din cele 10.(ex:cati clienti cumpara ceva din cei10)
binomial_data=np.random.binomial(10, 0.5, size=5)
print("Binomial data distribution: ", binomial_data)



#orice numar intre 1 si 10are sanse egale sa apara(ex:loterie)
uniform_data=np.random.uniform(low=1, high=10, size=5)
print("Uniform data distribution: ", uniform_data)


#modeleaza timpul pana se intampla un eveniment. Scale=media timpului intre evenimente
#Ex: cat dureaza pana vine urm autobuz, timpul de viata al unui bec, frecventa utilizatorilor pe un server
Exponential_data=np.random.exponential(scale=2, size=5)
print("Exponential data distribution: ", Exponential_data)

#Modeleaza valori care cresc rapid dar au limite superioare si inferioare in probabilitate
#datele extreme sunt mai probabile
#loc = centrul, punctul de echilibru
#scale(dispersia) cat de puternic fluctueaza schimbarea
#ex: probabilitati in regresie logistica(Machine Learning), studii sociale(probabilitatea unei alegeri(DA/NU)), biologie ->creseterea populatiei pana la un plafon
logistic_data=np.random.logistic(loc=0, scale=1, size=5)
print("Logistic data distribution: ", logistic_data)


# Normală->Ce este cel mai comun?
#Binomială->De câte ori reușim într-un număr de încercări?
#Exponențială->Cât timp trece până la următorul eveniment?
#Logistică->Cum evoluează ceva rapid, dar cu o limită firească?
#Uniformă->Ce se întâmplă când totul e perfect aleator?
#