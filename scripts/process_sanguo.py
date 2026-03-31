import os
import re
import sys

# 添加 src 目录到 Python 路径
sys.path.insert(
    0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src"))
)

from sanguoagent.settings import Settings
from sanguoagent.utils import ensure_directory

settings = Settings()

# 原始 txt 路径
file_path = os.path.join(settings.DATA_DIR, "book", "三国演义.txt")
# 创建输出目录
output_dir = os.path.join(settings.PROCESSED_DATA_DIR, "三国演义")
ensure_directory(output_dir)

# 读取文件内容，尝试使用 UTF-8 编码，如果失败则使用 GBK 编码
try:
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
except UnicodeDecodeError:
    with open(file_path, "r", encoding="gbk") as f:
        content = f.read()

# 正则表达式匹配回目标题
pattern = r"(第[一二三四五六七八九十百零]+回\s+[^\n]+)"
matches = re.findall(pattern, content)

# 打印匹配到的回目标题
print(f"匹配到的回目数量: {len(matches)}")
for i, match in enumerate(matches):
    print(f"{i+1}: {match.strip()}")

# 处理回目，提取回目序号和内容
chapters = []
for match in matches:
    # 提取回目序号
    chapter_num_match = re.match(r"第([一二三四五六七八九十百零]+)回", match)
    if chapter_num_match:
        chapter_num = chapter_num_match.group(1)
        # 转换为数字格式，以便排序
        num_map = {
            "一": 1,
            "二": 2,
            "三": 3,
            "四": 4,
            "五": 5,
            "六": 6,
            "七": 7,
            "八": 8,
            "九": 9,
            "十": 10,
            "百": 100,
            "零": 0,
        }
        chapter_num_arabic = 0
        if "百" in chapter_num:
            parts = chapter_num.split("百")
            if parts[0]:
                chapter_num_arabic += num_map[parts[0]] * 100
            if parts[1]:
                if len(parts[1]) == 3:
                    if "零" in parts[1]:
                        # 如"一百零一" -> 101
                        chapter_num_arabic += num_map[parts[1][2]]
                    else:
                        # 如"一百二十" -> 120
                        chapter_num_arabic += (
                            num_map[parts[1][0]] * 10 + num_map[parts[1][2]]
                        )
                elif len(parts[1]) == 2:
                    if parts[1][0] == "十":
                        # 如"百十" -> 110
                        chapter_num_arabic += 10 + num_map[parts[1][1]]
                    elif parts[1][0] == "零":
                        # 如"零一" -> 1
                        chapter_num_arabic += num_map[parts[1][1]]
                    else:
                        # 如"二十" -> 20
                        chapter_num_arabic += num_map[parts[1][0]] * 10
                else:
                    chapter_num_arabic += num_map[parts[1][0]]
        else:
            if len(chapter_num) == 3:
                # 如"二十八" -> 28
                chapter_num_arabic += (
                    num_map[chapter_num[0]] * 10 + num_map[chapter_num[2]]
                )
            elif len(chapter_num) == 2:
                if chapter_num[0] == "十":
                    # 如"十八" -> 18
                    chapter_num_arabic += 10 + num_map[chapter_num[1]]
                else:
                    # 如"二十" -> 20
                    chapter_num_arabic += num_map[chapter_num[0]] * 10
            else:
                chapter_num_arabic += num_map[chapter_num[0]]
        chapters.append((chapter_num_arabic, chapter_num, match))

# 按回目序号排序
chapters.sort(key=lambda x: x[0])

# 提取每个回目的内容并保存
for i, (chapter_num_arabic, chapter_num, chapter_title) in enumerate(chapters, 1):
    # 提取回目内容
    if i < len(chapters):
        next_chapter_title = chapters[i][2]
        # 使用正则表达式进行分割，确保只匹配完整的标题
        chapter_content = re.split(
            rf"^{re.escape(next_chapter_title)}$",
            content.split(chapter_title)[1],
            flags=re.MULTILINE,
        )[0]
    else:
        chapter_content = content.split(chapter_title)[1]

    # 保存到文件
    print(
        f"Debug: i={i}, chapter_num_arabic={chapter_num_arabic}, chapter_num={chapter_num}, chapter_title={chapter_title}"
    )
    output_file = os.path.join(
        output_dir, f"No.{chapter_num_arabic} 第{chapter_num}回.txt"
    )
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(chapter_title + "\n\n" + chapter_content)

print(f"处理完成，共提取 {len(chapters)} 个回目")
