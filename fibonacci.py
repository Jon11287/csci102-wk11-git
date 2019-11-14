# fibonacci.py

def fib():
    fibs = [1, 2]

    for i in range(1,9):
        newNum = 0

        if i == 1:
            newNum = fibs[0] + fibs[1]
            fibs.append(newNum)
        elif i != 1:
            newNum = fibs[i] + fibs[i-1]
            fibs.append(newNum)


    return fibs

def main():
    print('OUTPUT', fib())

if __name__ == "__main__":
    main()

