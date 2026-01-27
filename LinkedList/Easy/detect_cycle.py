"""Given head, the head of a linked list, determine if the linked list has a cycle in it.
There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. 
Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.
Return true if there is a cycle in the linked list. Otherwise, return false.

Example 1:
Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).
Example 2:
Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.
Example 3:
Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.

Approach:
--> we shall go through each node and add that specific node to a set once it was visited and go to the next node
if that node was already in the visited set we will return it as true or else return False
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head) -> bool:
        if not head:
            return False
        
        visited = set()

        dummy_node = head

        while dummy_node:
            if dummy_node in visited:
                return True
            
            visited.add(dummy_node)

            dummy_node = dummy_node.next
        
        return False
    
# --- Your ListNode and Solution classes go here ---
if __name__ == "__main__":
    # 1. Create individual nodes
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)

    # 2. Connect them linearly: 1 -> 2 -> 3 -> 4
    node1.next = node2
    node2.next = node3
    node3.next = node4

    # 3. Create a CYCLE: point the last node back to node2
    # Now it looks like: 1 -> 2 -> 3 -> 4 --(points back to)--> 2
    node4.next = node2

    # 4. Initialize your solution and test
    sol = Solution()
    result = sol.hasCycle(node1)

    print(f"Does the list have a cycle? {result}")

