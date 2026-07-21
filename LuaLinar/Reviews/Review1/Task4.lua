-- Все ок
local a = io.read("n")
local b = io.read("n")
local c = io.read("n")

if (a >= b and a <= c) or (a >= c and a <= b) then
    print(a)
elseif (b >= a and b <= c) or (b >= c and b <= a) then
    print(b)
else
    print(c)
end
