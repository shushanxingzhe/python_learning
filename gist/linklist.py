class LinkNode(object):
    def __init__(self, value):
        self.value = value
        self.next = None

    def insert(self, value):
        if self.next:
            self.next.insert(value)
        else:
            self.next = LinkNode(value)


class LinkOperation(object):
    def print(self, node):
        p = node
        while p:
            print(p.value)
            p = p.next

    def reverse(self, node):
        p = node.next
        node.next = None
        prev = node
        while p:
            next = p.next
            p.next = prev
            prev = p
            p = next
        return prev

    def merge(self, link1, link2):
        if link1.value < link2.value:
            newlink = link1
            link1 = link1.next
        else:
            newlink = link2
            link2 = link2.next
        p = newlink
        while link1 and link2:
            if link1.value < link2.value:
                p.next = link1
                link1 = link1.next
            else:
                p.next = link2
                link2 = link2.next
            p = p.next
        if link1:
            p.next = link1
        else:
            p.next = link2
        return newlink


operation = LinkOperation()
link = LinkNode(3)
link.insert(4)
link.insert(5)
link.insert(7)

operation.print(link)

link1 = LinkNode(1)
link1.insert(2)
link1.insert(6)
link1.insert(8)
link1.insert(9)

operation.print(link1)

link3 = operation.merge(link1, link)
operation.print(link3)
