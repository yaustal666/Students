Players = game:GetService("Players")
local Admin = {}

local function getPlayer(UserId: number)
	return Players:GetPlayerByUserId(UserId)
end

function Admin.Kill(UserId)
    local player = getPlayer(UserId)
    local character = player.Character
    local humanoid = character:WaitForChild("Humanoid")
    humanoid.Health = 0
end

return Admin