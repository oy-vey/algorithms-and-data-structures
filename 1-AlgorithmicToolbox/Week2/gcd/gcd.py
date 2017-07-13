# Uses python3
import sys

def gcd(a, b):
    if(b == 0):
        return a
    a_prime = a % b
    return gcd(b, a_prime)

if __name__ == "__main__":
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(gcd(a, b))
