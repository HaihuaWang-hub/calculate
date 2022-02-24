def main():
    """
    calculate sum.
    """

    # 导入模块
    import argparse

    parser = argparse.ArgumentParser(usage="test",
                                    description="example test",
                                    epilog="Thank your for your support.")
    # version
    parser.add_argument('-v','--version', action='version', version='%(prog)s 0.0.1')
    # 读取注释类型文件
    parser.add_argument('integers', metavar ='N', type = int, nargs ='+',
                        help ='an integer for the accumulator')

    # 解析参数
    args = parser.parse_args()

    def add_number(number):
        val = sum(number)
        return val

    print(add_number(number=args.integers))
    
    
    
    
if __name__ == '__main__':
    main()
