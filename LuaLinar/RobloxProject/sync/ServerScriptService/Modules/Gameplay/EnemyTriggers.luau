local CollectionService = game:GetService("CollectionService")
local Players = game:GetService("Players")
local Rooms = require(game.ServerScriptService.Modules.Gameplay.Rooms)

local triggersCooldowns = {}

local function setupEnemyTrigger(part: BasePart)
    part.Touched:Connect(
        function(otherPart)
            local character = otherPart.Parent
            if not character then return end

            local player = Players:GetPlayerFromCharacter(character)
            if not player then return end

            if triggersCooldowns[tostring(player)] == false then return end
            triggersCooldowns[tostring(player)] = false

            Rooms.handlePlayer(player, part:GetAttribute("RoomNumber"))

            print(player)
            task.wait(1)
            triggersCooldowns[tostring(player)] = true
        end
    )
end

for _, part in ipairs(CollectionService:GetTagged("EnemyTrigger")) do
    setupEnemyTrigger(part)
end

CollectionService:GetInstanceAddedSignal("EnemyTrigger"):Connect(
    function(instance)
        setupEnemyTrigger(instance)
    end
)

local Module = {}
function Module.initPlayer(player) 
    triggersCooldowns[tostring(player)] = true;
end
return Module
