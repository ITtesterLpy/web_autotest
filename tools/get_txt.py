def get_txt(filename):

    # 文件存储路径
    file_path = "../data/" + filename

    # 读取文件
    with open(file_path, 'r', encoding='utf-8') as f:
        return f.readlines()


if __name__ == '__main__':
    arrs = []
    for data in get_txt('login_data.txt'):
        arrs.append(tuple(data.strip().split(',')))
    print(arrs[1::])