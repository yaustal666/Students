local model = script.Parent
local RUN_ANIM_ID = "rbxassetid://507767714"
MovementTrackerService = require(game.ServerScriptService.Modules.Gameplay.MovementTrackerService)
Players = game:GetService("Players")

local runners = {}
local function startRun(humanoid)
	if runners[humanoid] then return end
	local player = Players:GetPlayerFromCharacter(humanoid.Parent)
	local mult = model:GetAttribute("Multiplier")
	MovementTrackerService.SetPlayer(player, mult)

	local animator = humanoid:FindFirstChildOfClass("Animator")
	if not animator then
		animator = Instance.new("Animator")
		animator.Parent = humanoid
	end

	local anim = Instance.new("Animation")
	anim.AnimationId = RUN_ANIM_ID

	local track = animator:LoadAnimation(anim)
	track.Looped = true
	track:Play()
	track:AdjustSpeed(1.3) -- 3x lebih cepat

	runners[humanoid] = {
		Track = track,
		LastTouch = tick()
	}
end

for _, part in ipairs(model:GetDescendants()) do
	if part:IsA("BasePart") then
		part.Touched:Connect(function(hit)
			local character = hit.Parent
			local humanoid = character and character:FindFirstChildOfClass("Humanoid")

			if humanoid then
				startRun(humanoid)
				runners[humanoid].LastTouch = tick()
			end
		end)
	end
end

task.spawn(function()
	while true do
		for humanoid, data in pairs(runners) do
			if not humanoid.Parent or tick() - data.LastTouch > 0.3 then
				data.Track:Stop()
				data.Track:Destroy()
				runners[humanoid] = nil
				local player = Players:GetPlayerFromCharacter(humanoid.Parent)
				MovementTrackerService.UnsetPlayer(player)
			end
		end
		task.wait(0.1)
	end
end)


