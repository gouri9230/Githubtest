class fibonacci:
    def __init__(self, num):
        self.num = num
        self.first = 0
        self.second = 1
        self.count=1

    def __iter__(self):
        return self

    def __next__(self):
        if(self.num >= self.count):
            current = self.first + self.second
            self.first = self.second
            self.secon = current
            self.count+=1
            return current
        else:
            raise Exception


def main():
    numb = int(input("Enter a num until which you want fibonacci series: "))
    fib = iter(fibonacci(numb))
    for i in range(1,numb+1):
        try:
            print(next(fib))
        except Exception:
            print("out of bound")

if __name__ == "__main__":
    main()