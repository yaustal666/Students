local CollectionService = game:GetService("CollectionService")
local Players = game:GetService("Players")
local CurrencyService = require(game.ServerScriptService.Modules.Core.CurrencyService)

local function setupCoinButton(part: BasePart)
    part.Touched:Connect(
        function(otherPart)
            local character = otherPart.Parent
            if not character then return end

            local player = Players:GetPlayerFromCharacter(character)
            if not player then return end
            
            CurrencyService.addCurrency(
                player, 
                "Coins", 
                part:GetAttribute("CoinValue")
            )
        end
    )
end

local Module = {}

function Module.Init()
    for _, part in ipairs(CollectionService:GetTagged("CoinButton")) do
        setupCoinButton(part)
    end

    CollectionService:GetInstanceAddedSignal("CoinButton"):Connect(
        function(instance)
            setupCoinButton(instance)
        end
    )
end

return Module