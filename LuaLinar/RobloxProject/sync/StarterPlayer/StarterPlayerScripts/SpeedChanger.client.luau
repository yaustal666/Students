local ReplicatedStorage = game:GetService("ReplicatedStorage")
local CurrencyChangedEvent = ReplicatedStorage:WaitForChild("remotes"):WaitForChild("CurrencyChangedEvent")
local Players = game:GetService("Players")

CurrencyChangedEvent.OnClientEvent:Connect(function(currencyName, amount)
    if "Speed" == currencyName then
        local humanoid: Humanoid = Players.LocalPlayer.Character:FindFirstChild("Humanoid")
        humanoid.WalkSpeed = amount
    end
end)
