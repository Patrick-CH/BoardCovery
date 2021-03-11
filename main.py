import numpy as np
import matplotlib.pyplot as plt


class Board:
    def __init__(self, size, x, y):
        '''
        初始化棋盘

        :param size: 棋盘边长
        :param x: 特殊点横坐标
        :param y: 特殊点纵坐标
        '''
        self.special_block = (x, y)
        self.board = np.zeros((size, size), dtype=int)
        self.board[x][y] = (size * size - 1) / 3 + 1
        self.t = 1
        self.size = size

    def visualize(self):
        '''
        可视化函数

        :return: None
        '''
        plt.imshow(self.board, cmap=plt.cm.gray)
        plt.colorbar()
        plt.show()

    def fill_block(self, x, y):
        '''
        填充点(x, y)
        :param x: x
        :param y: y
        :return: None
        '''
        if self.board[x][y] == 0:
            self.board[x][y] = self.t
        else:
            raise Exception

    def fill(self, s_x, s_y, size, c_x, c_y):
        '''
        递归函数填充棋盘或子棋盘（下文称区块)

        :param s_x: 区块左上角x
        :param s_y: 区块左上角y
        :param size: 区块边长
        :param c_x: 区块特殊点坐标x
        :param c_y: 区块特殊点坐标x
        :return: None
        '''
        if size == 1:
            return
        pos = (round((c_x - s_x + 1) / size), round((c_y - s_y + 1) / size))
        center = (round(s_x + size / 2 - 1), round(s_y + size / 2 - 1))
        ls = [(0, 0), (0, 1), (1, 0), (1, 1)]  # 代表四个子区块
        for i in ls:
            if i != pos:  # 如果不是原有特殊点所在区块，则构造特殊点并填充
                x = center[0] + i[0]
                y = center[1] + i[1]
                self.fill_block(x, y)
        self.t += 1  # 标记号加一，标记下一骨牌
        for i in ls:
            if i != pos:  # 如果不是原有特殊点所在区块
                # 所构造特殊点位置(x, y)
                x = center[0] + i[0]
                y = center[1] + i[1]
                x1 = s_x + i[0] * (size / 2)
                y1 = s_y + i[1] * (size / 2)
                self.fill(x1, y1, size / 2, x, y)
            else:  # 如果是原有特殊点所在区块
                x1 = s_x + i[0] * (size / 2)
                y1 = s_y + i[1] * (size / 2)
                self.fill(x1, y1, size / 2, c_x, c_y)


if __name__ == '__main__':
    k = eval(input("请输入正整数K(棋盘大小2^2k,2^2k):\n"))
    loc_x = eval(input("请输入特殊点横坐标:\n"))
    loc_y = eval(input("请输入特殊点纵坐标:\n"))
    size = 2 ** (2 * k)
    b = Board(size, loc_x, loc_y)
    b.fill(0, 0, size, loc_x, loc_y)
    b.visualize()
    print(b.board)
