local CollectionService = game:GetService("CollectionService")
local CurrencyManager = require(script.Parent.CurrencyManager)

local isActive = true

local function setupCoinButton(part)
    part.Touched:Connect (
        function(otherPart)
            local character = otherPart.Parent
            if not character then return end

            local player = game:GetService("Players"):GetPlayerFromCharacter(character)
            
            if not player then return end
            if not isActive then return end

            local success = CurrencyManager.addCurrency(player, "Coins", part:GetAttribute("CoinValue"))
            if success then
                part.Material = Enum.Material.Carpet
                isActive = false
            else
                return
            end

            task.wait(4)
            part.Material = Enum.Material.CrackedLava
            isActive = true
        end
    )
end

for _, part in ipairs(CollectionService:GetTagged("CoinButton")) do
    setupCoinButton(part)
end

CollectionService:GetInstanceAddedSignal("CoinButton"):Connect(
    function(instance)
        setupCoinButton(instance)
    end
)