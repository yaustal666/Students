local ProximityPromptService = game:GetService("ProximityPromptService")
local ServerScriptService = game:GetService("ServerScriptService")

local function getPromptAction(promptObject)
	local ancestorModel = promptObject:FindFirstAncestorWhichIsA("Model")
	local action = require(ancestorModel.Action)
	return action
end

local function onPromptTriggered(promptObject, player)
	local action = getPromptAction(promptObject)
	action.promptTrigger(promptObject, player)
end

local function onPromptHoldBegan(promptObject, player)
	local action = getPromptAction(promptObject)
	action.promptHoldBegan(promptObject, player)
end


local function onPromptHoldEnded(promptObject, player)
	local action = getPromptAction(promptObject)
	action.promptHoldEnded(promptObject, player)
end

ProximityPromptService.PromptTriggered:Connect(onPromptTriggered)
ProximityPromptService.PromptButtonHoldBegan:Connect(onPromptHoldBegan)
ProximityPromptService.PromptButtonHoldEnded:Connect(onPromptHoldEnded)