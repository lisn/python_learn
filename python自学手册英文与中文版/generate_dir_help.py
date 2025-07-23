import sys

def save_dir_and_help(obj, filename="dir_help_output.txt"):
    # 重新生成输出的文件名
    filename = obj + '_' + filename
    with open(filename, "w") as f:
        # 改变标准输出为文件
        sys.stdout = f
        f.write('='*8 + 'dir()' + '='*8 +'\n')
        i = 0
        for obj_list in dir(eval(obj)):#eval去掉引号
            print('{}, '.format(obj_list),end='')
            i += 1
            # 输出8个进行换行
            if i % 8 == 0:
                print('')

        # 写入 help() 结果
        f.write('\n\n' + '='*8 + 'help()' + '='*8 + '\n')
        for obj_list in dir(eval(obj)):#eval去掉引号
            # 不输出内置的函数
            if not obj_list.startswith('__') :
                help(obj + '.' + obj_list)

        # 恢复标准输出
        sys.stdout = sys.__stdout__


if __name__ == '__main__':
    if len(sys.argv) <= 1:
        print(f'please input python {sys.argv[0]} + one data type')
    else :
        save_dir_and_help(sys.argv[1])

