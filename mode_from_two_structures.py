#mod bulma

#sözlük üzerinden mod değerinin bulunması

def my_mod_with_dict(my_hist_d):
    frequency_max=-1
    mode=-1
    for key in my_hist_d.keys():
        #print(key,my_hist_d[key])
        if my_hist_d[key]>frequency_max:
            frequency_max=my_hist_d[key]
            mode=key
    return mode,frequency_max

my_dict={1: 1, 5: 2, 3: 1, -2: 1, -1: 1, -5: 1, -4: 1, 4: 5}
print(my_mod_with_dict(my_dict))

#liste üzerinden mod değerinin bulunması

def my_mode_with_list(my_hist_list):
    frequency_max=-1
    mode=-1
    for item,frequency in my_hist_list:
        #print(item,frequency)
        if frequency>frequency_max:
            frequency_max=frequency
            mode=item
    return mode,frequency_max

my_list=[[-2,1],[3,1],[2,2],[-4,6],[-5,3],[1,1],[-3,1]]
print(my_mode_with_list(my_list))