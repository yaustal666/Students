local player = game.Players.LocalPlayer
local coinLabel = script.Parent.Frame.CoinLabel

local leaderstats = player:WaitForChild("leaderstats")
local coins = leaderstats:WaitForChild("Coins")

local function updateCoinLable()
    coinLabel.Text = "💰 " .. tostring(coins.Value)
end

updateCoinLable()

coins:GetPropertyChangedSignal("Value"):Connect(updateCoinLable)
