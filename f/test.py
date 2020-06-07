from random import randint
from f import py_solver
from subprocess import Popen, PIPE, STDOUT, call
from time import sleep


def cpp_solver(query):
    x = Popen(['./a.out'], stdout=PIPE, stdin=PIPE, stderr=STDOUT)
    while x.poll() is None:
        child_output = x.communicate(input=bytes(query, 'utf-8'))[0].decode().strip()
        if child_output.isdigit():
            result = int(child_output)
            return result
    return -1


def tester(target, arr):
    str_arr = " ".join(list(map(lambda x: str(x), arr)))
    query = f"{target}\n{str_arr}\n"
    with open('input.txt', 'w') as inp:
        inp.write(query)

    py_result = py_solver(query)
    cpp_result = cpp_solver(query)
    if py_result != cpp_result:
        print('You\'re loh.', 'Python:', py_result, 'C++:', cpp_result)
        with open('results.log', 'w') as res:
            res.write('Python: ' + str(py_result) +
                    ' C++: ' + str(cpp_result) +
                    ' Target: ' + str(target) +
                    ' Array: ' + ' '.join(map(lambda x: str(x), arr)) + f'\n')
        return -1

    return 0

    with open('output.txt', 'r') as out:
        output = out.readline()
        if output.isdigit():
            result = int(output)
            for el in arr:
                if el > target:
                    continue
                if target - el in arr and result == 0:
                    if arr.index(target - el) != arr.index(el) or arr.count(el) > 1:
                        print ('Error 0: Target', target, 'Array:', ' '.join(map(lambda x: str(x), arr)))
                        return
                elif target - el in arr and result == 1:
                    if arr.index(target - el) != arr.index(el) or arr.count(el) > 1:
                        print ('1:', target, 'Nums', el, 'and', target - el, 'both are in', ' '.join(map(lambda x: str(x), arr)))
                        return

            if result == 1:
                print ('Error 1: Target', target, 'Array:', ' '.join(map(lambda x: str(x), arr)))
            elif result == 0:
                print ('0:', target, 'Nums', el, 'and', target - el, 'are not in the', ' '.join(map(lambda x: str(x), arr)))
                return
        else:
            print(child_output)


if __name__ == "__main__":
    for i1 in range(0, 10000):
        target = randint(1, 1000)
        arr = []
        for i2 in range(0, randint(100, 1000)):
            arr.append(randint(1, 1000))
        #print ('Starting test number', i1, 'Target:', target, 'Array:', arr)
        print ('Starting test number', i1)
        if tester(target, arr) == -1:
            break
        sleep(0.002)
