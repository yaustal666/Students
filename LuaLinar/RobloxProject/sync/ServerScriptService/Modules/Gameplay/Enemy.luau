local RunService = game:GetService("RunService")
local enemy = game.Workspace.Enemy
local startPosition = enemy.CFrame
local speed = 10
local activePlayers = {}
local isIdle = true


local function enemyUpdate(dt)
    if isIdle then
        if startPosition ~= enemy.CFrame then
            local direction = (startPosition.Position - enemy.CFrame.Position).Unit
            enemy.CFrame = enemy.CFrame + (direction * speed)
        end
    else
        -- every 0.2 sec find closest player
        -- move to that player
    end
end

RunService.Heartbeat:Connect(enemyUpdate)

local module = {}

return module
