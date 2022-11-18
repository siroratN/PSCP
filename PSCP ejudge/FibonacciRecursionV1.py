""" FibonacciRecursionV1 """
def fibonacci(num):
    """ FibonacciRecursionV1 """
    if num <= 0:
        return abs(num)
    return fibonacci(num-1) + fibonacci(num-2)

def main():
    """ cal """
    value = int(input())
    print(fibonacci(value))
main()
