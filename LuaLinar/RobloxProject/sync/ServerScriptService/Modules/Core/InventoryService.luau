local InventoryService = {}

function InventoryService.calculateMultiplyer(player: Player)
    return player.inventory:FindFirstChild("SpeedMultiplier").Value
end

return InventoryService
