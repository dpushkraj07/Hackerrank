def print_formatted(st):
    # your code goes here


    w=len(bin(st)[2:])


    for i in range(1,st+1):
        print (str(i).rjust(w,' '),str(oct(i)[2:]).rjust(w,' '),str(hex(i)[2:].upper()).rjust(w,' '),str(bin(i)[2:]).rjust(w,' '))

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
