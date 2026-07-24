local CurrencyManager = require(script.Parent.CurrencyManager)
local button = Instance.new("Part")

button.Size = Vector3.new(6, 2, 6)
button.Position = Vector3.new(10, 4, 10)
button.BrickColor = BrickColor.new("Curry")
button.Material = Enum.Material.CrackedLava
button.Parent = workspace

local isActive = true

local function OnPlayerTouched(otherPart)
    local character = otherPart.Parent
	if not character then return end

	local player = game:GetService("Players"):GetPlayerFromCharacter(character)
	
	if not player then return end
    if not isActive then return end

    local success = CurrencyManager.addCurrency(player, "Coins", 10)
    if success then
        button.Material = Enum.Material.Carpet
        isActive = false
    else
        return
    end

    task.wait(4)
    button.Material = Enum.Material.CrackedLava
    isActive = true
end

button.Touched:Connect(OnPlayerTouched)