import re

with open("input.txt", "r") as f:
    tgt_x_min, tgt_x_max, tgt_y_min, tgt_y_max = map(int, re.match("^target area: x=(.+?)\.\.(.+?), y=(.+?)\.\.(.+?)$", f.read().strip()).groups())

high = 0
unique = 0

x_range = max(abs(tgt_x_min), abs(tgt_x_max))
y_range = max(abs(tgt_y_min), abs(tgt_y_max))
for vel_y_0 in range(-y_range, y_range + 1):
    for vel_x_0 in range(-x_range, x_range + 1):
        pos_x, pos_y = 0, 0
        vel_x, vel_y = vel_x_0, vel_y_0
        height = 0
        while pos_x <= tgt_x_max and pos_y >= tgt_y_min:
            pos_x += vel_x
            pos_y += vel_y
            vel_x -= (vel_x > 0) - (vel_x < 0)
            vel_y -= 1
            height = max(height, pos_y)
            if (tgt_x_min <= pos_x <= tgt_x_max and
                tgt_y_min <= pos_y <= tgt_y_max):
                high = max(high, height)
                unique += 1
                break

print("1:", high)
print("2:", unique)
