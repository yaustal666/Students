local CollectionService = game:GetService("CollectionService")

local function setupKillObject(part: BasePart)
    part.Touched:Connect(
        function(otherPart)
            local character = otherPart.Parent
            if not character then return end
            local humanoid = character:FindFirstChild("Humanoid")
            if humanoid then
                humanoid.Health = 0
            end
        end
    )
end


for _, part in ipairs(CollectionService:GetTagged("KillObject")) do
    setupKillObject(part)
end

CollectionService:GetInstanceAddedSignal("KillObject"):Connect(
    function(instance)
        setupKillObject(instance)
    end
)

local Module = {}

return Module