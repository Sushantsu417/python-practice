# Find Largest Value in Each Tree Row

class Solution(object):
    def largestValues(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        if not root:
            return []

        result = []
        level = [root]

        while level:
            max_value = float('-inf')
            next_level = []

            for node in level:
            
                max_value = max(max_value, node.val)
           
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)

            result.append(max_value)
            level = next_level

        return result
