local CollectionService = game:GetService("CollectionService")
local RunService = game:GetService("RunService")
local Rooms = require(game.ServerScriptService.Modules.Gameplay.Rooms)

local enemies = {}

local function calculateDistance(pos1: Vector3, pos2: Vector3)
    return (pos1 - pos2).Magnitude
end

local function findClosestPlayer(part: Vector3, players)
    local idx = 1
    local max = -1
    for i, player in ipairs(players) do
        if calculateDistance(part, player.Character.HumanoidRootPart.Position) > max then
            idx = i
        end
    end

    return players[idx]
end

local function findTarget(part)
	print("Enemy find works")

    while task.wait(0.2) do 
        local enemyName = part:GetAttribute("EnemyName")
        local playersInRoom = Rooms.getPlayersInRoom(part:GetAttribute("RoomNumber"))

        if next(playersInRoom) == nil then
			enemies[enemyName]["active"] = false
		else
			enemies[enemyName]["active"] = true
            enemies[enemyName]["target"] = findClosestPlayer(part.HumanoidRootPart.Position, playersInRoom)
        end
    end
end

local function setupEnemy(part)
    local enemyName = part:GetAttribute("EnemyName")
	local startPosition = part:WaitForChild("HumanoidRootPart").Position
    enemies[enemyName] = {}
    enemies[enemyName]["active"] = false
	enemies[enemyName]["target"] = nil
	task.spawn(function()
        findTarget(part)
    end)
	print("Enemy run")

	local enemyHumanoid = part.Humanoid
	
	RunService.Heartbeat:Connect(
		function(dt)
	        if not enemies[enemyName]["active"] then
	            enemyHumanoid:MoveTo(startPosition)
			else
				local targetPosition = enemies[enemyName]["target"].Character.HumanoidRootPart.Position
				enemyHumanoid:MoveTo(targetPosition)
	        end    
    end)
end


for _, part in ipairs(CollectionService:GetTagged("Enemy")) do
	print("Enemy found")
	setupEnemy(part)
end

CollectionService:GetInstanceAddedSignal("Enemy"):Connect(
    function(instance)
		setupEnemy(instance)
    end
)

local module = {}
return module

