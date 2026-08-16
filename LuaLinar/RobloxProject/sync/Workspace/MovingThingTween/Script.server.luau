local TweenService = game:GetService("TweenService")
local part = script.Parent

local startPosition = part.Position
local startCFrame = part.CFrame
local startTransparency = part.Transparency

local endPosition = startPosition + Vector3.new(20, 0, 0)

local tweenInfo = TweenInfo.new(
	1, 
	Enum.EasingStyle.Linear
)

local moveTween = TweenService:Create(part, tweenInfo, {Position = endPosition})

while true do
	part.Transparency = startTransparency
	task.wait(1) 

	moveTween:Play()
	moveTween.Completed:Wait()

	part.Transparency = 1
	part.Position = startPosition

	task.wait(1) 
end
