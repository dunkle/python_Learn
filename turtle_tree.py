# -*- coding: utf-8 -*-
'''
绘制分形树
'''

import turtle as tl

def draw_smalltree(tree_length,tree_angle,start_point):
    '''
    绘制分形树函数
    '''
    tl.penup()
    #tl.pencolor('green')
    tl.left(90)  #因为树是往上的，所以先把方向转左
    tl.backward(start_point) #把起点放到底部
    tl.pendown()

    if tree_length >= 3:
        tl.forward(tree_length) #往前画
        tl.right(tree_angle)  #往右转
        draw_smalltree(tree_length - 5,tree_angle,start_point)#画下一枝，直到画到树枝长小于3

        tl.left(2 * tree_angle)  #转向画左
        draw_smalltree(tree_length -5,tree_angle,start_point) #直到画到树枝长小于3

        tl.rt(tree_angle) #转到正向上的方向，然后回溯到上一层
        if tree_length <= 5:  #树枝长小于x # ，可以当作树叶了，树叶部分为绿色
            tl.pencolor('green')
        if tree_length > 5:
            tl.pencolor('brown')  #树干部分为棕色
        tl.backward(tree_length)  #往回画，回溯到上一层



def main():
    tree_length = 30  #我设置的最长树干为30
    tree_angle = 40  #树枝分叉角度
    start_point0 = 100
    draw_smalltree(tree_length, tree_angle, start_point0)

    draw_smalltree(tree_length, tree_angle, 500)
    tl.exitonclick()  #点击才关闭画画窗口

if __name__ == '__main__':
    main()