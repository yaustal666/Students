local CollectionService = game:GetService("CollectionService")
local ReplicatedStorage = game:GetService("ReplicatedStorage")
local CurrencyChangedEvent = ReplicatedStorage:WaitForChild("remotes"):WaitForChild("CurrencyChangedEvent")

local walls = {}

local function checkWalls(currencyName, amount)
	for _, part in ipairs(walls) do
		local threshold = part:GetAttribute("Threshold")
		if threshold and amount >= threshold then
			part.Transparency = 1
            part.CanTouch = false
		end
	end
end

for _, wall in CollectionService:GetTagged("Wall") do
    table.insert(walls, wall)
end

CollectionService:GetInstanceAddedSignal("Wall"):Connect(
    function(wall)
        table.insert(walls, wall)
    end
)

CurrencyChangedEvent.OnClientEvent:Connect(checkWalls)