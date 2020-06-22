def minion_game(string):
    # your code goes here
    vowel = 'AEIOU'
    Kscore = 0
    Sscore = 0
    for i in range(len(string)):
        if string[i] in vowel:
            Kscore += (len(string) - i)
        else:
            Sscore += (len(string) - i)

    if Kscore > Sscore:
        print('Kevin'+' '+str(Kscore))
    elif Sscore > Kscore:
        print('Stuart'+' '+str(Sscore))
    else:
        print("Draw")



if __name__ == '__main__':
