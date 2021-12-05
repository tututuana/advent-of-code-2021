local levels = {}
for line in io.lines("input.txt") do
    table.insert(levels, tonumber(line))
end

local function count(step)
    local sum = 0
    for i = 1, #levels - step do
        if levels[i] < levels[i + step] then
            sum = sum + 1
        end
    end
    return sum
end

print(count(1), count(3))
