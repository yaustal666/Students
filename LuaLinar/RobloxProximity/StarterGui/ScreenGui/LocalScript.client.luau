local TweenService = game:GetService("TweenService")

local button = script.Parent.ImageButton
local frame = script.Parent.Frame

local pos = frame.Position 
local hidePosition = UDim2.new(pos.X.Scale, 0, 1, 0)

frame.Position = hidePosition

local tweenInfo = TweenInfo.new(0.2, Enum.EasingStyle.Linear)
local openTween = TweenService:Create(frame, tweenInfo, {Position = pos})
local closeTween = TweenService:Create(frame, tweenInfo, {Position = hidePosition})
local isOpen = false

local isActive = true

local function handleButtonClick()
	if not isActive then return end
	isActive = false
	
	if not isOpen then
		openTween:Play()
		openTween.Completed:Wait()
		isOpen = true
	
	elseif isOpen then
		closeTween:Play()
		closeTween.Completed:Wait()
		isOpen = false
	end
	
	delay(0.4, function()
		isActive = true
	end)
end

button.MouseButton1Click:Connect(handleButtonClick)