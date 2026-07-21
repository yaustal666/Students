-- Не совсем)) Не каждый год, номер которого делится на 4 - високосный, например 1900 - не високосный

local a = io.read("n")

if a % 4 == 0 then
    print(true)
else
    print(false)
end