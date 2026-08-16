local RunService = game:GetService("RunService")
local wall = script.Parent

local startPosition = wall.CFrame
local timer = 3
local speed = 10
local a = 0

local isActive = true
local side = true
local cooldown = 3
local b = 0

local function respawnCooldown(dt)
	if not isActive then
		b += dt
		if b > cooldown then
			b = 0
			isActive = true
		end
	end
end

local function move(dt)
	if not isActive then return end
	
    a += dt
    if side then
        wall.CFrame += Vector3.new(1, 0, 0) * dt * speed
    else
        wall.CFrame -= Vector3.new(1, 0, 0) * dt * speed
    end

    if a > timer then
        a = 0
		side = not side
		isActive = false
    end
end

RunService.Heartbeat:Connect(move)
RunService.Heartbeat:Connect(respawnCooldown)