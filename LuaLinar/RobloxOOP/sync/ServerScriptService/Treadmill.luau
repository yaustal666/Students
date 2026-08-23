local Treadmill = {}
Treadmill.__index = Treadmill

function Treadmill.new(model, multiplier)
	local mill = {}
	setmetatable(mill, Treadmill)
	mill.Model = model
	mill.Multiplier = multiplier
	mill.Runners = {}
	mill.RUN_ANIM_ID = "rbxassetid://507767714"
	
	mill:Start()
	return mill	
end

function Treadmill:StartRun(humanoid)
	if self.Runners[humanoid] then return end

	local animator = humanoid:FindFirstChildOfClass("Animator")
	if not animator then
		animator = Instance.new("Animator")
		animator.Parent = humanoid
	end

	local anim = Instance.new("Animation")
	anim.AnimationId = self.RUN_ANIM_ID

	local track = animator:LoadAnimation(anim)
	track.Looped = true
	track:Play()
	track:AdjustSpeed(1.3)

	self.Runners[humanoid] = {
		Track = track,
		LastTouch = tick()
	}
end

function Treadmill:Start()
	for _, part in ipairs(self.Model:GetDescendants()) do
		if part:IsA("BasePart") then
			part.Touched:Connect(function(hit)
				local character = hit.Parent
				local humanoid = character and character:FindFirstChildOfClass("Humanoid")

				if humanoid then
					self:StartRun(humanoid)
					self.Runners[humanoid].LastTouch = tick()
				end
			end)
		end
	end

	task.spawn(function()
		while true do
			for humanoid, data in pairs(self.Runners) do
				if not humanoid.Parent or tick() - data.LastTouch > 0.3 then
					data.Track:Stop()
					data.Track:Destroy()
					self.Runners[humanoid] = nil
				end
			end
			task.wait(0.1)
		end
	end)
end

return Treadmill