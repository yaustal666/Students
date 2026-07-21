local part = script.Parent
local clickDetector = part:WaitForChild("ClickDetector")

local function onPartClicked(player)
	print(player.Name .. " clicked the part!")

	part.BrickColor = BrickColor.random()
end

clickDetector.MouseClick:Connect(onPartClicked)