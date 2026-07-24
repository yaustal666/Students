local player = game.Players.LocalPlayer
local coinLabel = script.Parent.Frame.CoinLabel

local leaderstats = player:WaitForChild("leaderstats")

local function updateCoinDisplay()
    local coins = leaderstats:FindFirstChild("Coins")
    if coins then
        coinLabel.Text = "💰 " .. tostring(coins.Value)
    end
end

updateCoinDisplay()

local coins = leaderstats:FindFirstChild("Coins")
if coins then
    coins:GetPropertyChangedSignal("Value"):Connect(updateCoinDisplay)
end
