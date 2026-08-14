local rooms = {{}, {}, {}}
local module = {}

function module.handlePlayer(player: Player, room: number)
    local index = table.find(rooms, player)
    if index then
        table.remove(rooms[room], index)
    else
		table.insert(rooms[room], player)
    end
end

function module.getPlayersInRoom(room: number)
    return rooms[room]
end

return module
