-- Удаляем крайних
-- Создать table в режиме массива с числами, предполагая что в общем случае - там люой набор чисел
-- Написать программу которая удалит из массива самый большой и самый маленький элементы
-- например {1, 100, -20, 80, 11} превратится в {1, 80, 11}

local numbers = {1, 100, -20, 80, 11}
local maxIndex, minIndex = 1, 1
for i = 2, #numbers do
    if numbers[i] > numbers[maxIndex] then
        maxIndex = i
    end
    if numbers[i] < numbers[minIndex] then
        minIndex = i
    end
end

if maxIndex > minIndex then
    table.remove(numbers, maxIndex)
    table.remove(numbers, minIndex)
elseif minIndex > maxIndex then
    table.remove(numbers, minIndex)
    table.remove(numbers, maxIndex)
else
    table.remove(numbers, maxIndex)
end

local parts = {}
for _, v in ipairs(numbers) do
    table.insert(parts, tostring(v))
end
print("{" .. table.concat(parts, ", ") .. "}")