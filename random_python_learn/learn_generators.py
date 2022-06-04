"""
Write BST iterator - https://leetcode.com/problems/binary-search-tree-iterator/discuss/1965156/Python-TC-O(1)-SC-O(h)-Generator-Solution

Construct BST from array level wise - https://stackoverflow.com/questions/23754060/how-to-construct-a-binary-tree-using-a-level-order-traversal-sequence
"""
from email.generator import Generator
import queue
from typing import List, Optional

# TODO fix this - learn more about generator and then fix it


class TreeNode:
    def __init__(self, val: int = 0, left: "TreeNode" = None, right: "TreeNode" = None) -> None:
        self.val = val
        self.left = left
        self.right = right


class BST:
    def __init__(self, root: "TreeNode") -> None:
        self.bst = root

    @classmethod
    def constructBST(self, arr: List[Optional[int]]) -> Optional["TreeNode"]:
        size = len(arr)
        if size == 0:
            return None
        level_complete_flag = 0
        queue = []
        root = TreeNode(arr[0])
        queue.append(root)

        level_start_node = None
        for i in range(1, size):
            new_node = TreeNode(arr[i])
            if level_complete_flag == 0:
                level_start_node = queue.pop(0)

            if level_complete_flag == 0:
                level_complete_flag += 1
                level_start_node.left = new_node
            else:
                level_complete_flag = 0
                level_start_node.right = new_node

            if arr[i] != "null":
                queue.append(new_node)

        return root


class BSTIterator:
    def __init__(self, root: Optional["TreeNode"]) -> None:
        self.iter = self._inorder(root)
        self.next_iter = next(self.iter, None)

    def _inorder(self, node: Optional["TreeNode"]):
        if node:
            yield from self._inorder(node.left)
            yield node.val
            yield from self._inorder(node.right)

    def next(self) -> int:
        ans_next, self.next_iter = self.next_iter, next(self.next_iter, None)
        return ans_next.val

    def hasNext(self) -> bool:
        return self.next_iter


if __name__ == "__main__":
    input_name = ["BSTIterator", "next", "next", "hasNext",
                  "next", "hasNext", "next", "hasNext", "next", "hasNext"]
    input_val = [[[7, 3, 15, "null", "null", 9, 20]],
                 [], [], [], [], [], [], [], [], []]

    assert len(input_name) == len(input_val)
    ans = []
    bstIterator = None
    for i in range(len(input_name)):
        if input_name[i] == "BSTIterator":
            root = BST.constructBST(arr=input_val[i][0])
            bstIterator = BSTIterator(root)
            ans.append(None)
        elif input_name[i] == "next":
            ans.append(bstIterator.next())
        elif input_name[i] == "hasNext":
            ans.append(bstIterator.hasNext())

    print(ans)
