local RunService = game:GetService("RunService")

local ancestorModel = script.Parent
local valueFolder = script.Parent.Values
local soundFolder = script.Parent.Sounds

local module = {}

function module.promptTrigger(promptObject, player)
	ancestorModel.PrimaryPart:SetNetworkOwner(nil)

	local constraint = ancestorModel:FindFirstChildWhichIsA("HingeConstraint", true)

	local isOpen = valueFolder.OpenValue
	if isOpen.Value == false then
		constraint.TargetAngle = constraint.UpperAngle
		soundFolder.Open:Play()
	elseif isOpen.Value == true then
		constraint.TargetAngle = constraint.LowerAngle
		soundFolder.Close:Play()
	end

	constraint.AngularSpeed = valueFolder.OpenSpeed.Value

	promptObject.Enabled = false

	local connection
	connection = RunService.Stepped:Connect(function(t, dt)
		if constraint.TargetAngle > constraint.CurrentAngle and constraint.TargetAngle - constraint.CurrentAngle < 0.005 then
			isOpen.Value = true
			promptObject.ActionText = valueFolder.PromptTextClose.Value
			promptObject.HoldDuration = valueFolder.PromptCloseDuration.Value
			promptObject.Enabled = true
			connection:Disconnect()
			
		elseif constraint.TargetAngle < constraint.CurrentAngle and constraint.CurrentAngle - constraint.TargetAngle < 0.005 then
			isOpen.Value = false
			promptObject.ActionText = valueFolder.PromptTextOpen.Value
			promptObject.HoldDuration = valueFolder.PromptOpenDuration.Value
			promptObject.Enabled = true
			soundFolder.Close:Stop()
			soundFolder.Lock:Play()
			connection:Disconnect()
		end
	end)
end

function module.promptHoldBegan(promptObject, player)
	if ancestorModel.Name == "PrisonDoor" then
		if valueFolder.OpenValue.Value == false then
			soundFolder.Picking:Play()
		end
	end
end

function module.promptHoldEnded(promptObject, player)
	if ancestorModel.Name == "PrisonDoor" then
		soundFolder.Picking:Stop()
	end
end

return module
