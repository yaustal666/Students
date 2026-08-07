local ReplicatedStorage = game:GetService("ReplicatedStorage")
local Admin = require(ReplicatedStorage:WaitForChild("Admin"))

local UserIdInput = script.Parent.UserIdInput
local KillButton = script.Parent.Kill

KillButton.MouseButton1Click:Connect(function()
    local UserId = tonumber(UserIdInput.Text)
    Admin.Kill(UserId)
end)