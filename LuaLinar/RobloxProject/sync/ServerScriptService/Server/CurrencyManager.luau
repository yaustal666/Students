local LogService = game:GetService("LogService")
local CurrencyManager = {}

local CurrencyData = {
    Coins = {
        defaultValue = 0,
        displayName = "Coins",
    }
}

function CurrencyManager.initPlayer(player)
    local leaderstats = Instance.new("Folder")
    leaderstats.Name = "leaderstats"
    leaderstats.Parent = player

    for currencyName, config in pairs(CurrencyData) do
        local currency = Instance.new("IntValue")
        currency.Parent = leaderstats
        currency.Name = currencyName
        currency.Value = config.defaultValue
    end
end

function CurrencyManager.GetCurrency(player, currencyName)
    local leaderstats = player:FindFirstChild("leaderstats")
    if not leaderstats then 
        return false
    end

    local currency = leaderstats:FindFirstChild(currencyName)

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

    currency.Value += amount
    LogService:Info(`{player.Name} received {amount} {currencyName}. Total {currencyName}: {currency.Value}`)
    return true
end

-- функция проверки достаточно ли валюты
-- функция вычета валюты, например при покупке

return CurrencyManager