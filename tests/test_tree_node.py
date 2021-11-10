import pytest

from dfinity_take_home_problem.tree_node import TreeNode


def test_givenInvalidInput_whenCreatingTreeNode_thenFail():
    with pytest.raises(ValueError):
        TreeNode(None, [])

    with pytest.raises(ValueError):
        TreeNode("label", None)
