def is_pangram(s):
    count = {}
    for x in [x.lower() for x in s if x.isalpha()]:
        if x in count:
            count[x]+=1
        else:
            count[x]=1
    return True if len(count)==26 else False

print(is_pangram(input('Enter a sentence you want to check:')))