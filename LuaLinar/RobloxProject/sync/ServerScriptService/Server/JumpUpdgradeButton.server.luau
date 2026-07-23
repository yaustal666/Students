local LogService = game:GetService("LogService")
local RunService = game:GetService("RunService")

local jump = Instance.new("Part")
jump.Parent = workspace
jump.Size = Vector3.new(4, 3, 4)
jump.Position = Vector3.new(20, 3, 10)
 
local function upjump(otherPart)
    local character = otherPart.Parent
    local humanoid = character:FindFirstChild("Humanoid")
    
    if humanoid then
        humanoid.JumpHeight = 100 
        jump.CanCollide = false
    else
        LogService:Error("Not player!")
    end
end

jump.Touched:Connect(upjump)

RunService.Heartbeat:Connect()