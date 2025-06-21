input_path = "scene/hotcrush/images.txt"
output_path = "scene/hotcrush/images_fixed.txt"

with open(input_path, "r") as fin:
    lines = fin.readlines()

i = 0
fixed_lines = []

while i < len(lines):
    line = lines[i]

    if line.strip().startswith("#") or line.strip() == "":
        fixed_lines.append(line)
        i += 1
        continue

    # 图像元数据行
    parts = line.strip().split()
    if len(parts) >= 10:
        original_name = parts[9]
        try:
            image_number = int(original_name.split(".")[0])
            parts[9] = f"frame_{image_number:04d}.jpg"
        except ValueError:
            pass  # 如果不能转为数字则跳过
        fixed_lines.append(" ".join(parts) + "\n")
    else:
        fixed_lines.append(line)

    # 图像的第二行（特征点）直接原样写入
    if i + 1 < len(lines):
        fixed_lines.append(lines[i + 1])

    i += 2

# 写入到新文件中（此时文件才打开）
with open(output_path, "w") as fout:
    fout.writelines(fixed_lines)


