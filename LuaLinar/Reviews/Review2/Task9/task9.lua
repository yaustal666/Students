-- Корзина товаров
-- Все просто, есть table, сам его создай пожалуйста
-- Он состоит из продуктов и стоимости
-- Нужно посчитать общую стоимость - то есть цену корзины
local cart = {
    {product = "Хлеб", price = 45},
    {product = "Молоко", price = 89},
    {product = "Яйца", price = 120},
    {product = "Сыр", price = 350},
    {product = "Яблоки", price = 95},
}

local total = 0
for _, item in ipairs(cart) do
    total = total + item.price
end

print("Общая стоимость корзины: " .. total)