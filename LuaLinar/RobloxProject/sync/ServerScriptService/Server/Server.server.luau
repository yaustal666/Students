local CollectionService = game:GetService("CollectionService")
local Players = game:GetService("Players")
local ReplicatedStorage = game:GetService("ReplicatedStorage")
local NetworkSetup = require(game.ServerScriptService.Server.NetworkSetup)
NetworkSetup.Init()
local CurrencyManager = require(game.ServerScriptService.Server.CurrencyManager)
local InventoryManager = require(game.ServerScriptService.Server.InventoryManager)
local MoneyButtons = require(game.ServerScriptService.Server.MoneyButtons)
MoneyButtons.Init()
local MovementTracker = require(game.ServerScriptService.Server.MovementTracker)
local DataService = require(game.ServerScriptService.Server.DataService)

Players.PlayerAdded:Connect(
    function(player)
        local playerData = DataService.loadDataAsync(player)
        DataService.initPlayerSession(player, playerData)
        InventoryManager.initPlayer(player)
        CurrencyManager.initPlayer(player, playerData)
        MovementTracker.initPlayer(player)
    end
)

Players.PlayerRemoving:Connect(
    function(player)
        DataService.saveDataAsync(player)
    end
)

local AddCurrencyEvent = ReplicatedStorage.remotes.AddCurrencyEvent
local buttonCooldowns = {}
AddCurrencyEvent.OnServerEvent:Connect(
	function(player, currencyName, amount, part)
        print(player)
		if not (part and part:IsA("BasePart") and CollectionService:HasTag(part, "CoinButton")) then return end
		if part:GetAttribute("CoinValue") ~= amount then return end
		if buttonCooldowns[part] then return end

		buttonCooldowns[part] = true
		CurrencyManager.addCurrency(player, currencyName, amount)

		task.delay(4, function()
			buttonCooldowns[part] = nil
		end)
	end
)