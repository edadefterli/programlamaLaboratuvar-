import pylab
import random
import scipy.integrate

def getBMData(filename):
    data={}
    f=open(filename)
    line=f.readline()
    data["name"],data["gender"],data["age"]=[],[],[]
    data["division"],data["country"],data["time"]=[],[],[]
    while line != '':
        split=line.split(',')
        data["name"].append(split[0])
        data["gender"].append(split[1])
        data["age"].append(int(split[2]))
        data["division"].append(int(split[3]))
        data["country"].append(split[4])
        data["time"].append(float(split[5][:-1]))
        line=f.readline()
    f.close()
    return data

def variance(x):
    mean=sum(x)/len(x)
    tot=0.0
    for i in x:
        tot+=(i-mean)**2
    return tot/len(x)

def stdDev(x):
    return variance(x)**0.5

def makeHist(data,bins,title,xLabel,yLabel):
    pylab.hist(data,bins)
    pylab.title(title)
    pylab.xlabel(xLabel)
    pylab.ylabel(yLabel)
    mean=sum(data)/len(data)
    std=stdDev(data)
    pylab.annotate('Mean=' + str(round(mean,2)) +\
                   '\nSD= ' +str(round(std,2)),fontsize=20,xy=(0.65,0.75),xycoords='axes fraction')

times=getBMData('bm_results2012.txt')['time']
makeHist(times,20,'2012 Boston Marathon','Minutes to Complete Race','Number of Runners')

def sampleTimes(times,numExamples):
    sample=random.sample(times,numExamples)
    makeHist(sample,10,'Sample of Size'+str(numExamples),'Minutes to Complete Race','Number of Runners')

sampleSize=40
sampleTimes(times,sampleSize)

def gaussian(x,mu,sigma):
    factor1=(1/(sigma*((2*pylab.pi)**0.5)))
    factor2=pylab.e**-(((x-mu)**2)/(2*sigma**2))
    return factor1*factor2

area=round(scipy.integrate.quad(gaussian,-3,3,(0,1))[0],4)
print('Probability of being within 3',
      'of true mean of tight dist.=',area)
area=round(scipy.integrate.quad(gaussian,-3,3,(0,100))[0],4)
print('Probability of being within 3',
      'of true mean of tight dist.=',area)

def testSamples(numTrials,sampleSize):
    tightMeans,wideMeans=[],[]
    for t in range(numTrials):
        sampleTight,sampleWide=[],[]
        for i in range(sampleSize):
            sampleTight.append(random.gauss(0,1))
            sampleWide.append(random.gauss(0,100))
        tightMeans.append(sum(sampleTight)/len(sampleTight))
        wideMeans.append(sum(sampleWide)/len(sampleWide))
    return tightMeans,wideMeans

tightMeans,wideMeans=testSamples(1000,40)
pylab.plot(wideMeans,'y*',label='SD=100')
pylab.plot(tightMeans,'bo',label='SD=1')
pylab.xlabel('Sample Number')
pylab.ylabel('Sample Mean')
pylab.title('Means of Samples of Size '+str(40))
pylab.legend()

pylab.figure()
pylab.hist(wideMeans,bins=20,label='SD=100')
pylab.title('Distribution of Sample Means')
pylab.xlabel('Sample Mean')
pylab.ylabel('Frequency of Occurrence')
pylab.legend()
