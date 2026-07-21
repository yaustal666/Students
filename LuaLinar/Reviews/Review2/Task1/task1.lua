local stats = {
    health = 100
}

stats.mana = 100

local seconds = io.read("n")

for i = 1, seconds do
    stats.mana = stats.mana - 2
    stats.health = stats.health + 1
end

print(stats.health)
print(stats.mana)