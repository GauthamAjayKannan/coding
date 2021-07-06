class Node:
    def __init__(self,value):
        self.data=value
        self.left=None
        self.right=None
class BST:
    def __init__(self):
        self.root=None

    def insert(self,data):
        if self.root==None:
            print("inserted")
            self.root=Node(data)
        else:
            self.insertnode(self.root,data)

    def insertnode(self,node,data):
        if data<node.data:
            if node.left==None:
                node.left=Node(data)
            else:
                self.insertnode(node.left,data)
        elif data>node.data:
            if node.right==None:
                node.right=Node(data)
            else:
                self.insertnode(node.right,data)

    def traversein(self):
        if self.root==None:
            print("no nodes in binary search tree to be traversed")
        else:
            self.traverse_in_order(self.root)
                
    def traverse_in_order(self,node):
        if node.left!=None:
            self.traverse_in_order(node.left)
        print(node.data)
        if node.right!=None:
            self.traverse_in_order(node.right)

    def lca(self,x,y):
        if self.root==None:
            print("no tree is present")
        else:
            return self.lowest(self.root,x,y)
            
    def lowest(self,node,x,y):
        if node==None:
            return None
        if node.data==x or node.data==y:
            return node.data

        l=self.lowest(node.left,x,y)
        r=self.lowest(node.right,x,y)

        if l==None:
            return r
        if r==None:
            return l
        print(l,r)
        return node.data
            

a=BST()
a.insert(5)
a.insert(2)
a.insert(9)
a.insert(3)
a.insert(6)
a.insert(10)
a.insert(7)
a.insert(20)
a.traversein()
print("LCA",a.lca(10,20))
