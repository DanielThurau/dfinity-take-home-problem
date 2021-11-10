import logging

from dfinity_take_home_problem import dfinity_take_home_problem as df
from dfinity_take_home_problem.tree_node import TreeNode


def buildTree():
    return TreeNode(
        "with",
        [
            TreeNode(
                "luck",
                [TreeNode("good"), TreeNode("!"), TreeNode("of", [TreeNode("best")])],
            ),
            TreeNode("interviews"),
        ],
    )


def main():
    logger = logging.getLogger()
    logger.setLevel("INFO")

    root = buildTree()
    label = "best"
    path_to_leaf = df.find_next_leaf(root, label)

    logging.info("Label: '%s', Path: %s", label, path_to_leaf)


if __name__ == "__main__":
    main()
