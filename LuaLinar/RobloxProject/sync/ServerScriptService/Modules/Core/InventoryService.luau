local InventoryService = {}

function InventoryService.calculateMultiplyer(player)
    return player.inventory:FindFirstChild("SpeedMultiplier").Value
end

return InventoryService
