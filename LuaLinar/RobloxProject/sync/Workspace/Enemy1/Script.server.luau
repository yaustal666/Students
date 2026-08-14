local RunService = game:GetService("RunService")
local enemy = script.Parent
local target = game.Workspace.Target

local speed = 1
RunService.Heartbeat:Connect(function(dt)
	enemy.Position = enemy.Position:Lerp(target.Position, speed / 1000)
end)