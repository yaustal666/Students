local RunService = game:GetService("RunService")
MovementTrackerService = require(game.ServerScriptService.Modules.Gameplay.MovementTrackerService)
Players = game:GetService("Players")
local treadmill = script.Parent
--task.wait(3)

--local humanoid = workspace.bukunoko.HumanoidRootPart
--local player = Players:GetPlayerFromCharacter(workspace.bukunoko)
-- treadmill.Touched:Connect(function(part)
--     local character = part.Parent
--     local player = Players:GetPlayerFromCharacter(character)
--     if not player then return end
--     if part.Name ~= "LeftFoot" then return end
--     print(part.Name)
    
--     MovementTrackerService.SetPlayer(player)
-- end)

-- treadmill.TouchEnded:Connect(function(part)
--     local character = part.Parent
--     local player = Players:GetPlayerFromCharacter(character)
--     if not player then return end
--     if part.Name ~= "LeftFoot" then return end
--     print(part.Name)
    
--     MovementTrackerService.UnsetPlayer(player)
-- end)

--while task.wait(1) do
--    local distance = (treadmill.Position - humanoid.Position).Magnitude

--    if distance < 9 then
--        MovementTrackerService.SetPlayer(player)
--    else
--        MovementTrackerService.UnsetPlayer(player)
--    end
--end