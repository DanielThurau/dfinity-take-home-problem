from dfinity_take_home_problem.tree_node import TreeNode


def peek(stack):
    if len(stack) > 0:
        return stack[-1]
    else:
        return None


def simplify_path(list_of_nodes):
    return [node.label for node in list_of_nodes]


def build_example_tree():
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


def build_simple_tree():
    return TreeNode(
        "root",
        [TreeNode("left-child"), TreeNode("center-child"), TreeNode("right-child")],
    )
