local Players = game:GetService("Players")
local ReplicatedStorage = game:GetService("ReplicatedStorage")
local NetworkSetup = require(game.ServerScriptService.Server.NetworkSetup)
NetworkSetup.Init()
local CurrencyManager = require(game.ServerScriptService.Server.CurrencyManager)
local MovementTracker = require(game.ServerScriptService.Server.MovementTracker)
local DataService = require(game.ServerScriptService.Server.DataService)

Players.PlayerAdded:Connect(
    function(player)
        local playerData = DataService.loadDataAsync(player)
        DataService.initPlayerSession(player, playerData)
        CurrencyManager.initPlayer(player, playerData)

        MovementTracker.initPlayer(player)
    end
)

Players.PlayerRemoving:Connect(
    function(player)
        DataService.saveDataAsync(player)
    end
)

local AddCurrencyEvent: RemoteEvent = ReplicatedStorage.remotes.AddCurrencyEvent
AddCurrencyEvent.OnServerEvent:Connect(
    function(player, currencyName, amount)
        CurrencyManager.addCurrency(player, currencyName, amount)
    end
)