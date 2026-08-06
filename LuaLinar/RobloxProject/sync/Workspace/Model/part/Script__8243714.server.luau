local TweenService = game:GetService("TweenService")
local part = script.Parent

-- Store the original position and calculate the pressed distance
local originalPosition = part.Position
local PRESS_DEPTH = 0.6 -- How many studs the key drops down when pressed

-- Define the target position for the pressed state
local pressedPosition = originalPosition - Vector3.new(0, PRESS_DEPTH, 0)

-- Smooth animation configurations for a crisp, tactile switch feel
local pressInfo = TweenInfo.new(0.05, Enum.EasingStyle.Quad, Enum.EasingDirection.Out) -- Fast down stroke
local releaseInfo = TweenInfo.new(0.12, Enum.EasingStyle.Back, Enum.EasingDirection.Out) -- Springy return snap

-- Sound management setup
local sounds = {
	part:WaitForChild("KeySound1"),
	part:WaitForChild("KeySound2"),
	part:WaitForChild("KeySound3")
}
local lastSoundIndex = 0

local function playRandomKeySound()
	local nextIndex
	repeat
		nextIndex = math.random(1, #sounds)
	until nextIndex ~= lastSoundIndex

	lastSoundIndex = nextIndex
	local sound = sounds[nextIndex]
	if sound then
		-- Randomise pitch slightly to mimic real tactile switch acoustic variation
		sound.Pitch = math.random(95, 105) / 100 
		sound:Play()
	end
end

-- State Tracking Variables
local touchingParts = {}
local isPressed = false

local function updateKeyState()
	local currentlyTouched = false
	for _, _ in pairs(touchingParts) do
		currentlyTouched = true
		break
	end

	if currentlyTouched then
		if not isPressed then
			isPressed = true
			playRandomKeySound()

			-- Actuate the down-stroke
			local pressTween = TweenService:Create(part, pressInfo, {Position = pressedPosition})
			pressTween:Play()
		end
	else
		if isPressed then
			isPressed = false

			-- Return up with a crisp mechanical spring back
			local releaseTween = TweenService:Create(part, releaseInfo, {Position = originalPosition})
			releaseTween:Play()
		end
	end
end

part.Touched:Connect(function(hit)
	local character = hit.Parent
	if character and character:FindFirstChild("Humanoid") then
		touchingParts[hit] = true
		updateKeyState()
	end
end)

part.TouchEnded:Connect(function(hit)
	if touchingParts[hit] then
		touchingParts[hit] = nil
	end

	-- Small delay buffer to keep the key stable while a player walks across its surface
	task.wait(0.08)
	updateKeyState()
end)
