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