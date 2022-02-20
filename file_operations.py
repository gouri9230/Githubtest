word_str = { }

with open("C:\\Users\\Shrigouri\\poem.txt",'r') as p:
    for line in p:
        words = line.split(' ')
        for word in words:
            if word in word_str:
                word_str[word]+=1
            else:
                word_str[word] = 1
print(word_str)

word_occurance= list(word_str.values())
max_count = max(word_occurance)
print('Max times word has occurred is: ', max_count)

for value,count in word_str.items():
    if count == max_count:
        print('Word that has occurred most is: ',value)

print(p.closed)