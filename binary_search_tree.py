#!/usr/bin/env python
# -*-coding:utf-8 -*-

"""
参考https://github.com/EchoLLLiu/DataStructure/blob/master/ch04tree/BinarySearchTree.py
"""

class Define_Tree_Node:
    def __init__(self, val):
        self.val = val      #定义键值
        self.left = None    #定义左节点
        self.right = None   #定义右节点

class Binary_Search_Tree:
    def insert(self, root, val):
        """
        将节点和键值插入二叉树
        :param root: 根节点
        :param val: 键值
        :return:返回每次插入操作后的新节点
        """
        if root == None:
            root = Define_Tree_Node(val)
        elif val < root.val:
            root.left = self.insert(root.left, val)
        elif val > root.val:
            root.right = self.insert(root.right, val)
        return root
    def query(self, root, val):
        """
        查找键值
        :param root: 根节点
        :param val: 待查找的键值
        """
        if root == None:
            return False
        elif root.val == val:
            return True
        elif val > root.val:
            return self.query(root.right, val)
        elif val < root.val:
            return self.query(root.left, val)
    def find_min_val(self, root):
        """
        查找最小键值
        """
        if root.left:
            return self.find_min_val(root.left)
        else:
            return root
    def find_max_val(self, root):
        """
        查找最大键值
        """
        if root.right:
            return self.find_max_val(root.right)
        else:
            return root

    def delNode(self, root, val):
        '''删除二叉查找树中值为val的点'''
        if root == None:
            return
        if val < root.val:
            root.left = self.delNode(root.left, val)
        elif val > root.val:
            root.right = self.delNode(root.right, val)
        # 当val == root.val时，分为三种情况：只有左子树或者只有右子树、有左右子树、既无左子树又无右子树
        else:
            if root.left and root.right:
                # 既有左子树又有右子树，则需找到右子树中最小值节
                temp = self.find_min_val(root.right)
                root.val = temp.val
                # 再把右子树中最小值节点删除
                root.right = self.delNode(root.right, temp.val)
            elif root.right == None and root.left == None:
                # 左右子树都为空
                root = None
            elif root.right == None:
                # 只有左子树
                root = root.left
            elif root.left == None:
                # 只有右子树
                root = root.right
        return root
    #def Find_min_node(self, root):
        #"""
        #查找最小值
        #"""
        #if root.left == None:
        #    return root
        #root = self.Find_min_node(root.left)
        #return root

    def print_tree(self, root):
        if root == None:
            return
        self.print_tree(root.left)
        print(root.val, end=" ")
        self.print_tree(root.right)
if __name__ == '__main__':
    list = [17, 5, 35, 15, 11, 29, 38, 9, 16, 8]
    root = None
    BST = Binary_Search_Tree()
    for val in list:
        root = BST.insert(root, val)
    print("中序打印二叉查找树：", end=" ")
    BST.print_tree(root)
    print("")
    print("根节点的键值：", root.val)
    print("树中最大值：", BST.find_max_val(root).val)
    print("树中最小值：", BST.find_min_val(root).val)
    print("查询键值为5的节点：", BST.query(root, 5))
    print("查询键值为100的节点：", BST.query(root, 100))
    print("删除键值为9的节点：", end=" ")
    root = BST.delNode(root, 9)
    BST.print_tree(root)
    print("")
    #print(BST.Find_min_node(root).val)



