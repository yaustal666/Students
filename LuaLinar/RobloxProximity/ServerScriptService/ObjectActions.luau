local RunService = game:GetService("RunService")

local ObjectActions = {}

-- Actions for when prompt is triggered
function ObjectActions.promptTriggeredActions(promptObject, player)
	-- Locate model/folders related to the prompt object
	local ancestorModel = promptObject:FindFirstAncestorWhichIsA("Model")
	local valueFolder = ancestorModel:FindFirstChild("Values")
	local soundFolder = ancestorModel:FindFirstChild("Sounds")

	-- StandardDoor or PrisonDoor
	if ancestorModel.Name == "StandardDoor" or ancestorModel.Name == "PrisonDoor" then
		-- Assign primary part network ownership to server
		ancestorModel.PrimaryPart:SetNetworkOwner(nil)

		-- Get the constraint which operates the door
		local constraint = ancestorModel:FindFirstChildWhichIsA("HingeConstraint", true)

		-- Open or close the door based on its current state
		local isOpen = valueFolder.OpenValue
		if isOpen.Value == false then
			constraint.TargetAngle = constraint.UpperAngle
			soundFolder.Open:Play()
		elseif isOpen.Value == true then
			constraint.TargetAngle = constraint.LowerAngle
			soundFolder.Close:Play()
		end

		-- Activate the hinge servo
		constraint.AngularSpeed = 0.5

		-- Disable the prompt while door is opening or closing
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

		-- Lantern
	elseif ancestorModel.Name == "Lantern" then
		-- Get visual objects for the light effect
		local light = ancestorModel:FindFirstChildWhichIsA("PointLight", true)
		local emitter = ancestorModel:FindFirstChildWhichIsA("ParticleEmitter", true)

		-- Turn the lantern on or off
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

		-- After a short delay, re-enable the prompt
		delay(2, function()
			promptObject.Enabled = true
		end)

		-- Bench
	elseif ancestorModel.Name == "Bench" then
		-- Get the seat related to the prompt
		local seat = promptObject.Parent:FindFirstChildWhichIsA("Seat")
		local character = player.Character
		local humanoid = character:WaitForChild("Humanoid")

		seat:GetPropertyChangedSignal("Occupant"):Connect(function()
			if seat.Occupant then
				promptObject.Enabled = false
			else
				promptObject.Enabled = true
				-- Disable seat when vacant to prevent sitting without using proximity prompt
				seat.Disabled = true
			end
		end)

		-- If seat is not occupied and player is not already sitting, enable seat and make player sit
		if not seat.Occupant and not humanoid.Sit then
			seat.Disabled = false
			seat:Sit(humanoid)
		end

		-- HiddenDoor
	elseif ancestorModel.Name == "HiddenDoor" then
		-- Assign primary part network ownership to server
		ancestorModel.PrimaryPart:SetNetworkOwner(nil)

		-- Get the constraint which operates the door
		local constraint = ancestorModel:FindFirstChildWhichIsA("PrismaticConstraint", true)

		-- Open or close the door based on its current state
		local isOpen = valueFolder.OpenValue
		if isOpen.Value == false then
			constraint.TargetPosition = 4.5
			soundFolder.Slide:Play()
		elseif isOpen.Value == true then
			constraint.TargetPosition = 0
			soundFolder.Slide:Play()
		end

		-- Disable the prompt while door is opening or closing
		promptObject.Enabled = false

		-- Track door position
		local connection
		connection = RunService.Stepped:Connect(function(t, dt)
			if constraint.TargetPosition > constraint.CurrentPosition and constraint.TargetPosition - constraint.CurrentPosition < 0.005 then
				isOpen.Value = true
				promptObject.Enabled = true
				soundFolder.Slide:Stop()
				soundFolder.SlideStop:Play()
				connection:Disconnect()
			elseif constraint.TargetPosition < constraint.CurrentPosition and constraint.CurrentPosition - constraint.TargetPosition < 0.005 then
				isOpen.Value = false
				promptObject.Enabled = true
				soundFolder.Slide:Stop()
				soundFolder.SlideStop:Play()
				connection:Disconnect()
			end
		end)

		-- Elevator
	elseif ancestorModel.Name == "Switch" then
		-- Get the elevator model
		local elevator = ancestorModel:FindFirstAncestor("Elevator")

		-- Get the constraint which operates the elevator
		local constraint = elevator:FindFirstChildWhichIsA("PrismaticConstraint", true)

		-- Function to enable or disable all related elevator switch prompts
		local function togglePrompts()
			local elevatorChildren = elevator:GetChildren()
			for _, child in pairs(elevatorChildren) do
				if child.Name == "Switch" then
					local promptObject = child:FindFirstChildWhichIsA("ProximityPrompt", true)
					promptObject.Enabled = not promptObject.Enabled
				end
			end
		end

		-- Handle operational switches
		if valueFolder.Broken.Value == false then
			-- Raise or lower the elevator based on its current state
			local isMoving = elevator.Values.MovingValue
			local isRaised = elevator.Values.RaisedValue

			-- Return if elevator is in motion
			if isMoving.Value == true then return end

			-- Set elevator target position
			if isRaised.Value == false then
				constraint.TargetPosition = constraint.UpperLimit
			else
				constraint.TargetPosition = constraint.LowerLimit
			end

			-- Start elevator motion
			isMoving.Value = true
			constraint.Speed = elevator.Values.SpeedValue.Value
			elevator.Sounds.MovingStart:Play()
			elevator.Sounds.Moving:Play()

			-- Disable all related elevator switches while platform is moving
			togglePrompts()

			-- Track elevator position
			local connection
			connection = RunService.Stepped:Connect(function(t, dt)
				if math.abs(constraint.TargetPosition - constraint.CurrentPosition) < 0.005 then
					isMoving.Value = false
					isRaised.Value = not isRaised.Value
					elevator.Sounds.Moving:Stop()
					elevator.Sounds.MovingStop:Play()
					connection:Disconnect()
					-- Enable all related elevator switches
					togglePrompts()
				end
			end)

			-- Handle broken switches
		elseif valueFolder.Broken.Value == true then
			local emitter = ancestorModel:FindFirstChildWhichIsA("ParticleEmitter", true)
			emitter:Emit(50)
			soundFolder.Press:Play()
			soundFolder.Broken:Play()
		end
	end
end

-- Actions for when prompt hold begins
function ObjectActions.promptHoldBeganActions(promptObject, player)
	-- Locate model/folders related to the prompt object
	local ancestorModel = promptObject:FindFirstAncestorWhichIsA("Model")
	local valueFolder = ancestorModel:FindFirstChild("Values")
	local soundFolder = ancestorModel:FindFirstChild("Sounds")

	-- PrisonDoor
	if ancestorModel.Name == "PrisonDoor" then
		if valueFolder.OpenValue.Value == false then
			soundFolder.Picking:Play()
		end
	end
end

-- Actions for when prompt hold ends
function ObjectActions.promptHoldEndedActions(promptObject, player)
	-- Locate model/folders related to the prompt object
	local ancestorModel = promptObject:FindFirstAncestorWhichIsA("Model")
	local soundFolder = ancestorModel:FindFirstChild("Sounds")

	-- PrisonDoor
	if ancestorModel.Name == "PrisonDoor" then
		soundFolder.Picking:Stop()
	end
end

return ObjectActions