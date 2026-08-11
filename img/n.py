import os
import re

# 当前文件夹
folder = os.getcwd()

# 找出符合“纯数字.png”的文件
files = []

for filename in os.listdir(folder):
    match = re.fullmatch(r"(\d+)\.png", filename, re.IGNORECASE)
    if match:
        old_num = int(match.group(1))
        new_num = old_num + 2
        files.append((old_num, new_num, filename))

# 先改成临时文件名，避免 1.png -> 3.png 时与原来的 3.png 冲突
temp_files = []

for old_num, new_num, filename in files:
    old_path = os.path.join(folder, filename)
    temp_path = os.path.join(folder, f"__temp_{old_num}.png")

    os.rename(old_path, temp_path)
    temp_files.append((temp_path, new_num))

# 再改成最终文件名
for temp_path, new_num in temp_files:
    new_path = os.path.join(folder, f"{new_num}.png")
    os.rename(temp_path, new_path)

print(f"完成，共重命名 {len(files)} 个 PNG 文件。")