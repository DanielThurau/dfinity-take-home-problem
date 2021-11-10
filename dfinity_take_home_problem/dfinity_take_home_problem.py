from collections import deque
import logging

from dfinity_take_home_problem.tree_node import TreeNode


def find_next_leaf(root_node, target_label):
    """Entry point to solve the dfinity_take_home_problem. Given a tree (via root node), find the
    leaf with the target_label and return a list of strings representing the path from the target
    label leaf to the "next leaf".

    Args:
        root_node (TreeNode): The root of the tree
        target_label (str): The label the algorithm searches for

    Raises:
        ValueError: If the label doesn't exist in the tree of it's node is not a leaf.

    Returns:
        list[str]: List of strings representing the path from the target label leaf to its ""next leaf".
                   Empty if no such path exists.
    """
    if root_node is None or target_label is None:
        logging.error(
            "Illegal input values: root_node:%s, target_label:%s",
            root_node,
            target_label,
        )
        return []

    path_to_label = deque()  # Python O(1) access stack object
    path_to_label = dfs(root_node, target_label, path_to_label)

    if len(path_to_label) == 0:
        raise ValueError("Label %s not found.".format(target_label))

    found_node = path_to_label[-1]
    if len(found_node.children) > 0:
        raise ValueError(
            "Label {} found but was not in a leaf node. This may cause answers that look correct but are not.".format(
                target_label
            )
        )

    return next_leaf(path_to_label)


def dfs(node, target_label, path):
    """Use the Depth First Search algorithm (recursive) to find a descendant node that matches the target_label
    while building a path to it.

    Args:
        node (TreeNode): The current node the algorithm is iterating on
        target_label (str): The value the algorithm is searching for
        path (collections.deque): A stack representing the path to the current node

    Returns:
        path: an updated version of the path based on if the target_label has been found
    """
    path.append(node)

    if node.label == target_label:
        logging.debug("Found the search value '%s'! Path to node: %s", target_label, path)
        return path

    for child in node.children:
        path = dfs(child, target_label, path)
        # Path will always have at least the current node on the stack
        peeked_node = path[-1]  
        # If theres a different node on the returned path, the path leads to the target_label
        if peeked_node != node:
            return path

    path.pop()
    return path


def next_leaf(lifo_path):
    """Given a path from a root node to a leaf node, find the next leaf in the tree.

    Args:
        lifo_path (List[TreeNode]): A list of TreeNodes where the 0th element is the root of the tree and the nth element is a leaf node

    Returns:
        List[TreeNode]: A list of TreeNodes from the leaf element from path to the next (right) possible leaf in the tree rooted by the 0th element in path. Empty list if there is no next leaf
    """
    src_node = lifo_path.pop()
    path_to_next_leaf = [src_node.label]
    last_checked = src_node

    while len(lifo_path) > 0:
        candidate = lifo_path.pop()
        path_to_next_leaf.append(candidate.label)

        # Base case. Discovered a leaf that isn't the src node
        if len(candidate.children) == 0:
            return path_to_next_leaf

        path_to_take = find_next_node(last_checked, candidate)
        if path_to_take is not None:
            lifo_path.append(path_to_take)

        last_checked = candidate

    # If the stack has run out without finding a leaf, there is no solution
    return []


def find_next_node(previous_node, current_node):
    """Given a previous_node and a current_node, check if the previous_node is one of current_node 
    children. If its not return the first child of the current_node (in this case we've already checked it has children).

    If previous_node is one of current_node's children, check if current_node is the right most node. If it is not,
    return the next node to the right in current_node's children. If previous_node is the rightmost child, return None.

    Args:
        previous_node (TreeNode): The node checked for existance
        current_node (TreeNode): The node who's children are being checked

    Returns:
        node: the next node to check or None
    """
    index = -1
    for i in range(0, len(current_node.children)):
        if current_node.children[i] == previous_node:
            index = i
            break
    # Case previous_node not one of the current_node's children. Return first child
    if index == -1:
        return current_node.children[0]
    # Case previous_node is one of the children of current_node but not the right-most
    elif index + 1 != len(current_node.children):
        return current_node.children[index + 1]
    # Case previous_node is one of current_node's children and is the rightmost
    else:
        return None
