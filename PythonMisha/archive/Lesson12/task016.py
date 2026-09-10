# a = [int(i) for i in input().split(",")]
# b = [i*i for i in a if i % 2 == 1]
# print(b)

# print([int(i) * int(i) for i in input().split(",") if int(i) % 2 == 1])

print({i:int(i) for i in range(10)})

users = [["Alex", 10], ["Marti", 2]]
print({i[0] : i[1] for i in users})