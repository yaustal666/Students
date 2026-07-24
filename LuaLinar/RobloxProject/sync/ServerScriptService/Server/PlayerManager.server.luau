local Players = game:GetService("Players")
local CurrencyManager = require(script.Parent.CurrencyManager)

local function OnPlayerAdded(player)
    local success = CurrencyManager.initPlayer(player)
end

Players.PlayerAdded:Connect(OnPlayerAdded)