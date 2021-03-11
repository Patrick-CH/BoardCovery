# 棋盘覆盖问题
 棋盘覆盖问题的python实现


![image.png](https://i.loli.net/2021/03/11/9fnp7O5XoQzWqPC.png)


![image.png]( https://i.loli.net/2021/03/11/hNcMAbsER4nKIJ1.png)


![image.png]( https://i.loli.net/2021/03/11/EzwadybcGNWTkRX.png)


**棋盘覆盖问题**，是一种编程问题。
如何应用分治法求解棋盘覆盖问题呢？分治的技巧在于如何划分棋盘，使划分后的子棋盘的大小相同，并且每个子棋盘均包含一个特殊方格，从而将原问题分解为规模较小的棋盘覆盖问题。k>0时，可将2^k×2^k的棋盘划分为4个2^（k-1）×2^（k-1）的子棋盘。这样划分后，由于原棋盘只有一个特殊方格，所以，这4个子棋盘中只有一个子棋盘包含该特殊方格，其余3个子棋盘中没有特殊方格。为了将这3个没有特殊方格的子棋盘转化为特殊棋盘，以便采用递归方法求解，可以用一个L型骨牌覆盖这3个较小棋盘的会合处，从而将原问题转化为4个较小规模的棋盘覆盖问题。递归地使用这种划分策略，直至将棋盘分割为1×1的子棋盘。

问题解释来源 百度
_https://baike.baidu.com/item/%E6%A3%8B%E7%9B%98%E8%A6%86%E7%9B%96%E9%97%AE%E9%A2%98/3015357?fr=aladdin_