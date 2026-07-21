local stats = {
    health = 100
}
-- То же самое что и в прошлый раз, но дополнительно вначале вводится два числа
-- Первое - хп игрока, нужно его поменять
-- Второе - максимальное хп, то есть если изначальное хп 10, а максимальное 20
-- и ввели 50 секунд, то здоровье все равно останется 20
-- Также теперь надо проверять, что мана не ушла в отрицательное значение

-- Все ок

stats.mana = 100
stats.health = io.read("n")
stats.maxHealth = io.read("n")

local seconds = io.read("n")

for i = 1, seconds do
    stats.mana = stats.mana - 2
    if stats.mana < 0 then
        stats.mana = 0
        break
    end

    stats.health = stats.health + 1
    if stats.health > stats.maxHealth then
        stats.health = stats.maxHealth
        break
    end
end

print(stats.health)
print(stats.mana)
