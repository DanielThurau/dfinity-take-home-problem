class TreeNode:
    def __init__(self, label, children=[]):
        if label is None:
            raise ValueError("Cannot init TreeNode with no value")
        elif children is None:
            raise ValueError(
                "Cannot init TreeNode with None type for children. Consider using an empty list"
            )

        self.label = label
        self.children = children

    def __str__(self):  # pragma: no cover
        return "Label: '{}'. Children: {}".format(
            self.label, str([child.label for child in self.children])
        )

    def __repr__(self):  # pragma: no cover
        return self.__str__()
