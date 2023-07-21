def SpecialSubsequencesAG(sequence):
    s=sequence.lower()
    count=0
    result=0
    for i in s:
        if i=='a':
            count+=1
        elif i=='g':
            result+=count

    return result

sequence=input()
print(SpecialSubsequencesAG(sequence))