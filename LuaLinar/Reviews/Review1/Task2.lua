-- Все ок

local a = io.read("n")
local b = io.read("n")


if b == 1 then
    print(a / 1000000)   -- миллиграмы
elseif b == 2 then       
    print(a)             --кг
elseif b == 3 then       
    print(a * 100)       --центнеры
elseif b == 4 then
    print(a * 1000)      --тонны
end
