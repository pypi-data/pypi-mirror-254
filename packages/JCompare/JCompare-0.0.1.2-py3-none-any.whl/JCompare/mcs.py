from .folder import Folder
from .tree import find_max_common_subtree, find_common_subtree, subtract_max_common_subtree, rm_common_node,  dict2list, tree2path


def find_identical_files_by_mcs(folder1: Folder, folder2: Folder, ignore_directory_names: bool = False, path: None | tuple[tuple[str], tuple[str]] = None) -> list[dict[str, list[str]]]:
    """
    Finds identical files between two folders based on the maximum common subtree (MCS).

    Args:
        folder1 (Folder): The first folder object, which contains the files to be compared.
        folder2 (Folder): The second folder object, which contains the files to be compared.
        ignore_directory_names (bool, optional): If set to True, directory names will be ignored when comparing the folder structures. Defaults to False.
        path (None | tuple[tuple[str], tuple[str]], optional): A tuple of two tuples, each containing the path to a subtree in the corresponding folder. If provided, only the specified subtrees will be compared. Defaults to None.

    Returns:
        list[dict[str, list[str]]]: A list of dictionaries. Each dictionary represents a set of identical files in an MCS (there might be multiple), with the keys being the relative paths of the files in the first folder and the values being lists of the relative paths of the identical files in the second folder.
    """

    if path == None:
        tree1 = folder1.tree
        tree2 = folder2.tree
        subtrees = find_max_common_subtree(
            tree1, tree2, ignore_directory_names)
    else:
        tree1 = folder1.tree
        tree2 = folder2.tree
        for i in path[0]:
            tree1 = tree1[i]
        for i in path[1]:
            tree2 = tree2[i]
        subtrees = [[find_common_subtree(tree1, tree2, ignore_directory_names)[
            0], path[0], path[1]]]

    results = []

    if path == None:
        path = ((), ())

    for subtree in subtrees:
        tmp = {}
        for i in dict2list(subtree[0]):
            file1 = "../" + \
                "/".join(list(path[0]) + [j[0]
                         if isinstance(j, tuple) else j for j in i])
            file2 = "../" + \
                "/".join(list(path[1]) + [j[1]
                         if isinstance(j, tuple) else j for j in i])
            tmp[file1] = [file2]
        results.append(tmp)

    return results


def find_different_files_by_mcs(folder1: Folder, folder2: Folder, ignore_directory_names: bool = False, path: None | tuple[tuple[str], tuple[str]] = None) -> list[dict[str, list[str] | str, bool]]:
    """
    Finds different files between two folders based on the maximum common subtree (MCS).

    Args:
        folder1 (Folder): The first folder object, which contains the files to be compared.
        folder2 (Folder): The second folder object, which contains the files to be compared.
        ignore_directory_names (bool, optional): If set to True, directory names will be ignored when comparing the folder structures. Defaults to False.
        path (None | tuple[tuple[str], tuple[str]], optional): A tuple of two tuples, each containing the path to a subtree in the corresponding folder. If provided, only the specified subtrees will be compared. Defaults to None.

    Returns:
        list[dict[str, list[str] | str, bool]]: A list of dictionaries. Each dictionary represents a set of different files in an MCS (there might be multiple), with the keys being the relative paths of the files in the first and second folder and a boolean indicating whether the files are identical or not.
    """

    if path == None:
        tree1 = folder1.tree
        tree2 = folder2.tree
        subtrees = find_max_common_subtree(
            tree1, tree2, ignore_directory_names)
    else:
        tree1 = folder1.tree
        tree2 = folder2.tree
        for i in path[0]:
            tree1 = tree1[i]
        for i in path[1]:
            tree2 = tree2[i]
        subtrees = [[find_common_subtree(tree1, tree2, ignore_directory_names)[
            0], path[0], path[1]]]

    results = []

    for subtree in subtrees:
        if ignore_directory_names:
            f1_tree, f2_tree = folder1.tree, folder2.tree
        else:
            f1_tree, f2_tree = rm_common_node(folder1.tree, folder2.tree)

        tree1, tree2 = subtract_max_common_subtree(
            f1_tree, f2_tree, subtree)
        results.append({
            "folder1": tree2path(tree1),
            "folder2": tree2path(tree2),
            "is_identical": not tree1 and not tree2
        })
    return results
