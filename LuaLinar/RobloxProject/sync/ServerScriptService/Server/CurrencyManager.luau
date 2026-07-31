local DataService = require(game.ServerScriptService.Server.DataService)
local InventoryManager = require(game.ServerScriptService.Server.InventoryManager)

local CurrencyManager = {}

function CurrencyManager.initPlayer(player, playerData)
    local leaderstats = Instance.new("Folder", player)
    leaderstats.Name = "leaderstats"

    for currencyName, value in pairs(playerData) do
        local currency = Instance.new("IntValue", leaderstats)
        currency.Name = currencyName
        currency.Value = value
    end
end

function CurrencyManager.GetCurrency(player, currencyName)
    local playerData = DataService.getPlayerData(player)
    if not playerData then return 0 end

    local currency = playerData[currencyName]

    if not currency then
        return false
    end

    return currency
end

function CurrencyManager.addCurrency(player, currencyName, amount)
    local currency = CurrencyManager.GetCurrency(player, currencyName)
    if currency == false then
        return false
    end

    local mult = InventoryManager.calculateMultiplyer(player)
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

-- функция проверки достаточно ли валюты
function CurrencyManager.hasCurrency(player, currencyName, amount)
    local currency: IntValue = CurrencyManager.GetCurrency(player, currencyName)
    if currency.Value >= amount then
        return true
    end
    return false
end

-- функция вычета валюты, например при покупке
function CurrencyManager.Pay(player, currencyName, amount)
    local currency: IntValue = CurrencyManager.GetCurrency(player, currencyName)
    if CurrencyManager.hasCurrency(player, currencyName, amount) then
        currency.Value -= amount
        return true
    end
    return false
end

return CurrencyManager