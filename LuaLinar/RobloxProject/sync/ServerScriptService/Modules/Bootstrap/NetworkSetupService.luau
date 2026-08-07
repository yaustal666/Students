local remoteEventsNames = {
    "AddCurrencyEvent",
    "CurrencyChangedEvent"
}

local remotes = Instance.new("Folder", game.ReplicatedStorage)
remotes.Name = "remotes"

for _, remoteEventName in ipairs(remoteEventsNames) do
    local event = Instance.new("RemoteEvent", remotes)
    event.Name = remoteEventName
end

local Module = {}
return Module