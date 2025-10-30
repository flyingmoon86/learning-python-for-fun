#Python 提供了内置函数 open() 来操作文件。
import os

# 切换到脚本所在目录
script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)

# 打印当前工作目录和文件位置以便调试


#下面是一个简单的示例，展示如何使用 open() 函数读取和写入文件。    
#推荐使用 with语句（会自动关闭文件）：
with open('example.txt', 'w') as file:
    file.write('Hello, World!')
    # 打开文件时使用 'w' 模式会覆盖原有内容
# ===============================
#模式	含义
#"r"	只读（默认）
#"w"	写入（覆盖原内容）
#"a"	追加写入（在末尾添加内容）
#"r+"	读写模式
#"b"	二进制模式（可加在后面，例如 "rb", "wb"）
# ===============================
def copy_first_10_lines(src_file, dst_file):
    try:
        with open(src_file, "r", encoding="utf-8") as f_src:
            lines = f_src.readlines()[:4]  # 读取前4行

        with open(dst_file, "w", encoding="utf-8") as f_dst:
            for line in lines:
                f_dst.write(line)

        print(f"✅ 成功将 {src_file} 的前10行写入 {dst_file}")

    except FileNotFoundError:
        print(f"⚠️ 文件 {src_file} 不存在，请检查路径！")
    except Exception as e:
        print(f"❌ 出现错误：{e}")

# 主程序入口
if __name__ == "__main__":
    print("当前工作目录:", os.getcwd())
    print("当前脚本位置:", __file__)
    copy_first_10_lines('data.txt', 'output.txt')
    