#min, max değerleri ve eleman sayısı girilerek rastgele dizi üretme

import random
def get_n_random_number(n=10,min=-5,max=5):
    numbers=[]
    for i in range(n):
        numbers.append(random.randint(min,max))
    return numbers

print(get_n_random_number())

#2 farklı metotla histogram değerlerini bulma (sözlük yapısı ile listede frekans tablosu elde etme)

list=get_n_random_number()
print(list)

#sözlük yapısı ile frekans tablosu oluşturma

def my_frequency_with_dict(list):
    frequency_dict={}
    for item in list:
        if (item in frequency_dict):
            frequency_dict[item]=frequency_dict[item]+1
        else:                           #eğer bir değerle ilk defa karşılaşıyorsa bu bloğa girer
            frequency_dict[item]=1
    return frequency_dict

print(my_frequency_with_dict(list))

#liste ile frekans tablosu oluşturma

def my_frequency_with_of_tuples(list_1):
    frequency_list=[]
    for i in range(len(list_1)):
        s=False
        for j in range(len(frequency_list)):
            if(list_1[i]==frequency_list[j][0]):
                frequency_list[j][1]=frequency_list[j][1]+1
                s=True
        if(s==False):                              #eğer bir değerle ilk defa karşılaşıyorsa bu bloğa girer
            frequency_list.append([list_1[i],1])
    return frequency_list

print(my_frequency_with_of_tuples(list))
