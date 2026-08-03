local PlayerSetupService = {}

local function SetupPlayerLeaderstats(player: Player, playerData: table)
    local leaderstats = Instance.new("Folder", player)
    leaderstats.Name = "leaderstats"

    for currencyName, value in pairs(playerData) do
        local currency = Instance.new("IntValue", leaderstats)
        currency.Name = currencyName
        currency.Value = value
    end
end

local function SetupPlayerInventory(player)
    local inventory = Instance.new("Folder")
    inventory.Name = "inventory"
    inventory.Parent = player

	local currency = Instance.new("NumberValue", inventory)
	currency.Name = "SpeedMultiplier"
    currency.Value = 2.5
end

function PlayerSetupService.initPlayer(player: Player, playerData: table)
    SetupPlayerLeaderstats(player, playerData)
    SetupPlayerInventory(player)
end

return PlayerSetupService
