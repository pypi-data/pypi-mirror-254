from dict_hash import sha256


def find_common_path(subtree1: dict, subtree2: dict, path: tuple[str] = ()) -> tuple[tuple[str, str]]:
    """
    Compares two dictionary-based tree structures and returns a tuple of common paths.

    Args:
        subtree1 (dict): The first tree to compare. This is a nested dictionary where each key-value pair represents a node and its subtree.
        subtree2 (dict): The second tree to compare. This is a nested dictionary where each key-value pair represents a node and its subtree.
        path (tuple[str], optional): The current path in the tree traversal. Defaults to an empty tuple.

    Returns:
        tuple[tuple[str, str]]: A tuple of tuples, where each inner tuple contains two strings representing common paths in the two trees.
    """

    if not isinstance(subtree1, dict) or not isinstance(subtree2, dict):
        return []

    result = []
    for i in tuple((key1, value1, key2, value2) for key1, value1 in subtree1.items() for key2, value2 in subtree2.items()):
        if i[0] == i[2] and isinstance(i[1], dict) and isinstance(i[3], dict):
            result.extend(find_common_path(i[1], i[3], path + (i[0],)))
        elif i[1] is None and i[3] is None:
            result.append(("/".join(path + (i[0],)), "/".join(path + (i[2],))))

    return result


def rm_common_node(tree1: dict, tree2: dict, path: tuple[str] = ()) -> tuple[dict, dict]:
    """
    Compares two dictionary-based tree structures and removes common nodes.

    Args:
        tree1 (dict): The first tree to compare. This is a nested dictionary where each key-value pair represents a node and its subtree.
        tree2 (dict): The second tree to compare. This is a nested dictionary where each key-value pair represents a node and its subtree.
        path (tuple[str], optional): The current path in the tree traversal. Defaults to an empty tuple.

    Returns:
        tuple[dict, dict]: A tuple of two dictionaries, each representing the tree structure with common nodes removed.
    """

    if not isinstance(tree1, dict) or not isinstance(tree2, dict):
        return tree1, tree2

    new_tree1 = {}
    new_tree2 = {}

    all_keys = set(tree1.keys()) | set(tree2.keys())

    for key in all_keys:
        if key in tree1 and key not in tree2:
            new_tree1[key] = tree1[key]
        elif key in tree2 and key not in tree1:
            new_tree2[key] = tree2[key]
        elif key in tree1 and key in tree2:
            if isinstance(tree1[key], dict) and isinstance(tree2[key], dict):
                new_tree1[key], new_tree2[key] = rm_common_node(
                    tree1[key], tree2[key], path + (key,))
                if not new_tree1[key]:
                    del new_tree1[key]
                if not new_tree2[key]:
                    del new_tree2[key]

    return new_tree1, new_tree2


def find_common_subtree(subtree1: dict, subtree2: dict, ignore_directory_names: bool = False) -> tuple[dict, int]:
    """
    Finds the common subtree between two given dictionary-based tree structures.

    Args:
        subtree1 (dict): The first tree to compare. This is a nested dictionary where each key-value pair represents a node and its subtree.
        subtree2 (dict): The second tree to compare. This is a nested dictionary where each key-value pair represents a node and its subtree.
        ignore_directory_names (bool, optional): If set to True, the function will ignore directory names and only compare the structure of the trees. Defaults to False.

    Returns:
        tuple[dict, int]: A tuple containing two elements. The first element is a dictionary representing the common subtree. The second element is an integer representing the size of the common subtree.
    """

    if not isinstance(subtree1, dict) or not isinstance(subtree2, dict):
        return {}, 0

    common_subtree = {}
    size = 0

    # Compare files directly
    for key in subtree1:
        if key in subtree2 and subtree1[key] is None and subtree2[key] is None:
            common_subtree[key] = None
            size += 1

    if ignore_directory_names:
        # Compare directories by structure, not by name
        for key1, child1 in subtree1.items():
            if isinstance(child1, dict):
                for key2, child2 in subtree2.items():
                    if isinstance(child2, dict):
                        common_child, child_size = find_common_subtree(
                            child1, child2, ignore_directory_names)
                        if common_child is not None:
                            if size == 0:
                                continue
                            common_key = key1 if key1 == key2 else (key1, key2)
                            common_subtree[common_key] = common_child
                            size += child_size

    else:
        # Compare directories by name
        for key in subtree1:
            if key in subtree2 and isinstance(subtree1[key], dict) and isinstance(subtree2[key], dict):
                common_child, child_size = find_common_subtree(
                    subtree1[key], subtree2[key], ignore_directory_names)
                if common_child is not None:
                    common_subtree[key] = common_child
                    size += child_size

    return common_subtree, size


def find_max_common_subtree(tree1: dict, tree2: dict, ignore_directory_names: bool = False) -> list[tuple[dict, tuple, tuple]]:
    """
    Finds the maximum common subtree(s) between two given dictionary-based tree structures.

    Args:
        tree1 (dict): The first tree to compare. This is a nested dictionary where each key-value pair represents a node and its subtree.
        tree2 (dict): The second tree to compare. This is a nested dictionary where each key-value pair represents a node and its subtree.
        ignore_directory_names (bool, optional): If set to True, the function will ignore directory names and only compare the structure of the trees. Defaults to False.

    Returns:
        list[tuple[dict, tuple, tuple]]: A list of tuples, where each tuple contains three elements. The first element is a dictionary representing the common subtree. The second and third elements are tuples representing the paths to the common subtree in the first and second trees, respectively.
    """

    max_subtree_info = []
    subtree_hash = set()
    max_size = 0

    def traverse_trees(node1: dict, node2: dict, path1: tuple[str] = (), path2: tuple[str] = ()) -> None:
        nonlocal max_subtree_info, max_size, subtree_hash
        common, size = find_common_subtree(
            node1, node2, ignore_directory_names)
        if size > max_size:
            max_subtree_info = [(common, path1, path2)]
            subtree_hash.add(sha256(common))
            max_size = size
        elif size == max_size:
            if sha256(common) not in subtree_hash:
                max_subtree_info.append((common, path1, path2))
                subtree_hash.add(sha256(common))

        if isinstance(node1, dict):
            for key, child in node1.items():
                traverse_trees(child, node2, path1 + (key,), path2)

        if isinstance(node2, dict):
            for key, child in node2.items():
                traverse_trees(node1, child, path1, path2 + (key,))

    traverse_trees(tree1, tree2)
    return max_subtree_info


def subtract_common_subtree(tree: dict, common_subtree: dict, path=()) -> dict:
    """
    Removes a given (common) subtree from the given tree.

    Args:
        tree (dict): The original tree. This is a nested dictionary where each key-value pair represents a node and its subtree.
        common_subtree (dict): The common subtree to be removed. This is a nested dictionary where each key-value pair represents a node and its subtree.
        path (tuple, optional): The path to the subtree in the original tree that should be compared with the common subtree. Defaults to an empty tuple, which means the whole tree will be compared.

    Returns:
        dict: The original tree with the common subtree removed. This is a nested dictionary where each key-value pair represents a node and its subtree.
    """

    if not path:
        for key, value in common_subtree.items():
            if key in tree and tree[key] == value:
                del tree[key]
            elif key in tree and isinstance(value, dict):
                subtract_common_subtree(tree[key], value)
                if not tree[key]:
                    del tree[key]
            elif isinstance(key, tuple) and isinstance(value, dict):
                for i in key:
                    if i in tree:
                        subtract_common_subtree(tree[i], value)
                        if not tree[i]:
                            del tree[i]
        return tree

    current = tree
    for key in path[:-1]:
        current = current.get(key, {})
        if not isinstance(current, dict):
            return tree

    last_key = path[-1]
    subtree = current.get(last_key, {})
    if not isinstance(subtree, dict):
        return tree

    for key, value in common_subtree.items():
        if key in subtree and subtree[key] == value:
            del subtree[key]
        elif key in subtree and isinstance(value, dict):
            subtract_common_subtree(subtree[key], value)
            if not subtree[key]:
                del subtree[key]

    if not subtree:
        del current[last_key]

    return tree


def subtract_max_common_subtree(tree1: dict, tree2: dict, max_common_subtree_info: tuple[dict, tuple, tuple]) -> tuple[dict, dict]:
    """
    Removes a given maximum common subtree from the given trees.

    Args:
        tree1 (dict): The first original tree. This is a nested dictionary where each key-value pair represents a node and its subtree.
        tree2 (dict): The second original tree. This is a nested dictionary where each key-value pair represents a node and its subtree.
        max_common_subtree_info (tuple[dict, tuple, tuple]): A tuple containing three elements. The first element is a dictionary representing the maximum common subtree. The second and third elements are tuples representing the paths to the maximum common subtree in the first and second trees, respectively.

    Returns:
        tuple[dict, dict]: A tuple containing two dictionaries, each representing the original tree with the maximum common subtree removed.
    """

    if not max_common_subtree_info:
        return tree1, tree2

    common_subtree, path1, path2 = max_common_subtree_info
    modified_tree1 = subtract_common_subtree(tree1, common_subtree, path1)
    modified_tree2 = subtract_common_subtree(tree2, common_subtree, path2)

    return modified_tree1, modified_tree2


def dict2list(dic: dict, prefix: list = []) -> list[list[str]]:
    """
    Converts a nested dictionary into a list of lists, where each list represents a path in the dictionary.

    Args:
        dic (dict): The original dictionary. This is a nested dictionary where each key-value pair represents a node and its subtree.
        prefix (list, optional): The current path in the dictionary traversal. Defaults to an empty list.

    Returns:
        list[list[str]]: A list of lists, where each list represents a path in the dictionary. The order of the paths is the same as the order of the keys in the dictionary.
    """

    res = []
    for k, v in dic.items():
        cur_key = prefix + [k]
        if isinstance(v, dict):
            res.extend(dict2list(v, cur_key))
        else:
            res.append(cur_key)
    return res


def tree2path(tree: dict) -> list[str]:
    """
    Converts a nested dictionary-based tree structure into a list of paths.

    Args:
        tree (dict): The original tree. This is a nested dictionary where each key-value pair represents a node and its subtree.

    Returns:
        list[str]: A list of strings, where each string represents a path in the tree. The paths are relative to the parent directory of the tree.
    """

    return ["../"+"/".join(i) for i in dict2list(tree)]
