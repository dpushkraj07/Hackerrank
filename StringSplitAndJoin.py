def split_and_join(line):
    # write your code here
    line = line.split(" ")
    nline = "-".join(line)

    return nline

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
