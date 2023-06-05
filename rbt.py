class Node:
    def __init__(self):
        self.value = None
        self.red = True
        self.left_child = None
        self.right_child = None

    def __str__(self):
        return (f"Значение {self.value} левый {self.left_child.value} правый {self.right_child.value} цвет {self.red}")

class RedBlackTree:
    def __init__(self):
        self.root = None

    def add(self, val):
        if self.root != None:
            result = self.add_node(self.root, val)
            self.root = self.rebalance(self.root)
            self.root.red = False
            return result
        else:
            self.root = Node()
            self.root.red = False
            self.root.value = val
            return True

    def add_node(self, node : Node, val):
        if node.value == val:
            return False
        else:
            if node.value > val:
                if node.left_child != None:
                    result = self.add_node(node.left_child, val)
                    node.left_child = self.rebalance(node.left_child)
                    return result
                else:
                    node.left_child = Node()
                    node.left_child.red = True
                    node.left_child.value = val
                    return True
            else:
                if node.right_child != None:
                    result = self.add_node(node.right_child, val)
                    node.right_child = self.rebalance(node.right_child)
                    return result
                else:
                    node.right_child = Node()
                    node.right_child.red = True
                    node.right_child.value = val
                    return True
                
    def colorswap(self, node : Node):
        node.right_child.red = False
        node.left_child.red = False
        node.red = True   

    def leftswap(self, node : Node):
        right = node.right_child
        between = right.left_child
        right.left_child = node
        node.right_child = between
        right.red = node.red
        node.red = True
        return right
    
    def rightswap(self, node : Node):
        left = node.left_child
        between = left.right_child
        left.right_child = node
        node.left_child = between
        left.red = node.red
        node.red = True
        return left

    def rebalance(self, node : Node):
        result = node
        while True:
            need_rebalance = False
            if result.right_child != None and result.right_child.red == True and (result.left_child == None or result.left_child.red == False):
                need_rebalance = True
                result = self.leftswap(result)
            if result.left_child != None and result.left_child.red == True and result.left_child.left_child != None and result.left_child.left_child.red == True:
                need_rebalance = True
                result = self.rightswap(result)
            if result.left_child != None and result.left_child.red == True and result.right_child != None and result.right_child.red == True:
                need_rebalance = True
                self.colorswap(result)
            if need_rebalance == False:
                break
        return result
