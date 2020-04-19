# 6.00 Problem Set 9
#
# Intelligent Course Advisor
#
# Name:
# Collaborators:
# Time:
#
from operator import itemgetter, attrgetter


SUBJECT_FILENAME = "subjects.txt"
SHORT_SUBJECT_FILENAME = "/Users/ifrahkhanyaree/Desktop/HomeDS/Code/MIT_guttag/todo/ps9_greedyalgo_scheduleopti/ps9/shortened_subjects.txt"
VALUE, WORK = 0, 1

#
# Problem 1: Building A Subject Dictionary
#
def loadSubjects(filename):
    """
    Returns a dictionary mapping subject name to (value, work), where the name
    is a string and the value and work are integers. The subject information is
    read from the file named by the string filename. Each line of the file
    contains a string of the form "name,value,work".

    returns: dictionary mapping subject name to (value, work)
    """

    # The following sample code reads lines from the specified file and prints
    # each one.
    dic = {}
    inputFile = open(filename)
    for line in inputFile:
        key,val1,val2=line.strip().split(',', 3)
        dic[key] = (int(val1),int(val2))
    return dic

    # TODO: Instead of printing each line, modify the above to parse the name,
    # value, and work of each subject and create a dictionary mapping the name
    # to the (value, work).

def printSubjects(subjects):
    """
    Prints a string containing name, value, and work of each subject in
    the dictionary of subjects and total value and work of all subjects
   """
    totalVal, totalWork = 0,0
    res = 'Course\tValue\tWork\n======\t====\t=====\n'
    subNames = subjects.keys()
    subNames = sorted(subNames)
    for s in subNames:
        val = subjects[s][VALUE]
        work = subjects[s][WORK]
        res = res + s + '\t' + str(val) + '\t' + str(work) + '\n'
        totalVal += val
        totalWork += work

    res = res + '\nTotal Value:\t' + str(totalVal) +'\n'
    res = res + 'Total Work:\t' + str(totalWork) + '\n'
    return totalVal , totalWork
    return res



#
# Problem 2: Subject Selection By Greedy Optimization
#

def cmpValue(subInfo1, subInfo2):
    """
    Returns True if value in (value, work) tuple subInfo1 is GREATER than
    value in (value, work) tuple in subInfo2
    """
    # TODO...
    if subInfo1[0] > subInfo2[0]:
        return True
    

def cmpWork(subInfo1, subInfo2):
    """
    Returns True if work in (value, work) tuple subInfo1 is LESS than than work
    in (value, work) tuple in subInfo2
    """
    # TODO...
    work=[]
    if subInfo1[1] < subInfo2[1]:
        work.append(subInfo1[1])
    else:
        work.append(subInfo2[1])
    print (work)
   


def cmpRatio(subInfo1, subInfo2):
    """
    Returns True if value/work in (value, work) tuple subInfo1 is 
    GREATER than value/work in (value, work) tuple in subInfo2
    """
    # TODO...

    ratio1 = subInfo1[0]/subInfo1[1]
    ratio2 = subInfo2[0]/subInfo2[1]
    if ratio1 > ratio2:
        return True
  

def greedyAdvisor(subjects,maxWork,comparator):
    """
    maxWork, comparator
    Returns a dictionary mapping subject name to (value, work) which includes
    subjects selected by the algorithm, such that the total work of subjects in
    the dictionary is not greater than maxWork.  The subjects are chosen using
    a greedy algorithm.  The subjects dictionary should not be mutated.

    subjects: dictionary mapping subject name to (value, work)
    maxWork: int >= 0
    comparator: function taking two tuples and returning a bool
    returns: dictionary mapping subject name to (value, work)
    # TODO...
    #sorted_dict = sorted(subjects.items())
    #sorted_dict_value = sorted(subjects.items(), key=itemgetter(0))
    
    sorted_dict = sorted(subjects.items(), key=lambda x: x[1][comparator],reverse=True)
    
    maxwork_schedule = {}
    courseLoad = 0
    i = 0
    for i in range(0,len(sorted_dict)):
        if sorted_dict[i][1][1] <= maxWork - courseLoad:
            maxwork_schedule[sorted_dict[i][0]] = sorted_dict[i][1]
            courseLoad += sorted_dict[i][1][1]
    print(maxwork_schedule)




"""


#
# Problem 3: Subject Selection By Brute Force
#

def dToB(n, numDigits):
    """requires: n is a natural number less than 2**numDigits
      returns a binary string of length numDigits representing the
              the decimal number n."""
    bStr = ''
    while n > 0:
        bStr = str(n % 2) + bStr
        n = n//2
    while numDigits - len(bStr) > 0:
        bStr = '0' + bStr
    return bStr

def genPset(Items):
    """Generate a list of lists representing the power set of Items"""
    numSubsets = 2**len(Items)
    templates = []
    for i in range(numSubsets):
        templates.append(dToB(i, len(Items)))
    listitems = []
    for i in Items.items():
        listitems.append(i)
    #print(listitems)

    pset = []
    for t in templates[0:20]:
        elem = []
        for j in range(len(t)):
            if t[j] == '1':
                elem.append(listitems[j])
        pset.append(elem)
    return pset
    #print(pset)


def chooseBest(pset, constraint):
    bestVal = 0.0
    bestSet = None
    for Items in pset:
        if len(Items) > 0:
            ItemVal = 0
            ItemWeight = 0
            for item in Items:
                ItemVal += int(item[1][0])
                ItemWeight += int(item[1][1])
            if ItemWeight <= constraint and ItemVal > bestVal:
                bestVal = ItemVal
                bestSet = Items
    return (bestSet, bestVal)


if __name__ == '__main__':
    l = loadSubjects(SHORT_SUBJECT_FILENAME)
    g = genPset(l)
    cset,cval = chooseBest(g,10)
    print(cset,cval)
