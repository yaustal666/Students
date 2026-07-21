-- Куда отправить игрока?

local levels = {
    level1 = {
        name = "Forest", difficulty = 2,
        enemies = {
            "Goblin",
            "Wolf",
            boss = {
                name = "Hobgoblin, wolf-rider",
                reward = "Big club"
            }
        }
    },
    level2 = {
        name = "Cave", difficulty = 4,
        enemies = {
            "Bat",
            "Spider",
            "Slime",
            boss = {
                name = "Giga-Slime",
                reward = "SlimyPants"
            }
        }
    },
    level3 = {
        name = "Castle", difficulty = 5,
        enemies = {
            "Knight",
            "Dragon",
            boss = {
                name = "Elder Dragon",
                reward = "Elder Dragon's scale"
            }
        }
    }
}

-- На вход подается имя игрока и его уровень
-- В зависимости от уровня игрока он отправляется на соответсвующий уровень игры
-- 0 - 10 - level1, 11 - 25 - level2, 26 - 50 - level3
-- нужно составить для игрока сообщение следующего вида
-- _playerName_ goes to level _levelName_
-- You will face _enemiesNames_ there
-- Kill the _bossName_ to gather _bossReward_
-- dificculty: _levelDifficulty_

local function getLevelKey(playerLevel)
    if playerLevel >= 0 and playerLevel <= 10 then
        return "level1"
    end

    if playerLevel >= 11 and playerLevel <= 25 then
        return "level2"
    end

    if playerLevel >= 26 and playerLevel <= 50 then
        return "level3"
    end

    return nil 
end


local function sendPlayerToLevel(playerName, playerLevel)
    local levelKey = getLevelKey(playerLevel)
    if not levelKey then
        return playerName .. ": уровень " .. playerLevel .. " вне допустимого диапазона (0-50)"
    end

    local level = levels[levelKey]

    local enemiesStr = ""
    for _, enemy in ipairs(level.enemies) do
        enemiesStr = enemiesStr .. enemy .. " "
    end

    local boss = level.enemies.boss

    return playerName .. " goes to level " .. level.name .. "\n"
        .. "You will face " .. enemiesStr .. " there\n"
        .. "Kill the " .. boss.name .. " to gather " .. boss.reward .. "\n"
        .. "dificculty: " .. level.difficulty
end

print(sendPlayerToLevel("Hero", 5))
print()
print(sendPlayerToLevel("Warrior", 15))
print()
print(sendPlayerToLevel("Champion", 40))
print()
print(sendPlayerToLevel("Ghost", 99))


