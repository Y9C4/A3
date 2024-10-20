from __future__ import annotations

from typing import List, Tuple, TypeVar
from algorithms.mergesort import mergesort
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
        
        This will be implemented using MergeSort, meaning it will be called recursivley.
        Args:
            elements (List[Tuple[K, I]]): The elements we wish to sort.

        Returns:
            list(Tuple[K, I]]) - elements after being sorted.

        Complexity:
            Best Case Complexity: O(n*log(n))
            Worst Case Complexity: O(n*log(n))
        """
        return mergesort(elements)

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
        def build_tree_rec(lo, hi):
            if hi - lo < 1:
                return
            # Add median
            mid = (hi + lo) // 2
            key, value = elements[mid]
            self[key] = value
            build_tree_rec(lo, mid)
            build_tree_rec(mid+1, hi)

        build_tree_rec(0, len(elements))
