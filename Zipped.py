# Enter your code here. Read input from STDIN. Print output to STDOUT

m,n = map(int,(input().split()))
sub = []
for _ in range(n):
    sub.append(map(float,input().split()))

for i in zip(*sub):
    print(sum(i)/len(i))
