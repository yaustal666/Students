-- Глупые ограничения (или нет?)
-- дан table с животными, животным от 1 до 5 лет, 
-- нужно просто его распечатать, но! не просто так

local animals = {
    {name = "Barsik", type="Dog", age = 4},
    {name = "Pupik", type="Cat", age = 2},
    {name = "Nana", type="Cat", age = 1},
    {name = "Luka", type="Dog", age = 5},
}

local voiceByType = {
    Cat = "meow",
    Dog = "bark",
}

local ageCategoryByYear = {
    [1] = "baby",
    [2] = "child",
    [3] = "child",
    [4] = "old",
    [5] = "old",
}

for _, animal in ipairs(animals) do
    print(animal.type .. ": " .. animal.name)
    print("Voice: " .. voiceByType[animal.type])
    print("Age: " .. ageCategoryByYear[animal.age])
    print()
end
-- Если это кот, то первой строчкой идет Cat: + имя животного
-- Если собака, то Dog: + имя животного
-- Потом идет Voice:, если кот то meow, если собака то bark
-- Потом идет возраст. Соответственно по годам 1 - baby, 2, 3 - child, 4, 5 - old
-- НЕЛЬЗЯ использовать условия, можно создавать свои table. Но никаких if, циклы можно
-- Могут возникнуть затруднения именно формирования строк, вроде достаточно функции concat из tutorial, но можешь гуглить если что