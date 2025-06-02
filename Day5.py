lst = [10,15,16,2,3,4,7, 6,45,200,59]

def sum_avg(n):
    total = 0
    for i in n:
        total = total + i 
    average = total/len(n)
    return f"the total {total} and Average is {round(average,2)}"

output = sum_avg(lst)
print(output)


x = int(input())
lmbda = lambda x : x**2 

print(lmbda(x))