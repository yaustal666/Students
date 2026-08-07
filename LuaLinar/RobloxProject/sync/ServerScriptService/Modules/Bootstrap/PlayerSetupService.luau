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

local function SetupPlayerInventory(player: Player)
    local inventory = Instance.new("Folder", player)
    inventory.Name = "inventory"

    local multipliers = Instance.new("Folder", inventory)
    multipliers.Name = "multipliers"
    
	local mult = Instance.new("NumberValue", multipliers)
	mult.Name = "SpeedMultiplier"
    mult.Value = 2.5
    mult:SetAttribute("CurrencyName", "Speed")
end

function PlayerSetupService.initPlayer(player: Player, playerData: table)
    SetupPlayerLeaderstats(player, playerData)
    SetupPlayerInventory(player)
end

return PlayerSetupService
