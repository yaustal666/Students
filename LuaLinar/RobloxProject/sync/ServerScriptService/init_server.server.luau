local NetworkSetupService = require(game.ServerScriptService.Modules.Bootstrap.NetworkSetupService)
NetworkSetupService.Init()

local CurrencyService = require(game.ServerScriptService.Modules.Economics.CurrencyService)
local InventoryService = require(game.ServerScriptService.Modules.Core.InventoryService)

local PlayerConnectionService = require(game.ServerScriptService.Modules.Core.PlayerConnectionService)

local MoneyButtonsService = require(game.ServerScriptService.Modules.Gameplay.MoneyButtonsService)
MoneyButtonsService.Init()

local ControllerService = require(game.ServerScriptService.Modules.ControllerService)