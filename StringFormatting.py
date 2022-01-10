def print_formatted(number):
    w=len(bin(number)[2:])
    for i in range(1,number+1):
       print('{:>{width}} {:>{width}} {:>{width}} {:>{width}}'.format(i,oct(i)[2:],str(hex(i)[2:]).upper(),bin(i)[2:],width=w))


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)