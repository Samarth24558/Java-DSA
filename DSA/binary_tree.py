# python programme to perform binary tree

class Node:
    def __init__(self,value) -> None:
        self.left=None
        self.value=value
        self.right=None
    
class BTree:
    def __init__(self) -> None:
        self.root=None
    
    def insert_root(self,value) -> None:
        if self.root==None:
            self.root=Node(value)
        else:
            print("root node already inserted")
    
    def insert_node_left(self,value):
        new_node=Node(value)
        if self.root==None:
            print("Insert root node first")
        else:
            self.root.left=new_node
    
    def print_tree(self) -> None:
        if self.root==None:
            print("No tree")
        else:
            print("   ",end='')
            print(self.root.value)
            print("   /")
            cur=self.root
            while cur.left:
                cur=cur.left
            print(" ",cur.value)
            print("   ",end='')


if __name__=="__main__":
    tree=BTree()
    tree.print_tree()
            
            
            
            
            