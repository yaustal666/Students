local CollectionService = game:GetService("CollectionService")
local Players = game:GetService("Players")
local Enemy = require(game.ServerScriptService.Modules.Gameplay.Enemy)

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

            local enemyName = part:GetAttribute("EnemyName")
            Enemy.playerTrigger(player, enemyName)

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
