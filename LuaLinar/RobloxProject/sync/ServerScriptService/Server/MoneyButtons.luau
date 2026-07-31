local CollectionService = game:GetService("CollectionService")
local CurrencyManager = require(game.ServerScriptService.Server.CurrencyManager)
local MoneyButtons = {}

local function setupCoinButton(part)
    part.Touched:Connect(
        function(otherPart)
            local character = otherPart.Parent
            if not character then return end
            local player = game:GetService("Players"):GetPlayerFromCharacter(character)
            if not player then return end
            
            CurrencyManager.addCurrency(player, "Coins", part:GetAttribute("CoinValue"))
        end
    )
end

function MoneyButtons.Init()
    for _, part in ipairs(CollectionService:GetTagged("CoinButton")) do
        setupCoinButton(part)
    end

    CollectionService:GetInstanceAddedSignal("CoinButton"):Connect(
        function(instance)
            setupCoinButton(instance)
        end
    )
end

return MoneyButtons