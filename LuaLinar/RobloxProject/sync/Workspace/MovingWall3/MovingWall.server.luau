local TweenService = game:GetService("TweenService")
local wall = script.Parent
local startPosition = wall.Position

local animationSettings = TweenInfo.new(
	10, 
	Enum.EasingStyle.Exponential,
	Enum.EasingDirection.Out,
	5,
	true,
	0.5	
)

local anim = TweenService:Create(wall, animationSettings, {Position = wall.Position + Vector3.new(80, 0, 0)})

anim:Play()

--while true do
--	task.wait(3)
	
--	anim:Play()
--	anim.Completed:Wait()
	
	
--	wall.Position = startPosition
--end
