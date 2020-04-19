# Problem Set 7: Simulating the Spread of Disease and Virus Population Dynamics 
# Name:
# Collaborators:
# Time:

import numpy
import random
import pylab

''' 
Begin helper code
'''

class NoChildException(Exception):
    """
    NoChildException is raised by the reproduce() method in the SimpleVirus
    and ResistantVirus classes to indicate that a virus particle does not
    reproduce. You can use NoChildException as is, you do not need to
    modify/add any code.
    """

'''
End helper code
'''

#
# PROBLEM 1
#
class SimpleVirus(object):

    """
    Representation of a simple virus (does not model drug effects/resistance).
    """
    def __init__(self, maxBirthProb, clearProb):
        self.maxBirthProb = maxBirthProb
        self.clearProb = clearProb


        """
        Initialize a SimpleVirus instance, saves all parameters as attributes
        of the instance.        
        maxBirthProb: Maximum reproduction probability (a float between 0-1)        
        clearProb: Maximum clearance probability (a float between 0-1).
        """

        # TODO

    def doesClear(self):

        """ Stochastically determines whether this virus particle is cleared from the
        patient's body at a time step. 
        returns: True with probability self.clearProb and otherwise returns
        False.
        """

        # TODO
        doNotClear = random.random()
        return self.clearProb > doNotClear

    
    def reproduce(self, popDensity):

        """
        Stochastically determines whether this virus particle reproduces at a
        time step. Called by the update() method in the SimplePatient and
        Patient classes. The virus particle reproduces with probability
        self.maxBirthProb * (1 - popDensity).
        
        If this virus particle reproduces, then reproduce() creates and returns
        the instance of the offspring SimpleVirus (which has the same
        maxBirthProb and clearProb values as its parent). 


        popDensity: the population density (a float), defined as the current
        virus population divided by the maximum population.         
        
        returns: a new instance of the SimpleVirus class representing the
        offspring of this virus particle. The child should have the same
        maxBirthProb and clearProb values as this virus. Raises a
        NoChildException if this virus particle does not reproduce.               
        """

        # TODO
        reproducing_prob = self.maxBirthProb * (1 - popDensity)

        if random.random() < reproducing_prob:
            babyvirus = SimpleVirus(self.maxBirthProb,self.clearProb)
            return babyvirus
        else:
            return NoChildException('Not reproduced')






class SimplePatient(object):

    """
    Representation of a simplified patient. The patient does not take any drugs
    and his/her virus populations have no drug resistance.
    """    

    def __init__(self, viruses, maxPop):

        """

        Initialization function, saves the viruses and maxPop parameters as
        attributes.

        viruses: the list representing the virus population (a list of
        SimpleVirus instances)

        maxPop: the  maximum virus population for this patient (an integer)
        """

        # TODO

        self.viruses = viruses
        self.maxPop = maxPop


    def getTotalPop(self):

        """
        Gets the current total virus population. 
        returns: The total virus population (an integer)
        """

        # TODO  
        currentTotPop = len(self.viruses)   
        return currentTotPop   


    def update(self):

        """
        Update the state of the virus population in this patient for a single
        time step. update() should execute the following steps in this order:
        
        - Determine whether each virus particle survives and updates the list
        of virus particles accordingly.   
        - The current population density is calculated. This population density
          value is used until the next call to update() 
        - Determine whether each virus particle should reproduce and add
          offspring virus particles to the list of viruses in this patient.                    

        returns: The total virus population at the end of the update (an
        integer)
        """

        # TODO
        for virus in self.viruses:
            if virus.doesClear():
                self.viruses.remove(virus)

"""        
        pop_density = len(self.viruses)/float(self.maxPop)

        children = []

        for virus in self.viruses:
            children.append(virus)
            try:
                child = virus.reproduce(pop_density)
                children.append(child)
            except NoChildException:

                

        self.viruses = self.viruses + children
        return len(self.viruses)
"""
    

#
# PROBLEM 2
#
def simulationWithoutDrug():

    """
    Run the simulation and plot the graph for problem 2 (no drugs are used,
    viruses do not have any drug resistance).    
    Instantiates a patient, runs a simulation for 300 timesteps, and plots the
    total virus population as a function of time.    
    """

    # TODO
    numSteps = 300
    numTrials = 100
    numViruses = 100
    maxpop = 1000
    maxbirthprob = 0.1
    clearprob = 0.05


    viruses_list = []

    for i in range(0,numTrials):
        for i in range(0,numViruses):
            init_virus = SimpleVirus(maxbirthprob,clearprob)
            viruses_list.append(init_virus)

    patient = SimplePatient(viruses_list,maxpop)
    viruses_in_patient = []
    for i in range(0,numSteps):
        patient.update()
        viruses_in_patient.append(patient.getTotalPop())
    return viruses_in_patient

    
    
    avg_viruses_in_pat = [x / float(numTrials) for x in viruses_in_patient]

    x_Axis = range(0,numSteps)
    y_Axis = updated_viruses

    pylab.plot(avgVirusList)
    pylab.title("SimpleVirus simulation")
    pylab.xlabel("Time step")
    pylab.ylabel("Avg # viruses")
    pylab.legend(loc = "best")
    pylab.show()

if __name__ == '__main__':
    sim = simulationWithoutDrug()

