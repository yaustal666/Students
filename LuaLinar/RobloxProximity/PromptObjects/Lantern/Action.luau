
local ancestorModel = script.Parent
local soundFolder = script.Parent.Sounds

local module = {}

function module.promptTrigger(promptObject, player)
	local light = ancestorModel:FindFirstChildWhichIsA("PointLight", true)
	local emitter = ancestorModel:FindFirstChildWhichIsA("ParticleEmitter", true)

	light.Enabled = not light.Enabled
	emitter:Clear()
	emitter.Enabled = not emitter.Enabled
	promptObject.Enabled = false
	if light.Enabled == true then
		promptObject.ActionText = "Turn Off"
		soundFolder.On:Play()
		soundFolder.Burning:Play()
	else
		promptObject.ActionText = "Turn On"
		soundFolder.Burning:Stop()
		soundFolder.Off:Play()
	end

	delay(1, function()
		promptObject.Enabled = true
	end)
end

function module.promptHoldBegan(promptObject, player)
	
end

function module.promptHoldEnded(promptObject, player)
	
end

return module
