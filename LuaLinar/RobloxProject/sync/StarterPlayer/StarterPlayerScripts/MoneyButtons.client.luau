local CollectionService = game:GetService("CollectionService")
local ReplicatedStorage = game:GetService("ReplicatedStorage")
local AddCurrencyEvent: RemoteEvent = ReplicatedStorage.remotes.AddCurrencyEvent

local isActive = true

local function setupCoinButton(part)
    part.Touched:Connect(
        function(otherPart)
            local character = otherPart.Parent
            if not character then return end

            local player = game:GetService("Players"):GetPlayerFromCharacter(character)
            
            if not player then return end
            if not isActive then return end

            AddCurrencyEvent:FireServer("Coins", part:GetAttribute("CoinValue"))

            part.Material = Enum.Material.Carpet
            isActive = false
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