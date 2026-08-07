local CollectionService = game:GetService("CollectionService")
local Players = game:GetService("Players")
local CurrencyService = require(game.ServerScriptService.Modules.Economics.CurrencyService)
local SpawnLocation = game.workspace.SpawnLocation

local buttonCooldowns = {}

local function setupCoinButton(part: BasePart)
    part.Touched:Connect(
        function(otherPart)
            local character = otherPart.Parent
            if not character then return end

            local player = Players:GetPlayerFromCharacter(character)
            if not player then return end

            if buttonCooldowns[tostring(player)] == false then return end
            buttonCooldowns[tostring(player)] = false

            CurrencyService.addCurrency(
                player, 
                "Coins", 
                part:GetAttribute("CoinValue")
            )
            
            character:PivotTo(SpawnLocation.CFrame + Vector3.new(0, 5, 0))
            task.wait(1)
            buttonCooldowns[tostring(player)] = true
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


local Module = {}

function Module.initPlayer(player) 
    buttonCooldowns[tostring(player)] = true;
end

return Module