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

    def pre_traversal_recursive(self):
        res = []
        if self.value:
            res.append(self.value)
        if self.left:
            res += self.left.pre_traversal_recursive()
        if self.right:
            res += self.right.pre_traversal_recursive()
        return res

    def pre_traversal(self):
        res = []
        stack = []
        cur = self
        while stack or cur:
            if cur:
                res.append(cur.value)
                if cur.right:
                    stack.append(cur.right)
                cur = cur.left
            else:
                cur = stack.pop()
        return res

    def mid_traversal_recursive(self):
        res = []
        if self.left:
            res += self.left.mid_traversal_recursive()
        if self.value:
            res.append(self.value)
        if self.right:
            res += self.right.mid_traversal_recursive()
        return res

    def mid_traversal(self):
        res = []
        stack = []
        cur = self
        while stack or cur:
            if cur:
                stack.append(cur)
                cur = cur.left
            else:
                cur = stack.pop()
                res.append(cur.value)
                cur = cur.right
        return res

    def post_traversal_recursive(self):
        res = []
        if self.left:
            res += self.left.post_traversal_recursive()
        if self.right:
            res += self.right.post_traversal_recursive()
        if self.value:
            res.append(self.value)
        return res

    def post_traversal(self):
        res = []
        stack = []
        cur = self
        while stack or cur:
            if cur:
                res.append(cur.value)
                if cur.left:
                    stack.append(cur.left)
                cur = cur.right
            else:
                cur = stack.pop()
        return res[::-1]

    def level_traversal(self):
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

    def double_link(self):
        stack = []
        cur = self
        queue = []
        while stack or cur:
            if cur:
                stack.append(cur)
                cur = cur.left
            else:
                cur = stack.pop()
                queue.append(cur)
                cur = cur.right
        queue_len = len(queue)
        for i in range(queue_len):
            if i+1 < queue_len:
                queue[i].right = queue[i+1]
            if i-1 >= 0:
                queue[i].left = queue[i-1]
        return queue[0]


tree = TreeNode(5)
tree.insert(9)
tree.insert(3)
tree.insert(7)
tree.insert(2)
tree.insert(1)
tree.insert(6)
tree.insert(4)
tree.insert(10)

print('pre_traversal_recursive:', tree.pre_traversal_recursive())  # 5 3 2 1 4 9 7 6 10
print('pre_traversal:', tree.pre_traversal())  # 5 3 2 1 4 9 7 6 10
print('mid_traversal_recursive:', tree.mid_traversal_recursive())  # 1 2 3 4 5 6 7 9 10
print('mid_traversal:', tree.mid_traversal())  # 1 2 3 4 5 6 7 9 10
print('post_traversal_recursive:', tree.post_traversal_recursive())  # 1 2 4 3 6 7 10 9 5
print('post_traversal:', tree.post_traversal())  # 1 2 4 3 6 7 10 9 5
print('level_traversal:', tree.level_traversal())  # 5 3 9 2 4 7 10 1 6

doubleLink = tree.double_link()
items = []
while doubleLink:
    items.append(doubleLink.value)
    doubleLink = doubleLink.right
print(items)


def rebuild_tree(list1, list2):
    if len(list1) == 0 or len(list2) == 0:
        return None
    root = list1[0]
    tree = TreeNode(root)
    root_index = list2.index(root)
    leftlist2 = list2[:root_index]
    leftlist1 = list1[1:len(leftlist2) + 1]
    tree.left = rebuild_tree(leftlist1, leftlist2)

    rightlist2 = list2[root_index + 1:]
    rightlist1 = list1[-len(rightlist2):]
    tree.right = rebuild_tree(rightlist1, rightlist2)
    return tree


tree = rebuild_tree([1, 2, 4, 7, 3, 5, 6, 8], [4, 7, 2, 1, 5, 3, 8, 6])

print('pre_traversal_recursive:', tree.pre_traversal_recursive())
print('pre_traversal:', tree.pre_traversal())
print('mid_traversal_recursive:', tree.mid_traversal_recursive())
print('mid_traversal:', tree.mid_traversal())
print('post_traversal_recursive:', tree.post_traversal_recursive())
print('post_traversal:', tree.post_traversal())
print('level_traversal:', tree.level_traversal())
