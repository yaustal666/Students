local DataStoreService = game:GetService("DataStoreService")
local Players = game:GetService("Players")
local PlayerDataStore = DataStoreService:GetDataStore("PlayerDataStore_v2")

local SessionData = {}

local function getPlayerDefaultData()
    return  {
        Coins = 0,
        Speed = 0,
    }
end

local Module = {}

function Module.loadDataAsync(player: Player) 
    local success, data = pcall(
        function()
            return PlayerDataStore:GetAsync(player.UserId)
        end
    )

    if not success then return nil end
    if not data then return getPlayerDefaultData() end
    return data
end

function Module.saveDataAsync(player: Player) 
    pcall(
        function()
            PlayerDataStore:SetAsync(player.UserId, SessionData[player.UserId])
        end
    )
end

function Module.getPlayerData(player: Player)
    return SessionData[player.UserId]
end

function Module.updatePlayerData(player: Player, key: string, newValue: any)
    if SessionData[player.UserId] then
        SessionData[player.UserId][key] = newValue
        return true
    end
    return false
end

function Module.initPlayerSession(player: Player, playerData: table)
    SessionData[player.UserId] = playerData
end

game:BindToClose (
    function()
        for _, player in ipairs(Players:GetPlayers()) do
            Module.saveDataAsync(player)
        end
    end
)

return Module