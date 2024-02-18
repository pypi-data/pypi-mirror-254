from .folder import Folder
from .metrics import Similarity, CompressionSimilarity
from .hash import find_identical_files, find_different_files
from .similarity import find_similar_files_pairwise, find_dissimilar_files_pairwise
from .mcs import find_identical_files_by_mcs, find_different_files_by_mcs
from .mode import ASYNC_AND_MULTIPROCESS, ASYNC, SYNC


def print_identical_files(folder1: Folder, folder2: Folder, same_parent_only: bool = False, hash_algorithm: tuple[str] = ("sha256",)) -> None:
    """
    Prints the identical files between two folders based on their hash values.

    Args:
        folder1 (Folder): The first folder object, which contains the files to be compared.
        folder2 (Folder): The second folder object, which contains the files to be compared.
        same_parent_only (bool, optional): If set to True, only files with the same parent folder will be compared. Defaults to False.
        hash_algorithm (tuple[str], optional): A tuple of strings specifying the names of the hash algorithms to use. Defaults to ("sha256",).
    """

    result = find_identical_files(
        folder1, folder2, same_parent_only, hash_algorithm)

    for key, value in result.items():
        print(f"+ {key}")
        for i in value:
            print(f"  - {i}")


def print_different_files(folder1: Folder, folder2: Folder, same_parent_only: bool = False, hash_algorithm: tuple[str] = ("sha256",)) -> None:
    """
    Prints the different files between two folders based on their hash values.

    Args:
        folder1 (Folder): The first folder object, which contains the files to be compared.
        folder2 (Folder): The second folder object, which contains the files to be compared.
        same_parent_only (bool, optional): If set to True, only files with the same parent folder will be compared. Defaults to False.
        hash_algorithm (tuple[str], optional): A tuple of strings specifying the names of the hash algorithms to use. Defaults to ("sha256",).
    """

    result = find_different_files(
        folder1, folder2, same_parent_only, hash_algorithm)

    if result["is_identical"]:
        print("The folders are identical.")
    else:
        print("Different files found:")
        if result['folder1']:
            print(f"Only in folder1:")
            for i in result['folder1']:
                print(f"+ {i}")
        if result['folder2']:
            print(f"Only in folder2:")
            for i in result['folder2']:
                print(f"+ {i}")


def print_identical_files_by_mcs(folder1: Folder, folder2: Folder, ignore_directory_names: bool = False, path: None | tuple[tuple[str], tuple[str]] = None) -> None:
    """
    Prints the identical files between two folders based on the maximum common subtree (MCS).

    Args:
        folder1 (Folder): The first folder object, which contains the files to be compared.
        folder2 (Folder): The second folder object, which contains the files to be compared.
        ignore_directory_names (bool, optional): If set to True, directory names will be ignored when comparing the folder structures. Defaults to False.
        path (None | tuple[tuple[str], tuple[str]], optional): A tuple of two tuples, each containing the path to a subtree in the corresponding folder. If provided, only the specified subtrees will be compared. Defaults to None.
    """

    results = find_identical_files_by_mcs(
        folder1, folder2, ignore_directory_names, path)

    for result in results:
        for key, value in result.items():
            print(f"+ {key}")
            for i in value:
                print(f"  - {i}")


def print_different_files_by_mcs(folder1: Folder, folder2: Folder, ignore_directory_names: bool = False, path: None | tuple[tuple[str], tuple[str]] = None) -> None:
    """
    Prints the different files between two folders based on the maximum common subtree (MCS).

    Args:
        folder1 (Folder): The first folder object, which contains the files to be compared.
        folder2 (Folder): The second folder object, which contains the files to be compared.
        ignore_directory_names (bool, optional): If set to True, directory names will be ignored when comparing the folder structures. Defaults to False.
        path (None | tuple[tuple[str], tuple[str]], optional): A tuple of two tuples, each containing the path to a subtree in the corresponding folder. If provided, only the specified subtrees will be compared. Defaults to None.
    """

    results = find_different_files_by_mcs(
        folder1, folder2, ignore_directory_names, path)

    for result in results:
        if result["is_identical"]:
            print("The folders are identical.")
        else:
            print("Different files found:")
            if result['folder1']:
                print(f"Only in folder1:")
                for i in result['folder1']:
                    print(f"+ {i}")
            if result['folder2']:
                print(f"Only in folder2:")
                for i in result['folder2']:
                    print(f"+ {i}")


def print_similar_files(folder1: Folder, folder2: Folder, threshold: float, same_parent_only: bool = False, comparer: Similarity = CompressionSimilarity("lzma2"), mode: int = ASYNC_AND_MULTIPROCESS) -> None:
    """
    Prints the similar files between two folders based on a similarity threshold.

    Args:
        folder1 (Folder): The first folder object, which contains the files to be compared.
        folder2 (Folder): The second folder object, which contains the files to be compared.
        threshold (float): The similarity threshold. Only files with a similarity score above this threshold will be considered similar.
        same_parent_only (bool, optional): If set to True, only files with the same parent folder will be compared. Defaults to False.
        comparer (Similarity, optional): The similarity comparer to use. Defaults to CompressionSimilarity("lzma2").
        mode (int, optional): The mode to use for comparison. Defaults to ASYNC_AND_MULTIPROCESS.
    """

    result = find_similar_files_pairwise(
        folder1, folder2, threshold, same_parent_only, comparer, mode)

    for key, value in result.items():
        print(f"+ {key}")
        for i in value:
            print(f"  - {i[0]} {i[1]*100:.2f}%")


def print_dissimilar_files(folder1: Folder, folder2: Folder, threshold: float, same_parent_only: bool = False, comparer: Similarity = CompressionSimilarity("lzma2"), mode: int = ASYNC_AND_MULTIPROCESS) -> None:
    """
    Prints the dissimilar files between two folders based on a similarity threshold.

    Args:
        folder1 (Folder): The first folder object, which contains the files to be compared.
        folder2 (Folder): The second folder object, which contains the files to be compared.
        threshold (float): The similarity threshold. Only files with a similarity score below this threshold will be considered dissimilar.
        same_parent_only (bool, optional): If set to True, only files with the same parent folder will be compared. Defaults to False.
        comparer (Similarity, optional): The similarity comparer to use. Defaults to CompressionSimilarity("lzma2").
        mode (int, optional): The mode to use for comparison. Defaults to ASYNC_AND_MULTIPROCESS.
    """

    result = find_dissimilar_files_pairwise(
        folder1, folder2, threshold, same_parent_only, comparer, mode)

    if result["is_similar"]:
        print("The folders are similar.")
    else:
        print("Dissimilar files found:")
        if result["folder1"]:
            print(f"Only in folder1:")
            for i in result['folder1']:
                print(f"+ {i}")
        if result["folder2"]:
            print(f"Only in folder2:")
            for i in result['folder2']:
                print(f"+ {i}")
