class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def helper(node, low=float("-inf"), high=float("inf")):
            if not node:
                return True
            if not (low < node.val < high):
                return False
            return (helper(node.left, low, node.val) and
                    helper(node.right, node.val, high))
        
        return helper(root)



root1 = TreeNode(2)
root1.left = TreeNode(1)
root1.right = TreeNode(3)


root2 = TreeNode(5)
root2.left = TreeNode(1)
root2.right = TreeNode(4)
root2.right.left = TreeNode(3)
root2.right.right = TreeNode(6)


root3 = TreeNode(10)
root3.left = TreeNode(5)
root3.right = TreeNode(15)
root3.right.left = TreeNode(6)
root3.right.right = TreeNode(20)

sol = Solution()
print(sol.isValidBST(root1))  
print(sol.isValidBST(root2))  
print(sol.isValidBST(root3))  
