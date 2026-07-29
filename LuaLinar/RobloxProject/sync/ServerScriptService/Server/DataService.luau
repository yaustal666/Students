local DataStoreService = game:GetService("DataStoreService")
local Players = game:GetService("Players")
local PlayerDataStore = DataStoreService:GetDataStore("PlayerDataStore_v1")

local SessionData = {}

-- PlayerConnected - load data from datastore in SessionData
-- If player is new - create new data in both data store and session
-- Player playing game. Working with SessionData
-- Player leave -> save from SessionData in DataStore

local function getPlayerDefaultData()
    return  {
        Coins = 0,
    }
end

local DataService = {}

function DataService.loadDataAsync(player: Player) 
    local success, data = pcall(
        function()
            return PlayerDataStore:GetAsync(player.UserId)
        end
    )

    if not success then return nil end
    if not data then return getPlayerDefaultData() end
    return data
end

function DataService.saveDataAsync(player: Player) 
    local success, result = pcall(
        function()
            PlayerDataStore:SetAsync(player.UserId, SessionData[player.UserId])
        end
    )
end

function DataService.getPlayerData(player: Player)
    return SessionData[player.UserId]
end

function DataService.updatePlayerData(player: Player, key: string, newValue)
    if SessionData[player.UserId] then
        SessionData[player.UserId][key] = newValue
        return true
    end
    return false
end

function DataService.initPlayerSession(player, playerData)
    SessionData[player.UserId] = playerData
end

game:BindToClose (
    function()
        for _, player in ipairs(Players:GetPlayers()) do
            DataService.saveDataAsync(player)
        end
    end
)

return DataService