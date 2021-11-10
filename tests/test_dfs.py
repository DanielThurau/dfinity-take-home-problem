from collections import deque

import dfinity_take_home_problem.dfinity_take_home_problem as df
from dfinity_take_home_problem.tree_node import TreeNode
from tests import test_utils


def test_givenRootOnlyNode_whenSearchingForRoot_thenFindRoot():
    label = "hello"
    root = TreeNode(label)
    path = deque()

    path = df.dfs(root, label, path)

    simplified_path = test_utils.simplify_path(path)
    assert len(path) == 1
    assert simplified_path == [label]

    found_node = test_utils.peek(path)
    assert found_node == root
    assert found_node.label == label


def test_givenRootOnlyNode_whenNotSearchingForRoot_thenFindNothing():
    label = "hello"
    root = TreeNode(label)
    path = deque()

    path = df.dfs(root, "non-existant-label", path)

    assert len(path) == 0


def test_givenSimpleTreeWithChildren_whenSearchingForExistingLabel_thenFindLabel():
    root = test_utils.build_simple_tree()
    path = deque()

    path = df.dfs(root, "left-child", path)
    simplified_path = test_utils.simplify_path(path)
    assert len(path) == 2
    assert simplified_path == ["root", "left-child"]

    path = deque()
    path = df.dfs(root, "center-child", path)
    simplified_path = test_utils.simplify_path(path)
    assert len(path) == 2
    assert simplified_path == ["root", "center-child"]

    path = deque()
    path = df.dfs(root, "right-child", path)
    simplified_path = test_utils.simplify_path(path)
    assert len(path) == 2
    assert simplified_path == ["root", "right-child"]


def test_givenComplexTree_whenSearchingForExistingLabel_thenFindLabel():
    root = test_utils.build_example_tree()
    path = deque()

    path = df.dfs(root, "best", path)

    simplified_path = test_utils.simplify_path(path)
    assert len(path) == 4
    assert simplified_path == ["with", "luck", "of", "best"]

    found_node = test_utils.peek(path)
    assert found_node != None
    assert found_node.label == "best"


def test_givenComplexTree_whenSearchingForNonExistingLabel_thenFindNothing():
    root = test_utils.build_example_tree()
    path = deque()

    path = df.dfs(root, "non-existant-label", path)

    assert len(path) == 0
