local AdminPanel = script.Parent.Parent.AdminPanel
local AdminPanelButton: TextButton = script.Parent

AdminPanelButton.MouseButton1Click:Connect(function()
    AdminPanel.Visible = not AdminPanel.Visible
end)