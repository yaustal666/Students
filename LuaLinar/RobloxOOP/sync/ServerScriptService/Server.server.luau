local CollectionService = game:GetService("CollectionService")
local PathfindingService = game:GetService("PathfindingService")
local JumpPad = require(game.ServerScriptService.Jpad)
local Treadmill = require(game.ServerScriptService.Treadmill)

for _, part in ipairs(CollectionService:GetTagged("Jbox")) do
	local jpad = JumpPad.new(part, part:GetAttribute("JumpForce"))
	jpad:Start()
end

for _, model in ipairs(CollectionService:GetTagged("Treadmill")) do
	local tmill = Treadmill.new(model, 10)
end

local part = Instance.new("Part", workspace)
part.Position = Vector3.new(10, 0, 20)
local jpad = JumpPad.new(part, 50)
jpad:Start()
