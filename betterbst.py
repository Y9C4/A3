from __future__ import annotations

from typing import List, Tuple, TypeVar

from data_structures.bst import BinarySearchTree, TreeNode

K = TypeVar('K')
I = TypeVar('I')


class BetterBST(BinarySearchTree[K, I]):
    def __init__(self, elements: List[Tuple[K, I]]) -> None:
        """
        Initialiser for the BetterBST class.
        We assume that the all the elements that will be inserted
        into the tree are contained within the elements list.

        As such you can assume the length of elements to be non-zero.
        The elements list will contain tuples of key, item pairs.

        First sort the elements list and then build a balanced tree from the sorted elements
        using the corresponding methods below.

        Args:
            elements(List[tuple[K, I]]): The elements to be inserted into the tree.

        Complexity:
            Best Case Complexity: TODO
            Worst Case Complexity: TODO
        """
        super().__init__()
        new_elements: List[Tuple[K, I]] = self.__sort_elements(elements)
        self.__build_balanced_tree(new_elements)

    def __sort_elements(self, elements: List[Tuple[K, I]]) -> List[Tuple[K, I]]:
        """
        Recall one of the drawbacks to using a binary search tree is that it can become unbalanced.
        If we know the elements ahead of time, we can sort them and then build a balanced tree.
        This will help us maintain the O(log n) complexity for searching, inserting, and deleting elements.
        
        Implemented using MergeSort.

        Args:
            elements (List[Tuple[K, I]]): The elements we wish to sort.

        Returns:
            list(Tuple[K, I]]) - elements after being sorted.

        Complexity:
            Best Case Complexity: O(n*log(n))
            Worst Case Complexity: O(n*log(n))
        """

        if len(elements) <= 1:  # Base case: empty list or single element list
            return elements

        # Step 1: Divide the list into two halves
        mid = len(elements) // 2
        left = self.__sort_elements(elements[:mid])  # Sort left half
        right = self.__sort_elements(elements[mid:])  # Sort right half

        # Step 2: Merge the sorted halves
        return self.__merge(left, right)
    
    def __merge(self, left: List[Tuple[K, I]], right: List[Tuple[K, I]]) -> List[Tuple[K, I]]:
            merged = []
            i = 0
            j = 0

            while i < len(left) and j < len(right):
                if left[i][0] <= right[j][0]:
                    merged.append(left[i])
                    i += 1
                else:
                    merged.append(right[j])
                    j += 1

            merged.extend(left[i:])
            merged.extend(right[j:])
            return merged

    def __build_balanced_tree(self, elements: List[Tuple[K, I]]) -> None:
        """
        This method will build a balanced binary search tree from the sorted elements.

        Args:
            elements (List[Tuple[K, I]]): The elements we wish to use to build our balanced tree.

        Returns:
            None

        Complexity:
            Best Case Complexity: O(n)
            Worst Case Complexity: O(n)

        Justification:
            The tree is built by recursively dividing the list into halves, leading to a balanced structure.
        """
        # Base Case: stops when there are no more elements in the list
        if len(elements) < 1:
            return 

        # Step 1: Find the median
        mid = len(elements) // 2
        median = elements[mid]

        # Step 2: Insert the median into the tree
        if self.root is None:
            print(len(elements))
            self.root = TreeNode(median[0], median[1])  # Initialize the root
        else:
            self.insert_aux(self.root, median[0], median[1], self.root.depth)  # Insert using the insertion logic

        # Step 3: Recursively build left and right subtrees
        left = elements[:mid]  # Left half of the elements
        right = elements[mid + 1:]  # Right half of the elements, skipping the median

        # Build the left and right subtrees
        self.__build_balanced_tree(left)
        self.__build_balanced_tree(right)
