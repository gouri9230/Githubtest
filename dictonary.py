dict_popu = {"China":143, "India":136, "USA":32,"Pakistan":21}

def printf():
    for k,v in dict_popu.items():
        print('Country',k ,'==>', v)

def add():
    name = input('Enter country name: ')
    if name in dict_popu:
        print('Country already exists in the dictonary')
    else:
        num = input('Enter population of the country: ')
        dict_popu[name] = num
        printf()

def remove():
    coun=input('Enter country to remove ')
    if coun in dict_popu:
        del dict_popu[coun]
        printf()
    else:
        print('The country does not exist in the dictonary.')

def query():
    coun=input('Enter country name ')
    print(f'Population of {coun} = {dict_popu[coun]}')


choice = int(input("Select any one operation: 1.Print 2.Add 3.Remove 4.query"))
if (choice == 1):
    printf()
elif (choice == 2):
    add()
elif (choice == 3):
    remove()
elif (choice == 4):
    query()
else:
    print('Enter a valid choice.')


