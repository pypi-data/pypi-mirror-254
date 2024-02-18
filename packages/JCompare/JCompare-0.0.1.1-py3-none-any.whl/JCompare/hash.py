import os
from typing import Union
import hashlib
from tqdm import tqdm
from .folder import Folder
from .tree import find_common_path


def calculate_file_hash(file_path: str, hash_algorithm: str) -> str:
    """
    Calculates the hash of a file using the specified hash algorithm.

    Args:
        file_path (str): The path to the file for which to calculate the hash.
        hash_algorithm (str): The name of the hash algorithm to use. This must be a string specifying the name of a hash algorithm available in the hashlib module.

    Returns:
        str: The hexadecimal representation of the hash of the file.
    """

    hash_object = hashlib.new(hash_algorithm)
    with open(file_path, 'rb') as file:
        while chunk := file.read(4096):
            hash_object.update(chunk)
    return hash_object.hexdigest()


def calculate_hash(files1_list: list[str], files2_list: list[str], folder1: Folder, folder2: Folder, hash_algorithm: tuple[str]) -> tuple[dict[str, tuple[str]], dict[str, tuple[str]]]:
    """
    Calculates the hash(es) of the files in two folders using the specified hash algorithms.

    Args:
        files1_list (list[str]): A list of relative paths to the files in the first folder for which to calculate the hash.
        files2_list (list[str]): A list of relative paths to the files in the second folder for which to calculate the hash.
        folder1 (Folder): The first folder object, which contains the files for which to calculate the hash.
        folder2 (Folder): The second folder object, which contains the files for which to calculate the hash.
        hash_algorithm (tuple[str]): A tuple of strings specifying the names of the hash algorithms to use.

    Returns:
        tuple[dict[str, tuple[str]], dict[str, tuple[str]]]: A tuple of two dictionaries. Each dictionary maps a file path to a tuple of hash values, one for each hash algorithm.
    """

    hash_dict1 = {}
    hash_dict2 = {}

    pbar = tqdm(total=(len(files1_list)+len(files2_list)) *
                len(hash_algorithm), desc="Calculating hash", unit="hash")
    for file in files1_list:
        for i in hash_algorithm:
            hash_dict1[file] = calculate_file_hash(
                folder1.get_file(file).name, i)
            pbar.update()

    for file in files2_list:
        for i in hash_algorithm:
            hash_dict2[file] = calculate_file_hash(
                folder2.get_file(file).name, i)
            pbar.update()

    return hash_dict1, hash_dict2


def find_identical_files(folder1: Folder, folder2: Folder, same_parent_only: bool, hash_algorithm: tuple[str]) -> dict[str, list[str]]:
    """
    Finds identical files between two folders based on their hash values.

    Args:
        folder1 (Folder): The first folder object, which contains the files to be compared.
        folder2 (Folder): The second folder object, which contains the files to be compared.
        same_parent_only (bool): If set to True, only files with the same parent folder will be compared.
        hash_algorithm (tuple[str]): A tuple of strings specifying the names of the hash algorithms to use.

    Returns:
        dict[str, list[str]]: A dictionary mapping the relative paths of the identical files in the first folder to lists of the relative paths of the identical files in the second folder.
    """

    if same_parent_only:
        pairs = find_common_path(folder1.tree, folder2.tree)
        files1_list = [i[0] for i in pairs]
        files2_list = [i[1] for i in pairs]
    else:
        files1_list = folder1.list
        files2_list = folder2.list
        pairs = tuple((file1, file2)
                      for file1 in files1_list for file2 in files2_list)

    files1_list = list(set(files1_list))
    files2_list = list(set(files2_list))

    hash_dict1, hash_dict2 = calculate_hash(
        files1_list, files2_list, folder1, folder2, hash_algorithm)

    identical_files = {}

    for file1, file2 in pairs:
        if hash_dict1[file1] == hash_dict2[file2]:
            file1_relpath = os.path.relpath(file1, folder1.path)
            file2_relpath = os.path.relpath(file2, folder2.path)

            if file1_relpath not in identical_files:
                identical_files[file1_relpath] = []
            identical_files[file1_relpath].append(file2_relpath)

    return identical_files


def find_different_files(folder1: Folder, folder2: Folder, same_parent_only: bool, hash_algorithm: tuple[str]) -> dict[str, Union[list[str], bool]]:
    """
    Finds different files between two folders based on their hash values.

    Args:
        folder1 (Folder): The first folder object, which contains the files to be compared.
        folder2 (Folder): The second folder object, which contains the files to be compared.
        same_parent_only (bool): If set to True, only files with the same parent folder will be compared.
        hash_algorithm (tuple[str]): A tuple of strings specifying the names of the hash algorithms to use.

    Returns:
        dict[str, Union[list[str], bool]]: A dictionary with keys "folder1", "folder2", and "is_identical". The values for "folder1" and "folder2" are lists of the relative paths of the different files in the respective folders. The value for "is_identical" is a boolean indicating whether the two folders are identical.
    """

    if same_parent_only:
        pairs = find_common_path(folder1.tree, folder2.tree)
        files1_list = [i[0] for i in pairs]
        files2_list = [i[1] for i in pairs]
    else:
        files1_list = folder1.list
        files2_list = folder2.list
        pairs = tuple((file1, file2)
                      for file1 in files1_list for file2 in files2_list)

    files1_list = list(set(files1_list))
    files2_list = list(set(files2_list))

    hash_dict1, hash_dict2 = calculate_hash(
        files1_list, files2_list, folder1, folder2, hash_algorithm)

    name_dict1 = {i: [] for i in files1_list}
    name_dict2 = {i: [] for i in files2_list}
    for file1, file2 in pairs:
        name_dict1[file1].append(file2)
        name_dict2[file2].append(file1)

    different_files_folder1 = []
    different_files_folder2 = []

    for file1, file1_hash in hash_dict1.items():
        if file1_hash not in [hash_dict2[i] for i in name_dict1[file1]]:
            different_files_folder1.append(
                os.path.relpath(file1, folder1.path))

    for file2, file2_hash in hash_dict2.items():
        if file2_hash not in [hash_dict1[i] for i in name_dict2[file2]]:
            different_files_folder2.append(
                os.path.relpath(file2, folder2.path))

    is_identical = not (different_files_folder1 or different_files_folder2)

    result = {
        "folder1": different_files_folder1,
        "folder2": different_files_folder2,
        "is_identical": is_identical
    }

    return result
