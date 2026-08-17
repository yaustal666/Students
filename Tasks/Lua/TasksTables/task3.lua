-- Неприятное обновление
-- Для справки - это в режиме массива, просто элементы массива это table в режиме объектов
-- В новое версии игры решили понерфить уровни
-- Теперь максимальный уровень - 100
-- Для людей, которые играют больше 50 дней и имеют > 100 уровня
-- Специальное событие - им выдают метку короля, king = true
-- Однако все остальным нужно указать, что у них ее нет, иначе при
-- попытке определить является ли игрок king код будет часто падать

local players = {
    {name = "Alex", level = 100, daysInGame = 5 },
    {name = "Miha100", level = 10, daysInGame = 10 },
    {name = "Tututum", level = 77, daysInGame = 1 },
    {name = "Shadow", level = 120, daysInGame = 100 },
    {name = "jjij", level = 115, daysInGame = 30 },
    {name = "Lolopop", level = 100, daysInGame = 55 },
    {name = "Tututum1", level = 77, daysInGame = 1 },
    {name = "Tututum2", level = 77, daysInGame = 5 },
    {name = "Tututum3", level = 77, daysInGame = 8 },
    {name = "Tututum4", level = 77, daysInGame = 7 },
    {name = "Kuka", level = 35, daysInGame = 10 },
    {name = "Tututum5", level = 77, daysInGame = 1 },
    {name = "AppleLover", level = 40, daysInGame = 8 },
}
for _, player in ipairs(players) do
    if player.level > 100 then
        if player.daysInGame > 50 then
            player.king = true
        end
        
        player.level = 100
    else
        player.king = false
    end
end

for _, player in ipairs(players) do
    print(player.name, player.level, player.daysInGame, player.king)
    -- local message = player.name .. " " .. tostring(player.level) .. " " .. tostring(player.score) .. " " .. tostring(player.king)
end


-- В результате нужно вывести список игроков с обновленными данными

