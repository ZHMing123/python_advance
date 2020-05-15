# _*_ coding:utf-8 _*_
# 文件作者: ZHMing123
# 开发时间：2020/5/9 13:24
# 文件名称：read_big_file.py
# 开发工具：PyCharm

# 500G特殊的一行, 里面的每一行分割符是{|}
def my_readlines(f, split_str):
    buf = ""  # 缓存，用来存储当前需要处理的字符
    while True:  # 外层循环，读取文件直到读取完
        while split_str in buf:  # 内层循环，用来识别每一行，并yield返回
            pos = buf.index(split_str)  # 返回buf中第一次出现分割符{|}的下标
            yield buf[:pos]  # 将分割符{|}之前的字符返回（即一行数据）
            # 丢弃已经返回了的字符（包括分割符{|}），继续处理缓存中后面的字符
            buf = buf[pos + len(split_str):]

        # 处理完当前缓存中的所有字符后（可能还存在剩余的字符，但没有了分割符{|}，返回不了）
        chunk = f.read(4096)  # 接着上次的继续从文件中读入4096个字节

        if not chunk:
            # 说明已经读到了文件的结尾了
            yield buf  # 把buf中还剩余的字符返回，因为文件结尾可能没有分割符{|}
            break      # 退出循环

        # 还没读完，则将这次读到是字符和上次剩余的字符合并后当作新的待处理字符集
        buf += chunk


if __name__ == '__main__':
    # print("zhmingrootzhmingrootzhmingroot".index("roo"))

    with open("big_file.txt") as f:
        for line in my_readlines(f, "{|}"):
            print(line)

