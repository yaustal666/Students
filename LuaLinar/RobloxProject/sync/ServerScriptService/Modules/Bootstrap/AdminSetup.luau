local Players = game:GetService("Players")
local AdminPanel = game.ServerStorage.AdminPanel
local AdminPanelButton = game.ServerStorage.AdminPanelButton

local admins = {
    11101857966
}

local module = {}

function module.initPlayer(player)
    local UserId = player.UserId
    if not table.find(admins, UserId) then return end

    local ScreenGui = player.PlayerGui:WaitForChild("UI").ScreenGui

    local apanel = AdminPanel:Clone()
    apanel.Parent = ScreenGui

    local apanelButton = AdminPanelButton:Clone()
    apanelButton.Parent = ScreenGui
end


return module
