from random import randint
from time import sleep
from subprocess import Popen, PIPE, STDOUT



def subprocess_interactions(num1, num2):
    x = Popen(['./a.out'], stdout=PIPE, stdin=PIPE, stderr=STDOUT)
    while x.poll() is None:

        query = f"{num1} {num2}\n"
        child_output = x.communicate(input=bytes(query, 'utf-8'))[0].decode().strip()

        if child_output.isdigit():
            result = int(child_output)
            if result != num1 + num2:
                print(str(num1), '+', str(num2), '!=', str(result))
                return
            else:
                #print('Success:', str(num1), '+', str(num2), '==', str(result))
                return
        else:
            print(str(num1), 'and', str(num2), 'resulted', str(child_output), 'TypeError')
            return





if __name__ == "__main__":
    print('Started tests for 100')
    for i in range(0, 10000):
        num1 = randint(1, 100)
        num2 = randint(1, 100)
        subprocess_interactions(num1, num2)
    print('Do you want to continue?')
    input()
    print('Started tests for 10000')
    for i in range(0, 10000):
        num1 = randint(1, 10000)
        num2 = randint(1, 10000)
        subprocess_interactions(num1, num2)
    print('Do you want to continue?')
    input()
    print('Started tests for 1000000')
    for i in range(0, 10000):
        num1 = randint(1, 1000000)
        num2 = randint(1, 1000000)
        subprocess_interactions(num1, num2)
    print('Do you want to continue?')
    input()
    print('Started tests for 100000000')
    for i in range(0, 10000):
        num1 = randint(1, 100000000)
        num2 = randint(1, 100000000)
        subprocess_interactions(num1, num2)
    print('Do you want to continue?')
    input()
    print('Started tests for 10000000000')
    for i in range(0, 10000):
        num1 = randint(1, 10000000000)
        num2 = randint(1, 10000000000)
        subprocess_interactions(num1, num2)
