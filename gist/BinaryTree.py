class TreeNode(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, val):
        if self.value:
            if val < self.value:
                if self.left:
                    self.left.insert(val)
                else:
                    self.left = TreeNode(val)
            else:
                if self.right:
                    self.right.insert(val)
                else:
                    self.right = TreeNode(val)
        else:
            self.value = val

    def preTraverse(self):
        res = []
        if self.value:
            res.append(self.value)
        if self.left:
            res += self.left.preTraverse()
        if self.right:
            res += self.right.preTraverse()
        return res

    def midTraverse(self):
        res = []
        if self.left:
            res += self.left.midTraverse()
        if self.value:
            res.append(self.value)
        if self.right:
            res += self.right.midTraverse()
        return res

    def postTraverse(self):
        res = []
        if self.left:
            res += self.left.postTraverse()
        if self.right:
            res += self.right.postTraverse()
        if self.value:
            res.append(self.value)
        return res

    def levelTraverse(self):
        res = []
        queue = []
        if self.value is None:
            return res
        queue.append(self)
        while queue:
            cur = queue.pop(0)
            res.append(cur.value)
            if cur.left:
                queue.append(cur.left)
            if cur.right:
                queue.append(cur.right)
        return res


tree = TreeNode(5)
tree.insert(9)
tree.insert(3)
tree.insert(7)
tree.insert(2)
tree.insert(1)
tree.insert(6)
tree.insert(4)
tree.insert(10)

print(tree.preTraverse()) # 5 3 2 1 4 9 7 6 10
print(tree.midTraverse()) # 1 2 3 4 5 6 7 9 10
print(tree.postTraverse()) # 1 2 4 3 6 7 10 9 5
print(tree.levelTraverse()) # 5 3 9 2 4 7 10 1 6