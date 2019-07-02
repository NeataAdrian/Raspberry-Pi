string = [x for x in raw_input().split(" ")]
n = int(input())
nepermise = [x for x in raw_input().split(" ")]

for count, word in enumerate(string):
    for ban in nepermise:
        if ban in word:
            string[int(count)] = string[int(count)].replace(ban, "*"*len(ban))

print(" ".join(string))