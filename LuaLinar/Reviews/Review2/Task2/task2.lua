local stats = {
    health = 100
}

stats.mana = 100
stats.minHealth = 10     -- начальное хп
stats.maxHealth = 20     -- максимальное хп
stats.health = stats.minHealth

local seconds = io.read("n")

for i = 1, seconds do
    stats.mana = stats.mana - 2
    if stats.mana < 0 then
        stats.mana = 0
    end

    stats.health = stats.health + 1
    if stats.health > stats.maxHealth then
        stats.health = stats.maxHealth
    end
end

print(stats.health)
print(stats.mana)