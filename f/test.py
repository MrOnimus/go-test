from random import randint
from subprocess import Popen, PIPE, STDOUT, call


def subprocess_interactions(target, arr):
    str_arr = " ".join(list(map(lambda x: str(x), arr)))
    query = f"{target}\n{str_arr}\n"
    x = Popen(['./a.out'], stdout=PIPE, stdin=PIPE, stderr=STDOUT)
    while x.poll() is None:
        child_output = x.communicate(input=bytes(query, 'utf-8'))[0].decode().strip()

        if child_output.isdigit():
            result = int(child_output)
            for el in arr:
                if el > target:
                    continue
                if target - el in arr and result == 0:
                    if arr.index(target - el) != arr.index(el) or arr.count(el) > 1:
                        print ('Error 0: Target', target, 'Array:', ' '.join(map(lambda x: str(x), arr)))
                        return
                elif target - el in arr and result == 1:
                    if arr.index(target - el) != arr.index(el) or arr.count(el) > 1:
                        pass #print ('1:', target, 'Nums', el, 'and', target - el, 'both are in', arr)
                        return

            if result == 1:
                print ('Error 1: Target', target, 'Array:', ' '.join(map(lambda x: str(x), arr)))
            elif result == 0:
                pass #print ('0:', target, 'Nums', el, 'and', target - el, 'are not in the', arr)
            return
        else:
            print(child_output)


if __name__ == "__main__":
    for i in range(0, 10000):
        target = randint(1, 100)
        arr = []
        for i in range(0, randint(10,50)):
            arr.append(randint(1, 100))
        subprocess_interactions(target, arr)

    #print('Beginning the second test.')
    #for i in range(0, 10000):
    #    target = randint(2, 100)
    #    arr = []
    #    num1 = target - randint(1,target - 1)
    #    num2 = target - num1
    #    arr.append(num1)
    #    arr.append(num2)
    #    for i in range(0, randint(10,50)):
    #        arr.append(randint(1, 100))
    #    subprocess_interactions(target, arr)
