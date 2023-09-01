def main():
    t = int(input())
    for _ in range(t):
        n,d = map(int, input().split())
        ls= list(map(int, input().split()))
        print(" ".join(map(str, ls[d:] + ls[:d])))
    
main()