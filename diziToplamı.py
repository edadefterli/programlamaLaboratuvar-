def max_of_two(a,b):
    if a>b:
        return a
    else:
        return b

def max_of_three(a,b,c):
    return max_of_two(a,max_of_two(b,c))

def my_sub_sum_recursive(liste1):
    if(len(liste1)==1):
        return liste1[0]
    n=len(liste1)
    left_i=0
    left_j=n//2
    right_i=(n//2)
    right_j=n
    left_sum=my_sub_sum_recursive(liste1[left_i:left_j])
    right_sum=my_sub_sum_recursive(liste1[right_i:right_j])
    temp_left_sum,t=0,0
    for i in range(left_j-1,left_i-1,-1):
        t+=liste1[i]
        if(t>temp_left_sum):
            temp_left_sum=t

    temp_right_sum,t=0,0
    for i in range(right_i,right_j):
        t+=liste1[i]
        if(t>temp_right_sum):
            temp_right_sum=t

    center_sum=temp_left_sum+temp_right_sum
    return max_of_three(left_sum,right_sum,center_sum)

liste2=[4,-3,5,-2,-1,2,6,-2]
print(my_sub_sum_recursive(liste2))