# -*- coding: utf-8 -*-
"""RealniGA.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Smy0OdiHUz-BT2EWLLGbG0NovNsvgwsu

## Realni Genetski Algoritam ##




*   Realni genetski algoritam
*   Ruletska selekcija
*   Simetrično ukrštanje
*   Primeri: sferna i Levijeva funkcija

**Postupak genetskog algoritma:** </br>
START
<br>
Inicijalizacija početne populacije
<br>
Računanje funkcije prilagođenosti
<br>
Ponavljati: <br>

*   Selekciju
*   Ukrštanje
*   Mutaciju
*   Računanje funkcije prilagođenosti

DOK populacija ne iskonvergira <br>
STOP<br>

# 1. Biblioteke

Prvo je nophodno učitati python biblioteke
"""

# Commented out IPython magic to ensure Python compatibility.
# %matplotlib inline

import random
import numpy as np
import matplotlib.pyplot as plt
import math

from mpl_toolkits import mplot3d

pi = 3.1415

"""# 2. Generisanje populacije

**Početna populacija** 

GA započinjemo kreiranjem skupa jedinki koji se naziva populacijom. Svaka jedinka predstavlja potencijalno rešenje.
"""

def generate_inital_chromosomes(length, max, min, pop_size):
  return [ [random.uniform(min,max) for j in range(length)] for i in range(pop_size)]

def population_stats(costs):
  return costs[0], sum(costs)/len(costs)

"""# 3. Funkcije za rangiranje i **selekciju** jedinki

Jedinke se rangiraju (sortiraju) po vrednosti funkcije prilagođenosti funkcijom **rank_chromosomes**.</br>
Implementirane su sledece vrste selekcija: prirodna i ruletska selekcija. </br>
Prirodna selekcija je implementirana u  funkciji **natural_selection**, pri čemu ostavljamo samo prvih *n_keep* jedinki.</br>
Funkcija **roulette_selection** predstavlja ruletski tip selekcije.
"""

def rank_chromosomes(cost, chromosomes):
  costs = list(map(cost, chromosomes))
  ranked  = sorted( list(zip(chromosomes,costs)), key = lambda c:c[1])
  
  return list(zip(*ranked))

def natural_selection(chromosomes, n_keep):
  return chromosomes[:n_keep]

def roulette_selection(parents):

  pairs = []
  i = 0
  for i in range(0, len(parents), 2):

    weights=[];
    for i in range(len(parents)):
        weights.append((len(parents)-i)*random.random()) #za minimum
      #  weights.append((i+1)*random.random()) #za maksimum
    if (weights[0]>=weights[1]):
        maxInd1=0;
        maxInd2=1;
    else:
        maxInd1=1;
        maxInd2=0;
    
    for i in range(2,len(parents)):
        if weights[i]>weights[maxInd1]:
            maxInd2=maxInd1
            maxInd1=i
        elif weights[i]>weights[maxInd2]:
            maxInd2=1
    pairs.append([parents[maxInd1], parents[maxInd2]])
      
  return pairs

"""# 4. Ukrštanje
a, b - roditelji </br>
y1, y2 - potomci </br>
(a, b) -> (y1, y2) </br>
**Simetrično ukrštanje** </br>
y1 = r * a + (1 - r) * b</br>
y2 = (1 - r) * a + r * b,</br>
gde je r slučanjo odabrani broj u intervalu (0, 1).
"""

def crossover(pairs):

  children = []
  
  for a,b in pairs:

    r=random.random()
    y1=[]
    y2=[]
    for i in range(0,len(a)):
      y1.append(r * a[i] + (1 - r) * b[i])
      y2.append((1 - r) *  a[i] + r*b[i])
    children.append(y1)
    children.append(y2)
      
  
  return children

crossover([[[-0.5, -0.5], [-7.04, -2.5]],[[-1.5, -1.05], [-9.04, -9.5]]])

"""# 5. Mutacija

Mutacija predstavlja slučajnu promenu nekih gena određene jedinke. Kako deluje nad samo jednom jedinkom, mutacija je unarni operator koji kao rezultat daje izmenjenu jedinku. Mutacija se na svaku jedinku primenjuje sa nekom malom verovatnoćom. Ukoliko je verovatnoća mutacije premala, ili se uopšte ne primenjuje, može doći do preuranjene lokalne konvergencije. Ako je vrednost verovatnoće mutacije velika, genetski algoritam će se svesti na slučajnu pretragu što nema smisla.
"""

def mutation(chromosomes, mutation_rate,mutation_width):
  mutated_chromosomes = [] 
  for chromosome in chromosomes: 
    y1=[]
    for i in range(0,len(chromosome)):
      if random.random() < mutation_rate:
        r=random.random()  
            
        y1.append( chromosome[i] + mutation_width * 2 * (r - 0.5) )        
      else:
        y1.append(chromosome[i])
      
    mutated_chromosomes.append(y1)
  return mutated_chromosomes

mutation([[-0.23170627655571208, 2.8058402091757224], [-2.538231077587461, 0.14136977843141585]], 0.3,1)

"""# 6. Elitizam

Postoji mogućnost da se dobro rešenje dobijeno nakon mnogo iteracija izgubi zbog genetskih operatora mutacije ili selekcije. Zbog toga se javlja potreba da se najbolje jedinke zaštite od izmene ili eliminacije tokom evolutivnog procesa. Takav mehanizam se naziva **elitizam**. 
"""

def elitis(chromosomes_old,chromosomes_new, elitis_rate, population_size):
 
  old_ind_size=int(np.round(population_size*elitis_rate))
  return chromosomes_old[:old_ind_size]+chromosomes_new[:(population_size-old_ind_size)]

"""# 7. Definicija  funkcije

Definisaćemo funkciju kojoj tražimo optimum (minimum). 

##  Primer 1: Sfera funkcija 

Kao prvi primer koristićemo sfernu funkciju koja se definiše na sledeći način


\begin{equation}
f(x, y) = x^2 +y ^2 \\
\mbox{interval: }  -10 < x, y < 10,\\
\mbox{minimum: } f(0,0) = 0 
\end{equation}

##  Primer 2: Levijeva funkcija 
Kao drugi primer koristićemo Levijevu funkciju koja se definiše na sledeći način


\begin{equation}
f(x, y) = sin^2 3πx + (x − 1)^2(1 + sin^2 3πy) + (y − 1)^2(1 + sin^2 2πy) \\
 \mbox{interval: } -10 < x, y < 10,\\
  \mbox{minimum: } f(1,1) = 0 
\end{equation}
"""

def sphera_function(chromosome):
  x = chromosome[0]
  y = chromosome[1] 
  
  tmp1 = math.pow(x, 2)
  tmp2 = math.pow(y, 2)


  return tmp1 + tmp2

def levy_function(chromosome):
  sum = 0
  sum1 = 0
  sum2 = 0
  
  for i in range(len(chromosome)):
    sum1+=chromosome[i]**2
    sum2+=chromosome[1]/2
  
  sum = sum1 + sum2**2 + sum2**4
  return sum

"""# 7.1. 3D Prikaz funkcije"""

def l_show(x, y):
  tmp1 = math.pow(math.sin(3*pi*x), 2)
  tmp2 = math.pow((x - 1), 2) * (1 + math.pow(math.sin(3*pi*y), 2))
  tmp3 = math.pow((y - 1), 2) * (1 + math.pow(math.sin(2*pi*y), 2))

  return tmp1 + tmp2 + tmp3

levy_vectorized = np.vectorize(l_show)

x = np.linspace(-13, 13, 30)
y = np.linspace(-13, 13, 30)

X, Y = np.meshgrid(x, y)
Z = levy_vectorized(X, Y)

ax = plt.axes(projection='3d')
ax.plot_surface(X, Y, Z, rstride=1, cstride=1,
                cmap='plasma', edgecolor='none')
ax.set_title('Levijeva funkcija');

ax.view_init(50, 35)

"""# 8. Main loop - sklopljen genetski algoritam
- Generišemo početnu populaciju veličine *population_size* 
- Vrtimo glavnu petlju maksimalno *max_iter* puta, pri čemu svaka iteracija petlje predstavlja jednu generaciju
- Rangiramo jedinke po prilagođenosti, funkcijom **rank_chromosomes**

- Funkcijom **roulette_selection** odvajamo parove roditeljskih hromozoma koje ćemo ukrstiti
- Metodom *ukrštanja*, tj funkcijom **crossover** uparujemo roditeljske hromozome i dobijemo populaciju dece
- Spajamo novonastale hromozome sa roditeljskim u novu populaciju *chromosomes* 
- Na ovoj populaciji vršimo * mutaciju* funkcijom **mutation** sa zadatim *mutation_rate = 0.3*

- Proveravamo da li populacija konvergira ili da li smo došli do optimalnog rešenja
- Ispisujemo statistike za svaku generaciju: prosečna prilagođenost, najbolji hromozom i sastav najboljeg hromozoma
"""

def genetic(cost_func , extent, population_size, mutation_rate = 0.1,elitis_rate=0.3, chromosome_length = 5, precision = 8, max_iter = 100):

  min_val = extent[0]
  max_val = extent[1]

  
  avg_list = []
  best_list = []
  curr_best = 10000
  same_best_count = 0



  
  chromosomes = generate_inital_chromosomes(chromosome_length, max_val, min_val, population_size)

  for iter in range(max_iter):
      
    ranked_parents, costs = rank_chromosomes(cost_func, chromosomes)     
    best, average = population_stats(costs)
    parents = natural_selection(ranked_parents, population_size) 

 

    pairs = roulette_selection (parents)  
        
    children = crossover(pairs)   
    print(children)   
    chromosomes = mutation(children, mutation_rate,1)


    ranked_children, costs = rank_chromosomes(cost_func, chromosomes)
    chromosomes=elitis(ranked_parents,ranked_children, elitis_rate, population_size)
    print("Generation: ",iter+1," Average: {:.3f}".format(average)," Curr best: {:.3f}".format(best), 
         "[X, Y, Z, E, F] = {:.3f} {:.3f} {:.3f} {:.3f} {:.3f}".format(chromosomes[0][0],chromosomes[0][1],chromosomes[0][2],chromosomes[0][3],chromosomes[0][4]))
    print("-------------------------")
    
    avg_list.append(average)
    if best < curr_best:
      best_list.append(best)
      curr_best = best
      same_best_count = 0
    else:
      same_best_count += 1
      best_list.append(best)
      
    ##
    if (cost_func(chromosomes[0]) < 0.005):
      
      avg_list = avg_list[:iter]
      best_list = best_list[:iter]
      all_avg_list.append(avg_list)
      all_best_list.append(best_list)
      generations_list.append(iter)
     
      print("\nSolution found ! Chromosome content: [X, Y, Z, E, F] = {:.3f} {:.3f} {:.3f} {:.3f} {:.3f}\n".format(chromosomes[0][0],chromosomes[0][1],chromosomes[0][2],chromosomes[0][3],chromosomes[0][4]))
      return
        
    if same_best_count > 20:
      print("\nStopped due to convergance.Best chromosome [X, Y, Z, E, F] = {:.3f} {:.3f} {:.3f} {:.3f} {:.3f}\n".format(chromosomes[0][0],chromosomes[0][1],chromosomes[0][2],chromosomes[0][3],chromosomes[0][4]))
      
      avg_list = avg_list[:iter]
      best_list = best_list[:iter]
      all_avg_list.append(avg_list)
      all_best_list.append(best_list)
      generations_list.append(iter)
      
      return
    
    if iter == 499:
      avg_list = avg_list[:iter]
      best_list = best_list[:iter]
      all_avg_list.append(avg_list)
      all_best_list.append(best_list)
      generations_list.append(iter)
      
      print("\nStopped due to max number of iterations, solution not found. Best chromosome [X, Y] = {:.3f} {:.3f} {:.3f} {:.3f} {:.3f}\n".format(chromosomes[0][0],chromosomes[0][1],chromosomes[0][2],chromosomes[0][3],chromosomes[0][4]))

all_avg_list = []
generations_list = []
all_best_list = []
# genetic(sphera_function, [-10, 10], 50)

"""# 9. Iscrtavanje grafikona</br>

Iscrtavamo prosečnu i najbolji prilagođenost za svaku generaciju.
"""

def display_stats(all_avg_list, all_best_list, generations_list):
  
  c = 0
  colors = ['red', 'green', 'blue', 'yellow', 'orange']
  
  for average_list in all_avg_list:
      x_axis = list(range(generations_list[c]))
      y_axis = average_list
      plt.plot(x_axis, y_axis, linewidth=3, color=colors[c], label=str(c + 1))
      plt.title('Average cost function value', fontsize=19)
      plt.xlabel('Generation', fontsize=10)
      plt.ylabel('Cost function')
      c += 1
  plt.legend(loc='upper right')
  plt.show()

  c = 0

  for best_list in all_best_list:
      x_axis = list(range(generations_list[c]))
      y_axis = best_list
      plt.plot(x_axis, y_axis, color=colors[c], label=str(c + 1))
      plt.title('Best cost function value', fontsize=19)
      plt.xlabel('Generation')
      plt.ylabel('Cost function')
      c += 1
  plt.legend(loc='upper right')
  plt.show()

"""# 10. Konfigurisanje i poziv genetskog algoritma

Argumenti funkcije:


1.   Funkcija za minimizaciju (u našem slučaju Levy_function) - *function*
2.   Opseg u kome pretražujemo rešenje - *list*
3.   Broj hromozoma (jedinki) - *int*


---

Opcioni argumenti:


4.   Stopa mutacije - *float*
5.   Stopa elitizma - *float*
7.   Maksimalni broj iteracija - *int*

"""

# number_of_chromosomes = [20, 100, 150]
all_avg_list = []
generations_list = []
all_best_list = []
run_number = 5

  
print("==========================")
  
for k in range(0, run_number):
     
  genetic(levy_function, [5, -5], 100)
    
  display_stats(all_avg_list, all_best_list, generations_list)
  all_best_list = []
  all_avg_list = []
  generations_list = []

 