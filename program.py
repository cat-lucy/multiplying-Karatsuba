import timeit
from KaratsubaMultiply import *
from MultiplyException import *

@timeit.timeit
def main():
    try:
        a = check_number((input('Enter first number: ')))
        b = check_number((input('Enter second number: ')))
        ans = KaratsubaMultiply().multiply(a, b)
        print(ans)
    except MultiplyException as err:
        print(err, err.arg, '(', err.type, ')')

while True:
    main()
