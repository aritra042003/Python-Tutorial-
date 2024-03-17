class Node:
    def __init__(self,item=None,left=None,right=None):
        self.item=item
        self.left=left
        self.right=right
class BST:
    def __init__(self):
        self.root=None
        
    def inorder(self):
        result=[]
        self.rinorder(self.root,result)
        return result
    def rinorder(self,root,result):
        if root:
            self.rinorder(root.left,result)
            result.append(root.item)
            self.rinorder(root.right,result)
    def min_Value(self,temp):
        current=temp
        while current.left is not None:
            current=current.left
        return current.item
    def max_Value(self,temp):
        current=temp
        while current.right is not None:
            current=current.right
        return current.item
    def delete(self,data):
        self.root=self.rDelete(self.root,data)
    def rDelete(self,root,data):
        if root is None:
            return root
        if data<root.item:
            root.left=self.rDelete(root.left,data)
           
        elif data>root.item:
            root.right=self.rDelete(root.right,data)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            root.item=self.min_Value(root.right)
            self.rDelete(root.right,root.item)
        return root
    def size(self):
        return len(self.inorder())
            
        
    
        
        
        
        
        
        
        
        
        
        
        
        
        
    
    
        