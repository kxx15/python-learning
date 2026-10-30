length = 5
width = 10
height = 15

def box_area(l, w, h):
    return 2 * (l*w + w*h + l*h)

print(f"{length}x{width}x{height} 纸箱表面积 =", box_area(length, width, height))


print(f"{length}x{width}x{height} 纸箱表面积 =", box_area(length, width, height))
print("小盒子 5x10x15：", box_area(5, 10, 15))
print("大盒子 30x20x10：", box_area(30, 20, 10))