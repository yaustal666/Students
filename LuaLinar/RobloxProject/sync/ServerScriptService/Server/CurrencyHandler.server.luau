local Players = game:GetService("Players")
local LogService = game:GetService("LogService")

local function OnPlayerConnected(player)
    local leaderstats = Instance.new("Folder")
    leaderstats.Name = "leaderstats"
    leaderstats.Parent = player

    local coins = Instance.new("IntValue")
    coins.Name = "Coins"
    coins.Parent = leaderstats
    coins.Value = 0

    LogService:Info(`{player.Name} joined with {coins.Value} coins`)
end

Players.PlayerAdded:Connect(OnPlayerConnected)

function _G.addCoins(player, amount)
    local leaderstats = player:FindFirstChild("leaderstats")
    local coins = leaderstats:FindFirstChild("Coins")

    if coins then
        coins.Value += amount
        LogService:Info(`{player.Name} received {amount} coins. Total coins: {coins.Value}`)
        return true
    end

    return false
end
