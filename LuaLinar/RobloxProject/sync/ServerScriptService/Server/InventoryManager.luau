local InventoryManager = {}

function InventoryManager.initPlayer(player)
    local inventory = Instance.new("Folder")
    inventory.Name = "inventory"
    inventory.Parent = player

	local currency = Instance.new("NumberValue", inventory)
	currency.Name = "SpeedMultiplier"
    currency.Value = 2.5
end

function InventoryManager.calculateMultiplyer(player)
    return player.inventory:FindFirstChild("SpeedMultiplier").Value
end

return InventoryManager
