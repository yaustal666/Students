local Players = game:GetService("Players")
local PlayerSetupService = require(game.ServerScriptService.Modules.Bootstrap.PlayerSetupService)
local DataService = require(game.ServerScriptService.Modules.Core.DataService)
local MovementTrackerService = require(game.ServerScriptService.Modules.Gameplay.MovementTrackerService)

Players.PlayerAdded:Connect(
    function(player)
        local playerData = DataService.loadDataAsync(player)
        DataService.initPlayerSession(player, playerData)
        PlayerSetupService.initPlayer(player, playerData)
		MovementTrackerService.initPlayer(player)
    end
)

Players.PlayerRemoving:Connect(
    function(player)
        DataService.saveDataAsync(player)
    end
)

local PlayerConnectionService = {}
return PlayerConnectionService
