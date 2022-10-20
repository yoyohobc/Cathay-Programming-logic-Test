def drop_calculator(height,times):
    if not height.isdigit() or not times.isdigit():
        return "error input !!!"

    height, times, total = int(height), int(times), 0

    for i in range(times):
        total += height
        height /= 2
        if i != (times - 1):
            total += height

    return f"總共 : {height}\n第{times}次 : {total}"

height = input("輸入高度 : ")
times = input("輸入落地次數 : ")
print(drop_calculator(height,times))