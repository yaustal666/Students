-- local Player = {
--     {name = "Alex", level = 100, score = 192176}
-- }

-- local Player2 = {}

-- function Player.addPlayer (name, level, score)
--     table.insert(Player, {name = name, level = level, score = score})
-- end

-- Player.addPlayer("Mixa", 99, 318373)

-- function Player.addPlayer (self, name, level, score)
--     table.insert(self, {name = name, level = level, score = score})
-- end

-- Player.addPlayer(Player2, "Mixa", 99, 318373)

-- function Player:addPlayer (name, level, score)
--     table.insert(self, {name = name, level = level, score = score})
-- end

-- Player:addPlayer("Mixa", 99, 318373)

-- local playerMetatable = {
--     __index = {
--         addPlayer = function(self, name, level, score)
--             table.insert(self, {name = name, level = level, score = score})
--         end
--     }
-- }

-- setmetatable(Player, playerMetatable)
-- setmetatable(Player2, playerMetatable)

-- Player:addPlayer("Mixa", 99, 318373)

-- for k, v in pairs(Player) do
--     print(k, v.name, v.level, v.score)
-- end