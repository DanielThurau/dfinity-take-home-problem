from collections import deque

from dfinity_take_home_problem.tree_node import TreeNode
import dfinity_take_home_problem.dfinity_take_home_problem as df


def test_givenRootOnly_whenSearchingForNextLeaf_thenFailToFindNextLeaf():
    root = TreeNode("hello")
    path = deque([root])

    path_to_leaf = df.next_leaf(path)

    assert len(path_to_leaf) == 0


def test_givenRootAndChild_whenSearchingForNextLeaf_thenFailToFindLeaf():
    child = TreeNode("world")
    root = TreeNode("hello", [child])
    path = deque([root, child])

    path_to_leaf = df.next_leaf(path)

    assert len(path_to_leaf) == 0


def test_givenSimpleTree_whenSearchingForNextLeafFromLeft_thenFindLeaf():
    left = TreeNode("left")
    center = TreeNode("center")
    right = TreeNode("right")
    root = TreeNode("root", [left, center, right])
    path = deque([root, left])

    path_to_leaf = df.next_leaf(path)

    assert len(path_to_leaf) == 3
    assert path_to_leaf == ["left", "root", "center"]


# Important test to know it can move to the next child from the center of a sibling list
def test_givenSimpleTree_whenSearchingForNextLeafFromCenter_thenFindLeaf():
    left = TreeNode("left")
    center = TreeNode("center")
    right = TreeNode("right")
    root = TreeNode("root", [left, center, right])
    path = deque([root, center])

    path_to_leaf = df.next_leaf(path)

    assert len(path_to_leaf) == 3
    assert path_to_leaf == ["center", "root", "right"]


def test_givenSimpleTree_whenSearchingForNextLeafFromRight_thenFailToFindLeaf():
    left = TreeNode("left")
    center = TreeNode("center")
    right = TreeNode("right")
    root = TreeNode("root", [left, center, right])
    path = deque([root, right])

    path_to_leaf = df.next_leaf(path)
    assert len(path_to_leaf) == 0


#                “root”
#              /       \
#             /         \
#       “left-child”  “right-child"
#          /
#  “left-grand-child”
def test_givenTree_whenSearchingForNextLeaf_thenFindLeafInNextSubtree_depthHigher():
    left_gchild = TreeNode("left-grand-child")
    left_child = TreeNode("left-child", [left_gchild])
    right_child = TreeNode("right-child")
    root = TreeNode("root", [left_child, right_child])
    path = deque([root, left_child, left_gchild])

    path_to_leaf = df.next_leaf(path)

    assert len(path_to_leaf) == 4
    assert path_to_leaf == [
        "left-grand-child",
        "left-child",
        "root",
        "right-child",
    ]


#                “root”
#              /       \
#             /         \
#       “left-child”  “right-child"
#          /               \
#  “left-grand-child”   "right-grand-child"
def test_givenTree_whenSearchingForNextLeaf_thenFindLeafInNextSubtree_depthEquivalent():
    left_gchild = TreeNode("left-grand-child")
    left_child = TreeNode("left-child", [left_gchild])
    right_gchild = TreeNode("right-grand-child")
    right_child = TreeNode("right-child", [right_gchild])
    root = TreeNode("root", [left_child, right_child])
    path = deque([root, left_child, left_gchild])

    path_to_leaf = df.next_leaf(path)

    assert len(path_to_leaf) == 5
    assert path_to_leaf == [
        "left-grand-child",
        "left-child",
        "root",
        "right-child",
        "right-grand-child",
    ]


#                “root”
#              /       \
#             /         \
#       “left-child”  “right-child"
#          /               /
#  “left-grand-child”   "right-grand-child"
#                             /
#                         "right-great-grand-child"
def test_givenTree_whenSearchingForNextLeaf_thenFindLeafInNextSubtree_depthLower():
    left_gchild = TreeNode("left-grand-child")
    left_child = TreeNode("left-child", [left_gchild])
    right_ggchild = TreeNode("right-great-grand-child")
    right_gchild = TreeNode("right-grand-child", [right_ggchild])
    right_child = TreeNode("right-child", [right_gchild])
    root = TreeNode("root", [left_child, right_child])
    path = deque([root, left_child, left_gchild])

    path_to_leaf = df.next_leaf(path)

    assert len(path_to_leaf) == 6
    assert path_to_leaf == [
        "left-grand-child",
        "left-child",
        "root",
        "right-child",
        "right-grand-child",
        "right-great-grand-child",
    ]
