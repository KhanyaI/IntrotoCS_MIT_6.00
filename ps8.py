# 6.00 Problem Set 8
#
# Name:
# Collaborators:
# Time:



import numpy
import random
import pylab


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
# PROBLEM 1
#
class ResistantVirus(SimpleVirus):

    """
    Representation of a virus which can have drug resistance.
    """      

    def __init__(self, maxBirthProb, clearProb, resistances, mutProb):

        """

        Initialize a ResistantVirus instance, saves all parameters as attributes
        of the instance.

        maxBirthProb: Maximum reproduction probability (a float between 0-1)        
        clearProb: Maximum clearance probability (a float between 0-1).

        resistances: A dictionary of drug names (strings) mapping to the state
        of this virus particle's resistance (either True or False) to each drug.
        e.g. {'guttagonol':False, 'grimpex',False}, means that this virus
        particle is resistant to neither guttagonol nor grimpex.

        mutProb: Mutation probability for this virus particle (a float). This is
        the probability of the offspring acquiring or losing resistance to a drug.        

        """


        SimpleVirus.__init__(self, maxBirthProbmax, clearProb)
        self.resistances = resistances
        self.mutProb = mutProb



    def isResistantTo(self, drug):

        """
        Get the state of this virus particle's resistance to a drug. This method
        is called by getResistPop() in Patient to determine how many virus
        particles have resistance to a drug.    

        drug: The drug (a string)
        returns: True if this virus instance is resistant to the drug, False
        otherwise.
        """

        # TODO

        for key,value in self.resistances:
            if key == drug:
                if value == True:
                    return drug
                else:
                    return False



    def reproduce(self, popDensity, activeDrugs):

        """
        Stochastically determines whether this virus particle reproduces at a
        time step. Called by the update() method in the Patient class.

        If the virus particle is not resistant to any drug in activeDrugs,
        then it does not reproduce. Otherwise, the virus particle reproduces
        with probability:       
        
        self.maxBirthProb * (1 - popDensity).                       
        
        If this virus particle reproduces, then reproduce() creates and returns
        the instance of the offspring ResistantVirus (which has the same
        maxBirthProb and clearProb values as its parent). 

        For each drug resistance trait of the virus (i.e. each key of
        self.resistances), the offspring has probability 1-mutProb of
        inheriting that resistance trait from the parent, and probability
        mutProb of switching that resistance trait in the offspring.        

        For example, if a virus particle is resistant to guttagonol but not
        grimpex, and `self.mutProb` is 0.1, then there is a 10% chance that
        that the offspring will lose resistance to guttagonol and a 90% 
        chance that the offspring will be resistant to guttagonol.
        There is also a 10% chance that the offspring will gain resistance to
        grimpex and a 90% chance that the offspring will not be resistant to
        grimpex.

        popDensity: the population density (a float), defined as the current
        virus population divided by the maximum population        

        activeDrugs: a list of the drug names acting on this virus particle
        (a list of strings). 
        
        returns: a new instance of the ResistantVirus class representing the
        offspring of this virus particle. The child should have the same
        maxBirthProb and clearProb values as this virus. Raises a
        NoChildException if this virus particle does not reproduce.         
        """
        # TODO
        ## When we need to call the ResistantVirus(), we pass four parameters
        
        for drug in activeDrugs:
            if self.isResistantTo(drug):
                reproducing_prob = self.maxBirthProb * (1 - popDensity)
                babyvirusresistances={}
                if reproducing_prob > random.random():
                    for drug in self.resistances.key():
                        if random.random() > self.mutProb:
                        babyvirusresistance[drug] = not self.resistances[drug]
                    else:
                        babyvirusresistance[drug] = self.resistances[drug]

                babyvirus = ResistantVirus(self.maxBirthProb,self.clearProb,babyvirusresistances,self.mutProb)
                return babyvirus
            else:
                raise NoChildException()



class DruggedPatient(SimplePatient):

    """
    Representation of a patient. The patient is able to take drugs and his/her
    virus population can acquire resistance to the drugs he/she takes.
    """

    def __init__(self, viruses, maxPop):
        """
        Initialization function, saves the viruses and maxPop parameters as
        attributes. Also initializes the list of drugs being administered
        (which should initially include no drugs).               

        viruses: the list representing the virus population (a list of
        SimpleVirus instances)
        
        maxPop: the  maximum virus population for this patient (an integer)
        """
        # TODO
        SimplePatient.__init__(self, viruses, maxPop)
        self.drugslist= []
    

    def addPrescription(self, newDrug):

        """
        Administer a drug to this patient. After a prescription is added, the 
        drug acts on the virus population for all subsequent time steps. If the
        newDrug is already prescribed to this patient, the method has no effect.

        newDrug: The name of the drug to administer to the patient (a string).

        postcondition: list of drugs being administered to a patient is updated
        """
        # TODO
        # should not allow one drug being added to the list multiple times
       
        if newDrug in self.drugslist:
            print('Already there')
        else:
            self.drugslist.append(newDrug)


    def getPrescriptions(self):

        """
        Returns the drugs that are being administered to this patient.
        returns: The list of drug names (strings) being administered to this
        patient.
        """

        # TODO
        return self.drugslist
        

    def getResistPop(self, drugResist):
        """
        Get the population of virus particles resistant to the drugs listed in 
        drugResist.        

        drugResist: Which drug resistances to include in the population (a list
        of strings - e.g. ['guttagonol'] or ['guttagonol', 'grimpex'])

        returns: the population of viruses (an integer) with resistances to all
        drugs in the drugResist list.
        """
        # TODO

        resistance = 0
        resistantviruses = 0
        self.drugResist = drugResist
        for virus in self.viruses:
            for drug in getPrescriptions():
                if virus.isResistantTo(drug):
                    resistance += 1
            if resistance == len(drugslist):
                resistantviruses += 1
        return resistantviruses
                   

    def update(self):

        """
        Update the state of the virus population in this patient for a single
        time step. update() should execute these actions in order:
        
        - Determine whether each virus particle survives and update the list of 
          virus particles accordingly          
        - The current population density is calculated. This population density
          value is used until the next call to update().
        - Determine whether each virus particle should reproduce and add
          offspring virus particles to the list of viruses in this patient. 
          The listof drugs being administered should be accounted for in the
          determination of whether each virus particle reproduces. 

        returns: the total virus population at the end of the update (an
        integer)
        """
        # TODO

        for virus in self.viruses:
            if virus.doesClear():
                self.viruses.remove(virus)

        popDensity = float(len(survived_viruses))/self.maxPop

        babyviruses = []
        for virus in self.viruses:
            try:
                virus.reproduce(popDensity,self.drugslist)
                babyviruses.append(virus)
            except NoChildException:
                pass
        self.viruses = babyviruses

        return self.getTotalPop()





#
# PROBLEM 2
#

def simulationWithDrug(numViruses, maxPop, maxBirthProb, clearProb, resistances,
                       mutProb, numTrials, steps):

    """

    Runs simulations and plots graphs for problem 4.
    Instantiates a patient, runs a simulation for 150 timesteps, adds
    guttagonol, and runs the simulation for an additional 150 timesteps.
    total virus population vs. time and guttagonol-resistant virus population
    vs. time are plotted
    """
    # TODO
    numTrials = 30
    numSteps = 150
    numViruses = 100 
    maxPop = 1000
    maxBirthProb = 0.1
    clearProb = 0.05
    resistances = {guttagonol: False}
    mutProb = 0.005
  

    
    for i in range (0,numTrials):
        for i in range(0,numViruses):
            resistantvirus = ResistantVirus(maxBirthProb,clearProb,resistances,mutProb)
            resistant_virus_list.append(resistantvirus)
        bob = DruggedPatient(resistant_virus_list,maxPop)
        
        resistantviruses_in_bob = []
        simpleviruses_in_bob = []

        for i in range(0,steps+150):
            if i == steps:
                bob.addPrescription("guttagonol")
            bob.update()
            simpleviruses_in_bob.append(bob.getTotalPop())
            resistantviruses_in_bob.append(bob.getResistPop(["guttagonol"]))
            return virsuses_in_bob
    

    avg_simple_viruses_in_bob = [x / float(numTrials) for x in simpleviruses_in_bob]
    avg_viruses_in_bob_drugged = [x / float(numTrials) for x in resistantviruses_in_bob]

    x = range(0,numSteps)
    y = avg_viruses_in_bob

    x_drug = range(0,numSteps)
    y_drug = avg_viruses_in_bob_drugged

    pylab.plot(x,y)
    pylab.plot(x_drug,y_drug)
    pylab.title("SimpleVirus & ResistantVirus simulation")
    pylab.xlabel("Time step")
    pylab.ylabel("Avg # viruses")
    pylab.legend(loc = "best")
    pylab.show()

  

 

#
# PROBLEM 3
#        

def simulationDelayedTreatment():

    """
    Runs simulations and make histograms for problem 5.
    Runs multiple simulations to show the relationship between delayed treatment
    and patient outcome.
    Histograms of final total virus populations are displayed for delays of 300,
    150, 75, 0 timesteps (followed by an additional 150 timesteps of
    simulation).    
    """

    # TODO

    delays = [300,150,75,0]
    finalvirus_list = []

   
    for delay in delays:
        delayed_viruses = simulationWithDrug(look above)
        finalvirus_list.append(delayed_viruses)

    print(finalvirus_list)
   
#
# PROBLEM 4
#

def simulationTwoDrugsDelayedTreatment():

    """
    Runs simulations and make histograms for problem 6.
    Runs multiple simulations to show the relationship between administration
    of multiple drugs and patient outcome.
   
    Histograms of final total virus populations are displayed for lag times of
    150, 75, 0 timesteps between adding drugs (followed by an additional 150
    timesteps of simulation).
    """

    # TODO
    #same like prob 2+3, add extra step for another medicine
    # total: pat.update
    #then delay, and add prescription: medicine 1
    #then delay, and add prescription: medicine 2


#
# PROBLEM 5
#    

def simulationTwoDrugsVirusPopulations():

    """

    Run simulations and plot graphs examining the relationship between
    administration of multiple drugs and patient outcome.
    Plots of total and drug-resistant viruses vs. time are made for a
    simulation with a 300 time step delay between administering the 2 drugs and
    a simulations for which drugs are administered simultaneously.        

    """
    #TODO

    #same as above
    # total time: add prescription: medicine 1+2, update
    #2nd sim, delay+300, update and prescrip with one medicine, then delay, and add prescription: medicine 2

