local Players = game:GetService("Players")
local CurrencyManager = require(game.ServerScriptService.Server.CurrencyManager)
local MovementTracker = require(game.ServerScriptService.Server.MovementTracker)

Players.PlayerAdded:Connect(
    function(player)
        CurrencyManager.initPlayer(player)
        MovementTracker.initPlayer(player)
    end
)