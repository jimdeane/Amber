import numpy as np
import random
from matplotlib import pyplot as plt
import math
    #Square well Prototype

def squareLattice1D(maxSteps,initialLattice):
    print("Definine lattices...")
    for i in range(maxSteps):
        allLattices=[]
        allLattices.append(np.zeros(len(initialLattice)).tolist())
        #clean up the list - turn the floats into ints
        for i,lattice in enumerate(allLattices):
            for j,element in enumerate(lattice):
                allLattices[i][j] = int(allLattices[i][j])
    return allLattices
print("Initialising...")
positionlattice = [] #position tracking
    #lattice length goes from -J...0,J, length 2J+1 (for center)
maxJ = 8
coordinatelattice = np.arange(-maxJ,maxJ+1) # coordinate reference
for i in coordinatelattice:
    positionlattice.append(0)
    centerIndex = int(np.where(coordinatelattice==0)[0])
   
    #method: track surviving points using the position lattice.
    #if a drunkard at the point survives, add 1 to the point
    #the result of this should be initially a dirac delta function that spreads out as a gaussian - same behaviour as QM Kernel\n",
    numberOfRepeats = 10000
    maxSteps = 400
    initialLattice = positionlattice
    allLattices = squareLattice1D(maxSteps,initialLattice)
    #define full array of following lattices up to the max steps
   
    "we have now created a 2d array, on the x axis we have the number of particles that arrived"
    "at the point, and on the y axis we have the time evolution, starting from t=0"
print("Running simulation...")
paths = [] #for visualisation
for t in range(numberOfRepeats):
    currentIndex = centerIndex
    path = [] #for visualisation
    for step in range(maxSteps): #step defines the index we're working on in allLattices
        if currentIndex < 0 or currentIndex >= len(initialLattice):
                #this chain is absorbed, end and go to the next repeat
            break # Note for future me: IF THERE'S A PROBLEM THIS IS PROBABLY THE CAUSE
            path.append(coordinatelattice[currentIndex])
            allLattices[step][currentIndex] += 1
            #now, we define the direction for the next step
            direction = random.randint(0,1)
            if direction == 0:
                currentIndex -= 1
            else:
                currentIndex += 1
            #path visualisation
   
            continue
            paths.append(path)
    #display the time-slices in order
   
survived = []
survivedstd = []
for lattice in allLattices:
        #print(f\"{lattice}, survived:{sum(lattice)}\")
    survived.append(sum(lattice))
    survivedstd.append(np.std(lattice))
    survived = np.array(survived)
    survived = np.divide(survived,numberOfRepeats)
    #print(survived)
    times = np.arange(0,len(allLattices))
    plt.plot(times, survived)
    plt.ylabel("Fraction Survived")
    plt.xlabel("Time steps")
    plt.title("Infinite square well potential")
   
   
   
   
   
   
   
   
"FIND THE ENERGY",
    #need to establish our deltatime and deltax later for *real* values
   
    #in arbitrary units:
    #set arbitrary delta
N = 50
averageSize = math.floor(len(allLattices)/N - (0.1*(len(allLattices)/N))) # size of \"averaging index\", must be odd to find midpoints
comparePointIndices = np.linspace(0,len(times)-1,N,endpoint=True)
inBetweenPoints = []
for i,index in enumerate(comparePointIndices):
    comparePointIndices[i] = int(math.floor(comparePointIndices[i]))
   
    #spacingcalculation
    spacings = comparePointIndices[1]-comparePointIndices[0] #assume spacings roughly constant
   
    plus = np.arange(0,averageSize,1) #get an average around +2 points after the index
    #now to actually calculate the energies
   
    timeindices = []
    predictedenergies = []
    for i1,index in enumerate(comparePointIndices[0:-3]): #i1 determines index in InBetweenPoints
        i2 = i1+1
        #values about i1,i2
        pm1 = np.add(plus,comparePointIndices[i1])
        if index == comparePointIndices[-2]: #if final value
            pm2 = np.subtract(comparePointIndices[i2],plus)
        else:
            pm2 = np.add(comparePointIndices[i2],plus)
        #indices found above
        #convert indices into integers
        point1index = int(pm1[int(math.floor((averageSize-1)/2))])
        point2index = int(pm2[int(math.floor((averageSize-1)/2))])
       
        #below, averaging 2 points
        point1neighbours = []
        for j in pm1:
            point1neighbours.append(survived[int(j)])
        point1 = np.average(point1neighbours)
        point2neighbours = []
        for j in pm2:
            point2neighbours.append(survived[int(j)])
        point2 = np.average(point2neighbours)
   
        middleindex = int(math.floor(np.average([point1index,point2index])))
   
        #now time for the actual calculation
        deltaT = point2index-point1index
        E = -(1/deltaT)*np.log(point2/point1)
        predictedenergies.append(E)
        timeindices.append(middleindex)
       #print(point1,point2,point1index,point2index,middleindex)
   
plt.plot(timeindices,predictedenergies)
plt.plot(times, survived)
plt.ylabel("Fraction Survived")
plt.xlabel("Time steps")
plt.title("Infinite square well potential"),
plt.grid()
