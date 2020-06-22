def merge_the_tools(s, k):
    # your code goes here
    n = len(s)
    for i in range(0, n, k):
        slicedStr = s[i : i+k]
        uni =[]
        for y in slicedStr:
            if y not in uni:
                uni.append(y)
        print(''.join(map(str,uni)))

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
