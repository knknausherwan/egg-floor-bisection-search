floors_max = 102
floors_min = 1

secret_egg_breaking_floor = 92

ans = (floors_max + floors_min) // 2
steps = 1

while ans != secret_egg_breaking_floor:
    print("Floor_num: ", ans, "Steps: ", steps)

    if ans == secret_egg_breaking_floor:
        break
    elif ans == secret_egg_breaking_floor - 1:
        ans += 1
        break
    elif ans < secret_egg_breaking_floor:
        floors_min = ans
    else:
        floors_max = ans

    ans = (floors_max + floors_min) // 2
    steps += 1

print(f"The floor where the egg does not break is {ans} and it took {steps} steps")
