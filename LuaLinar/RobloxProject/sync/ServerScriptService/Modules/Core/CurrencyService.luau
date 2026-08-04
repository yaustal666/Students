local DataService = require(game.ServerScriptService.Modules.Core.DataService)
local InventoryService = require(game.ServerScriptService.Modules.Core.InventoryService)

local Module = {}

function Module.GetCurrency(player, currencyName)
    local playerData = DataService.getPlayerData(player)
    if not playerData then return 0 end

    local currency = playerData[currencyName]
    if not currency then return false end

    return currency
end

function Module.addCurrency(player, currencyName, amount)
    local currency = Module.GetCurrency(player, currencyName)
    if currency == false then return false end

    local mult = InventoryService.calculateMultiplyer(player)
    local newValue = currency + amount * mult
    local success = DataService.updatePlayerData(player, currencyName, newValue)
    if not success then return false end

    local CurrencyChangedEvent: RemoteEvent = game.ReplicatedStorage.remotes.CurrencyChangedEvent
    CurrencyChangedEvent:FireClient(player, currencyName, newValue)

    local leaderstats = player:FindFirstChild("leaderstats")
    if not leaderstats then return false end

    local leaderstatsCurrency = leaderstats:FindFirstChild(currencyName)
    leaderstatsCurrency.Value = newValue
    return true
end

function Module.hasCurrency(player, currencyName, amount)
    local currency: IntValue = Module.GetCurrency(player, currencyName)
    if currency.Value >= amount then return true end
    return false
end

function Module.Pay(player, currencyName, amount)
    local currency: IntValue = Module.GetCurrency(player, currencyName)
    if Module.hasCurrency(player, currencyName, amount) then
        currency.Value -= amount
        return true
    end
    return false
end

return Module