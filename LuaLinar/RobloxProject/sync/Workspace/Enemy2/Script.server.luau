local RunService = game:GetService("RunService")
local enemy = script.Parent.Humanoid
local target = game.Workspace.Target

RunService.Heartbeat:Connect(function(dt)
	enemy:MoveTo(target.Position)
end)