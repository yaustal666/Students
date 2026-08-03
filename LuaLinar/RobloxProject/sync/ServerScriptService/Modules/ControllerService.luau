local CollectionService = game:GetService("CollectionService")
local ReplicatedStorage = game:GetService("ReplicatedStorage")
local CurrencyService = require(game.ServerScriptService.Modules.Core.CurrencyService)

local AddCurrencyEvent = ReplicatedStorage.remotes.AddCurrencyEvent
local buttonCooldowns = {}
AddCurrencyEvent.OnServerEvent:Connect(
	function(player, currencyName, amount, part)
		if not (part and part:IsA("BasePart") and CollectionService:HasTag(part, "CoinButton")) then return end
		if part:GetAttribute("CoinValue") ~= amount then return end
		if buttonCooldowns[part] then return end

		buttonCooldowns[part] = true
		CurrencyService.addCurrency(player, currencyName, amount)

		task.delay(4, function()
			buttonCooldowns[part] = nil
		end)
	end
)

local ControllerService = {}
return ControllerService
