import fileinput

class CustomStack:
    arr = []

    def add(self, num):
        self.arr.append(num)

    def remove(self, num):
        if num in self.arr:
            self.arr.remove(num)
            return 0
        return 1

    def pprint(self):
        for num in self.arr:
            print(num)


if __name__ == "__main__":
    mystack = CustomStack()

    for num in fileinput.input():
        if mystack.remove(num):
            mystack.add(num)
    mystack.pprint()
