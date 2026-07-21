-- local a = 3
-- local b = 5


-- if a > b then
--     print("a")
-- else 
--     print("b")
-- end


-- for i = 1, 10 do
--     print(i)
-- end


-- local a = io.read("n")
-- if a % 2 == 0 then
--     print(true)
-- else 
--     print(false)
-- end


-- local n = io.read("n")
-- for i = 1, n do
--     if i % 2 == 0 then
--         print(i)
--     end
-- end


-- local a, b, c = io.read("n", "n", "n")
-- local max = a
-- if b > max then
--     max = b
-- end

-- if c > max then
--     max = c
-- end
-- print(max)


-- local a, b, c = io.read("n", "n", "n")
-- if a > b and a > c then
--     print(a)
-- end

-- if b > a and b > c then
--     print(b)
-- end

-- if c > b and c > a then
--     print(c)
-- end

local a = io.read("n")
-- a = 111 - посчитать кол-во цифр, то есть 3
-- a = 4553424 - 7
-- 4555 % 10 = 5 , 4555 // 10 = 455
-- 455 % 10 = 5 , 455 // 10 = 45
-- 45 % 10 = 5 , 45 // 10 = 4
-- 4 % 10 = 4 , 4 // 10 = 0

-- Задание - посчитать сумму цифр в данном числе, то есть для 4555 = 19
local count = 0
while a ~= 0 do
    count = count + 1
    a = a // 10
end

print(count)