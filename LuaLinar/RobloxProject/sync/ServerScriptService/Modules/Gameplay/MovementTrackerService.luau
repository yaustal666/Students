local CurrencyService = require(game.ServerScriptService.Modules.Economics.CurrencyService)

local runningPlayers = {}

local function connectToPlayerRunning(player: Player)
    player.CharacterAdded:Connect(function(character)
        local humanoid = character:FindFirstChild("Humanoid")
        humanoid.Running:Connect(function(speed)
            if speed <= 0 then
                runningPlayers[tostring(player)].isActive = false
            end
            
            if speed > 0 and runningPlayers[tostring(player)].isActive then
                return
            end

            if speed > 0 then
                runningPlayers[tostring(player)].isActive = true
            end
        end)
    end)
end

local function OnRunning(dt: number)
    for _, playerData in pairs(runningPlayers) do
        if not playerData.isActive then
            playerData.timePassed = 0
            continue
        end
        
        playerData.timePassed += dt

        if playerData.timePassed > 0.5 then
            CurrencyService.addCurrency(playerData.playerRefrence, "Speed", 1)
            playerData.timePassed = 0
        end
    end
end

game:GetService("RunService").Heartbeat:Connect(OnRunning)

local Module = {}

function Module.initPlayer(player: Player)
    runningPlayers[tostring(player)] = 
    {
        playerRefrence = player, 
        isActive = false,
        timePassed = 0    
    }
    connectToPlayerRunning(player)
end

return Module