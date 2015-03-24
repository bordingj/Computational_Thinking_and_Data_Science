# 6.00.2x Problem Set 4

import numpy
import random
import pylab
from ps3b import *

#
# PROBLEM 1
#        
def simulationDelayedTreatment(numTrials):
    """
    Runs simulations and make histograms for problem 1.
 
    Runs numTrials simulations to show the relationship between delayed
    treatment and patient outcome using a histogram.
 
    Histograms of final total virus populations are displayed for delays of 300,
    150, 75, 0 timesteps (followed by an additional 150 timesteps of
    simulation).
 
    numTrials: number of simulation runs to execute (an integer)
    """
 
    maxPop = 1000
    maxBirthProb = 0.1
    clearProb = 0.05
    resistances = {'guttagonol': True}
    mutProb = 0.005
    numViruses = 100
 
    steps1 = 150 # 300, 150, 75, 0
    steps2 = 150
    viruses = []
    for v in range(numViruses):
        viruses.append(ResistantVirus(maxBirthProb, clearProb, resistances, mutProb))
    pop = []
    for i in range(numTrials):
        pat = TreatedPatient(viruses, maxPop)
        for t in range(steps1):
            viruspop = pat.update()
        pat.addPrescription('guttagonol')
        for t in range(steps2):
            viruspop = pat.update()
        pop.append(viruspop)
    pylab.hist(pop,numTrials)
    pylab.title('Effects of Delayed Treatment' )
    pylab.xlabel('Virus Population')
    pylab.ylabel('numTrials')
    pylab.show()






#
 
#
# PROBLEM 2
#
def simulationTwoDrugsDelayedTreatment(numTrials):
    """
   Runs simulations and make histograms for problem 2.
 
   Runs numTrials simulations to show the relationship between administration
   of multiple drugs and patient outcome.
 
   Histograms of final total virus populations are displayed for lag times of
   300, 150, 75, 0 timesteps between adding drugs (followed by an additional
   150 timesteps of simulation).
 
   numTrials: number of simulation runs to execute (an integer)
   """
    results = []
    for l in lags:
        #Uncomment these to use the red module
        #\/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/
#        r = red.update(num_viruses, max_pop, max_birth_prob, clear_prob,
#                       resistances, mut_prob, initial_steps + l + final_steps,
#                       [(initial_steps, 'guttagonol') ,
#                        (initial_steps + l, 'grimpex')], numTrials, 4)
#        results.append(r)
        #/\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\
        #Uncomment these out to use the red module
       
        #Comment these out to use the red module
        #\/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/
        partial_result = []
        for t in range(numTrials):
            viruses = [ResistantVirus(max_birth_prob, clear_prob,
                                      resistances, mut_prob)] * num_viruses
            tp = TreatedPatient(viruses, max_pop)
            for step in range(initial_steps + l + final_steps):
                if step == initial_steps:
                    tp.addPrescription('guttagonol')
                if step == initial_steps + l:
                    tp.addPrescription('grimpex')
                tp.update()
            print('Lag: ' + str(l) + '  Trial: ' + str(t))
            partial_result.append(tp.getTotalPop())
        results.append(partial_result)
        #/\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\
        #Comment these out to use the red module
   
    subplot = 221
    pylab.figure(simulationTwoDrugsDelayedTreatment.figure)
    simulationTwoDrugsDelayedTreatment.figure += 1
    for d, r in zip(lags, results):
        pylab.subplot(subplot)
        subplot += 1
        pylab.hist(r, bins=max_pop/remission, range=(0, max_pop))
        pylab.title(str(d) + ' Steps Delayed Treatment')
        pylab.xlabel('Final Virus Population')
        pylab.ylabel('Number of Trials')
    return results
 
num_viruses = 100
max_pop = 1000
max_birth_prob = 0.1
clear_prob = 0.05
resistances = {'guttagonol': False, 'grimpex': False}
mut_prob = 0.005
initial_steps = 150
lags = [300, 150, 75, 0]
final_steps = 150
remission = 50
trials = 100
simulationTwoDrugsDelayedTreatment.figure = 0
 

 
#Q1, Q2, Q4
#simulationTwoDrugsDelayedTreatment(trials)
 
#Q3
#mut_prob *= 2
#simulationTwoDrugsDelayedTreatment(trials)
#mut_prob /= 2
 
#Q5 This won't give you the correct answer, there is a chance the
#answer marked as correct in the Problem Set isn't in fact correct.
results = simulationTwoDrugsDelayedTreatment(trials)
for r in results:
    temp = pylab.array(r)
    print(temp.mean(), temp.var(), temp.std())
 
pylab.show()
