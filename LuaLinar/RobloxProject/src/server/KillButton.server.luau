local button = Instance.new("Part")

button.Size = Vector3.new(6, 2, 6)
button.Position = Vector3.new(10, 4, 10)
button.BrickColor = BrickColor.new("Curry")
button.Material = Enum.Material.CrackedLava
button.Parent = workspace

local isActive = true

local function KillPlayer(humanoid) 
    humanoid.Health = 0
end

local function SwitchMaterial(part)
    button.Material = Enum.Material.Carpet
end

local function OnPlayerTouched(otherPart)
    local character = otherPart.Parent
    local humanoid = character:FindFirstChild("Humanoid")

    if humanoid and isActive then 
        KillPlayer(humanoid)
        SwitchMaterial(button)
        isActive = false
    end

    task.wait(8)
    button.Material = Enum.Material.CrackedLava
    isActive = true
end

button.Touched:Connect(OnPlayerTouched)