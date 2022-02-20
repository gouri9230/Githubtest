expenses=[2200,2350,2600,2130,2090]
heros=['spider man','thor','hulk','iron man','captain america']

print('extra money spent in feb = ',expenses[1]-expenses[0])

print('total money spent in 1st quarter is',expenses[1]+expenses[0]+expenses[2])

flag=0
for item in range(5):
    if(expenses[item]==2000):
        print('you spent exactly 2000rs in the month',item+1)
        flag=0
    else:
        flag=1
if(flag==1):
    print('you did not spend 2000rs exactly in any month')

expenses.append(1980)
print(expenses)
refund =expenses[3]-200
expenses.remove(expenses[3])
expenses.insert(3,refund)
print(expenses)

print(len(heros))
heros.append('black panther')
print(heros)

heros[1:3]=['doctor strange']
print(heros)



