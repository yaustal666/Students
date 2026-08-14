local RunService = game:GetService("RunService")
local wall = script.Parent.HumanoidRootPart
local humanoid = script.Parent.Humanoid

task.wait(2)
humanoid:MoveTo(wall.Position + Vector3.new(40, 0, 0))