def gen(i):
    return i ** 2

def main():
    print("evil")
    n = int(input())
    for i in range(n+1):   #includes n. For n = 5, it generates 5 numbers. Without +, it would generate only 4
        print(gen(i))