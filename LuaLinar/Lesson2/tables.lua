-- local arr = {8, 2, 3, 16, 5, 45, 16, 13}
-- local b = io.read("n")

-- for index, value in ipairs(arr) do
--     if value == b then
--         print(index)
--         break
--     end
-- end

-- for i = 1, #arr do
--     arr[i] = arr[i] * 2
--     print(arr[i])
-- end

-- for index, _ in ipairs(arr) do
--     print(index)
-- end

-- local inventary = {
--     apple = 3,
--     potato = 6,
-- }

-- inventary.sword = 1

-- local user = {
--     name = "Max",
--     age = "23",
--     level = "100"
-- }

-- for key, value in pairs(inventary) do
--     print(key, value)
-- end

function analizeString(s) 
    local letters = {}
    for i = 1, #s do
        local char = s:sub(i, i)
        
        if letters[char] == nil then
            letters[char] = 1
        else
            letters[char] = letters[char] + 1
        end
    end

    for key, value in pairs(letters) do
        print(key, value)
    end
end

analizeString("kchskjhfcgalikjfjhkbvfkluas fjhasgdfo ugdfujyihjaSIKLH")