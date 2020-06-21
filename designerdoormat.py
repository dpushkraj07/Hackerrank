n,m = map(int,input().split())

pattern = ''
pat = []

for i in range(n//2):
    pattern = (('.|.')*(2*i+1)).center(m,'-')
    pat.append(pattern)
print('\n'.join(pat + ['WELCOME'.center(m,'-')] + pat[::-1]))
