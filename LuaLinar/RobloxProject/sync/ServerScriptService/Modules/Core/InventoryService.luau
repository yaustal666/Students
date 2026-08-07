local InventoryService = {}

function InventoryService.calculateMultiplyer(player: Player, currencyName: string)
    local finalMult = 1

    for _, multiplier in ipairs(player.inventory.multipliers:GetChildren()) do
        if currencyName == multiplier:GetAttribute("CurrencyName") then
            finalMult *= multiplier.Value
        end
    end

    return finalMult
end

return InventoryService
