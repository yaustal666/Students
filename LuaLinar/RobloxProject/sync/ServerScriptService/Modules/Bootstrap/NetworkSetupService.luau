local remoteEventsNames = {
    "AddCurrencyEvent",
    "CurrencyChangedEvent"
}

local Module = {}

function Module.Init()
    local remotes = Instance.new("Folder", game.ReplicatedStorage)
    remotes.Name = "remotes"

    for _, remoteEventName in ipairs(remoteEventsNames) do
        local event = Instance.new("RemoteEvent", remotes)
        event.Name = remoteEventName
    end
end

return Module
