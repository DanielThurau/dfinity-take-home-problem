import pytest

import dfinity_take_home_problem.dfinity_take_home_problem as df
from dfinity_take_home_problem.tree_node import TreeNode
from tests import test_utils


def test_givenInvalidInput_whenSearchingForNextLeaf_thenFailToFindNextLeaf():
    path_to_next_leaf = df.find_next_leaf(None, None)
    assert len(path_to_next_leaf) == 0


def test_givenRootOnly_whenSearchingForNonExistingKey_thenThrowException():
    root = TreeNode("root")
    with pytest.raises(ValueError):
        df.find_next_leaf(root, "non-existant-label")


def test_givenRootOnly_whenSearchingForExistingKey_thenFailToFindNextLeaf():
    root = TreeNode("root")
    path_to_next_leaf = df.find_next_leaf(root, "root")

    assert len(path_to_next_leaf) == 0


def test_givenSimpleTree_whenSearchingForLabelOfNonLeafNode_thenThrowException():
    root = TreeNode("root", [TreeNode("child")])

    with pytest.raises(ValueError):
        df.find_next_leaf(root, "root")


def test_givenExampleTree_whenSearchingForNextLeaf_thenFindNextLeaf():
    root = test_utils.build_example_tree()
    path_to_next_leaf = df.find_next_leaf(root, "good")

    assert len(path_to_next_leaf) == 3
    assert path_to_next_leaf == ["good", "luck", "!"]


def test_givenExampleTree_whenSearchingForLeafInNextSubtree_thenFindNextLeaf():
    root = test_utils.build_example_tree()
    path_to_next_leaf = df.find_next_leaf(root, "best")

    assert len(path_to_next_leaf) == 5
    assert path_to_next_leaf == ["best", "of", "luck", "with", "interviews"]


def test_givenExampleTree_whenSearchingForNextLeafOfRightMostLeaf_thenFailToFindNextLeaf():
    root = test_utils.build_example_tree()
    path_to_next_leaf = df.find_next_leaf(root, "interviews")

    assert len(path_to_next_leaf) == 0
