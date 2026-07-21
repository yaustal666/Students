function isEven(n)
    if n % 2 == 0 then
        return true
    else
        return false
    end
end

function sqr(a)
    return a * a
end

local a = sqr(12)
print(a)

for i = 1, 100 do
    if isEven(i) then
        print(i)
    end
end