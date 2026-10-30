# ============================================
# Day 1：你的第一个 Python 脚本
# 任务：算一个纸箱的用料面积（这是你专业的活儿）
#
# 运行方法：在终端输入
#   python day1_纸箱脚本.py
# ============================================

# ---- 第 1 部分：已经写好的示范 ----
# 变量：给一个值起个名字。下面是箱子的长宽高，单位 cm
length = 40.0   # 长
width = 30.0    # 宽
height = 25.0   # 高

# 五层瓦楞纸箱的表面积（假设 0201 型，简化计算：六个面）
surface_area = 2 * (length * width + length * height + width * height)

print("箱子尺寸:", length, "x", width, "x", height, "cm")
print("用料面积:", surface_area, "平方厘米")
print("约", round(surface_area / 10000, 3), "平方米")

l=50
w=40
h=30
surface_area2 = 2 *(l* w + l * h  + w * h)
print("箱子尺寸:", l, "x", w, "x", h, "cm")
print("用料面积:", surface_area2, "平方厘米")
print("约", round(surface_area2 / 10000, 3), "平方米")  
if surface_area < surface_area2:
    print("箱子 A 更省料")
else:
    print("箱子 B 更省料")

boxes = [[40.0, 30.0, 25.0], [50.0, 40.0, 30.0],[60,40,30],[32,54,25]]
for box in boxes:
    print(box)
    l,w,h = box
    surface_area2 = 2 *(l* w + l * h  + w * h)
    print("箱子尺寸:", l, "x", w, "x", h, "cm")
    print("用料面积:", surface_area2, "平方厘米")
    print("约", round(surface_area2 / 10000, 3), "平方米")  

