import random
import matplotlib
import pylab
from matplotlib import pylab
import matplotlib.pyplot as plt


def rollDie():  #bir defa zar atan fonksiyon
    return random.choice([1,2,3,4,5,6])

def rollN(n):   #n defa zar atan fonksiyon
    result=" "
    for i in range(n):
        result=result +"-"+ str(rollDie())
    print(result)

rollN(5)

def flip(numFlips):     #yazı-tura atan fonksiyon(bir para 'numFlips' kadar atıldığında tura gelme olasılığı kaçtir?)
    heads=0 #tura sayısı
    for i in range(numFlips):
        if random.choice(("H","T"))=="H":
            heads+=1
    return heads/numFlips

print("para 10 kez atıldığında tura gelme ihtimali:",flip(10))

def flipSim(numFlipsPerTrial,numTrials):    #numTrials:kaç deney yaptığımızı söyler / numFlipsPerTrial:kaç defa yazı-tura attığımızı belirler
    fracHeads=[] #kaç defa tura geldiğini tutar
    for i in range(numTrials):
        fracHeads.append(flip(numFlipsPerTrial))
    mean=sum(fracHeads)/len(fracHeads)
    return mean

print(flipSim(100,100))

def regressToMean(numFlips,numTrials):  #oluşan grafik bir olayın bir önceki olaydan bağımsız ve farklı olduğunu gösterir.
    fracHeads=[]
    for t in range(numTrials):
        fracHeads.append(flip(numFlips))
    extremes,nextTrials=[],[]
    for i in range(len(fracHeads)-1):
        if fracHeads[i]<0.33 or fracHeads[i]>0.66:
            extremes.append(fracHeads[i])
            nextTrials.append(fracHeads[i+1])
    pylab.plot(range(len(extremes)),extremes,'ko',label='Extreme')
    pylab.plot(range(len(nextTrials)), nextTrials, 'k^',label='Next Trials')
    pylab.axhline(0.5)
    pylab.ylim(0,1)
    pylab.xlim(-1,len(extremes)+1)
    pylab.xlabel('Extreme Example and Next Trial')
    pylab.ylabel('Fraction Heads')
    pylab.title('Regression to the Mean')
    pylab.legend(loc='best')

regressToMean(15,40)

def flipPlot(minExp,maxExp):
    ratios,diffs,xAxis=[],[],[]
    for exp in range(minExp,maxExp+1):
        xAxis.append(2**exp)
    for numFlips in xAxis:
        numHeads=0
        for n in range(numFlips):
            if random.choice(("H","T"))=="H":
                numHeads+=1
        numTails=numFlips-numHeads
        try:
            ratios.append(numHeads/numTails)
            diffs.append(abs(numHeads-numTails))
        except ZeroDivisionError:
            continue
        pylab.title('Difference Between Heads and Tails')
        pylab.xlabel('Number of Flips')
        pylab.ylabel('Abs(#Heads - #Tails)')
        pylab.plot(xAxis, diffs,'k')
        pylab.figure()
        pylab.title('Heads/Tails Ratios')
        pylab.xlabel('Number of Flips')
        pylab.ylabel('#Heads/#Tails')
        pylab.plot(xAxis, ratios,'k')

random.seed(0)
flipPlot(4, 20)

def variance(x):
    mean=sum(x)/len(x)
    tot=0.0
    for i in x:
        tot+=(i-mean)**2
    return tot/len(x)

def stdDev(x):
    return variance(x)**0.5


def makePlot(xVals, yVals, title, xLabel, yLabel, style, logX=False,logY=False):
    pylab.figure()
    pylab.title(title)
    pylab.xlabel(xLabel)
    pylab.ylabel(yLabel)
    pylab.plot(xVals, yVals, style)
    if logX:
        pylab.semilogx()
    if logY:
        pylab.semilogy()

def runTrial(numFlips):
    numHeads = 0
    for n in range(numFlips):
        if random.choice(("H","T"))=="H":
            numHeads += 1
    numTails = numFlips - numHeads
    return (numHeads, numTails)

def flipPlot1(minExp, maxExp, numTrials):
    ratiosMeans, diffsMeans, ratiosSDs, diffsSDs = [], [], [], []
    xAxis = []
    for exp in range(minExp, maxExp + 1):
        xAxis.append(2 ** exp)
    for numFlips in xAxis:
        ratios,diffs = [],[]
        for t in range(numTrials):
            numHeads, numTails = runTrial(numFlips)
            ratios.append(numHeads / numTails)
            diffs.append(abs(numHeads - numTails))
        ratiosMeans.append(sum(ratios) / numTrials)
        diffsMeans.append(sum(diffs) / numTrials)
        ratiosSDs.append(stdDev(ratios))
        diffsSDs.append(stdDev(diffs))
    numTrialsString = ' (' + str(numTrials) + ' Trials)'
    title = 'Mean Heads/Tails Ratios' + numTrialsString
    makePlot(xAxis, ratiosMeans, title, 'Number of flips', 'Mean Heads/Tails', 'ko', logX=True)
    title = 'SD Heads/Tails Ratios' + numTrialsString
    makePlot(xAxis, ratiosSDs, title, 'Number of Flips', 'Standard Deviation', 'ko', logX=True, logY=True)

flipPlot1(4,10,5)