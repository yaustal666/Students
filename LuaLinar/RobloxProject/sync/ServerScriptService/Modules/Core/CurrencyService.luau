local DataService = require(game.ServerScriptService.Modules.Core.DataService)
local InventoryService = require(game.ServerScriptService.Modules.Core.InventoryService)

local CurrencyService = {}

function CurrencyService.GetCurrency(player, currencyName)
    local playerData = DataService.getPlayerData(player)
    if not playerData then return 0 end

    local currency = playerData[currencyName]

    if not currency then
        return false
    end

    return currency
end

function CurrencyService.addCurrency(player, currencyName, amount)
    local currency = CurrencyService.GetCurrency(player, currencyName)
    if currency == false then
        return false
    end

    local mult = InventoryService.calculateMultiplyer(player)
    local newValue = currency + amount * mult

    local success = DataService.updatePlayerData(player, currencyName, newValue)
    if success then
		local CurrencyChangedEvent: RemoteEvent = game.ReplicatedStorage.remotes.CurrencyChangedEvent
		CurrencyChangedEvent:FireClient(player, currencyName, newValue)
	end

    local leaderstats = player:FindFirstChild("leaderstats")
    if not leaderstats then return false end
    local leaderstatsCurrency = leaderstats:FindFirstChild(currencyName)
    leaderstatsCurrency.Value = newValue
    return true
end

function CurrencyService.hasCurrency(player, currencyName, amount)
    local currency: IntValue = CurrencyService.GetCurrency(player, currencyName)
    if currency.Value >= amount then
        return true
    end
    return false
end

function CurrencyService.Pay(player, currencyName, amount)
    local currency: IntValue = CurrencyService.GetCurrency(player, currencyName)
    if CurrencyService.hasCurrency(player, currencyName, amount) then
        currency.Value -= amount
        return true
    end
    return false
end

return CurrencyService