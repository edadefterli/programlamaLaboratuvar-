import random
class Item(object):
    def __init__(self,n,v,w):
        self.name=n
        self.value=v
        self.weight=w
    def getName(self):
        return self.name
    def getValue(self):
        return self.value
    def getWeight(self):
        return self.weight
    def __str__(self):
        result= "<" + self.name + "," + str(self.value)\
                + "," + str(self.weight) + ">"
        return result


#toConsider --> eşyaların tutulduğu liste
#avail --> çantanın sahip olduğu kapasite
def maxVal(toConsider,avail):
    if toConsider==[] or avail==0:
        result=(0,())
    elif toConsider[0].getWeight() > avail:      #ilk eleman avail'dan büyük ise listenin geri kalanını fonksiyona gönder.
        result=maxVal(toConsider[1:],avail)
    else:
        nextItem=toConsider[0]
        #left branch
        withVal,withToTake=maxVal(toConsider[1:],avail-nextItem.getWeight())
        withVal+=nextItem.getValue()
        #right branch
        withoutVal,withoutToTake=maxVal(toConsider[1:],avail)
        #choose better branch
        if withVal > withoutVal:
            result=(withVal,withToTake+(nextItem,))
        else:
            result=(withoutVal,withoutToTake)
    return result

def smallTest():        #az elemanlı yapılar için kullanılır.
    names=['a','b','c','d']
    vals=[6,7,8,9]
    weights=[1,1,1,2]
    Items=[]
    for i in range(len(vals)):
        Items.append(Item(names[i],vals[i],weights[i]))
    val,taken=maxVal(Items,5)
    for item in taken:
        print(item)
    print("Total value of items taken=",val)

smallTest()

def buildManyItems(numItems,maxVal,maxWeight):
    items=[]
    for i in range(numItems):
        items.append(Item(str(i), random.randint(1, maxVal), random.randint(1, maxWeight)))
    return items

def bigTest(numItems):
    items=buildManyItems(numItems,10,10)
    val,taken=maxVal(items,40)
    print("Items Taken")
    for item in taken:
        print(item)
    print("Total value of items taken=",val)

bigTest(14)

def fastMaxVal(toConsider,avail,memo={}):
    if(len(toConsider),avail) in memo:
        result=memo[len(toConsider),avail]
    elif toConsider==[] or avail==0:
        result=(0,())
    elif toConsider[0].getWeight()> avail:
        result=fastMaxVal(toConsider[1:],avail,memo)
    else:
        nextItem=toConsider[0]
        withVal,withToTake=fastMaxVal(toConsider[1:],avail-nextItem.getWeight(),memo)
        withVal+=nextItem.getValue()
        withoutVal, withoutToTake = fastMaxVal(toConsider[1:], avail,memo)
        if withVal > withoutVal:
            result=(withVal,withToTake+(nextItem,))
        else:
            result=(withoutVal,withoutToTake)

    memo[len(toConsider),avail]=result
    return result

numItems=500
items=buildManyItems(numItems,10,10)
print(fastMaxVal(items,40))