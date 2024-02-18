import asyncio
import os
from typing import Union
from tqdm import tqdm
from tqdm.asyncio import tqdm_asyncio
from .folder import Folder
from .metrics import Similarity
from .tree import find_common_path
from .mode import ASYNC_AND_MULTIPROCESS, ASYNC, SYNC


async def async_compare_files(file1: str, file2: str, folder1: Folder, folder2: Folder, loop: asyncio.AbstractEventLoop, comparer: Similarity) -> tuple[str, str, float]:
    """
    Asynchronously compares two files for similarity.

    Args:
        file1 (str): The name of the first file to compare.
        file2 (str): The name of the second file to compare.
        folder1 (Folder): The folder object containing the first file.
        folder2 (Folder): The folder object containing the second file.
        loop (asyncio.AbstractEventLoop): The event loop in which the comparison will be run.
        comparer (Similarity): The similarity comparer object used to compare the files.

    Returns:
        tuple[str, str, float]: A tuple containing the names of the two files and their similarity score.
    """

    file1_fulpath = os.path.join(folder1.folder_path, file1)
    file2_fulpath = os.path.join(folder2.folder_path, file2)

    similarity = await loop.run_in_executor(None, comparer.cmp, *((file1_fulpath, file1), (file2_fulpath, file2)))

    return file1, file2, similarity


async def async_find_similar_files(pairs: tuple[tuple[str]], folder1: Folder, folder2: Folder, threshold: float, comparer: Similarity, mode: int) -> dict[str, list[tuple[str, float]]]:
    """
    Asynchronously finds similar files between two folders.

    Args:
        pairs (tuple[tuple[str]]): A tuple of tuples, where each tuple contains the names of two files to be compared.
        folder1 (Folder): The first folder object, which contains the first file in each pair.
        folder2 (Folder): The second folder object, which contains the second file in each pair.
        threshold (float): The similarity threshold. Only pairs of files with a similarity score equal to or above this threshold will be included in the result.
        comparer (Similarity): The similarity comparer object used to compare the files.
        mode (int): The mode of operation. If set to ASYNC, the function will use asynchronous I/O. If set to ASYNC_AND_MULTIPROCESS, the function will use both asynchronous I/O and multiprocessing.

    Returns:
        dict[str, list[tuple[str, float]]]: A dictionary where each key is the relative path of a file in the first folder and each value is a list of tuples. Each tuple contains the relative path of a similar file in the second folder and the similarity score.
    """

    similar_files = {}

    loop = asyncio.get_event_loop()
    tasks = [async_compare_files(
        file1, file2, folder1, folder2, loop, comparer) for file1, file2 in pairs]

    if mode == ASYNC:
        results = []
        for task in tqdm_asyncio.as_completed(tasks, total=len(tasks), desc="Comparing files", unit="pair"):
            results.append(await task)
    elif mode == ASYNC_AND_MULTIPROCESS:
        results = await tqdm_asyncio.gather(*tasks, total=len(tasks), desc="Comparing files", unit="pair")

    for result in tqdm(results, desc="Filtering results", unit="pair"):
        file1, file2, similarity = result
        if similarity >= threshold:
            file1_relpath = os.path.relpath(file1, folder1.path)
            file2_relpath = os.path.relpath(file2, folder2.path)

            if file1_relpath not in similar_files:
                similar_files[file1_relpath] = []
            similar_files[file1_relpath].append((file2_relpath, similarity))

    return similar_files


def find_similar_files_pairwise(folder1: Folder, folder2: Folder, threshold: float, same_parent_only: bool, comparer: Similarity, mode: int) -> dict[str, list[tuple[str, float]]]:
    """
    Finds similar files between two folders in a pairwise manner.

    Args:
        folder1 (Folder): The first folder object, which contains the files to be compared.
        folder2 (Folder): The second folder object, which contains the files to be compared.
        threshold (float): The similarity threshold. Only pairs of files with a similarity score equal to or above this threshold will be included in the result.
        same_parent_only (bool): If set to True, only files with the same parent directory will be compared.
        comparer (Similarity): The similarity comparer object used to compare the files.
        mode (int): The mode of operation. If set to SYNC, the function will use synchronous I/O. If set to ASYNC, the function will use asynchronous I/O. If set to ASYNC_AND_MULTIPROCESS, the function will use both asynchronous I/O and multiprocessing.

    Raises:
        ValueError: If an invalid mode is given.

    Returns:
        dict[str, list[tuple[str, float]]]: A dictionary where each key is the relative path of a file in the first folder and each value is a list of tuples. Each tuple contains the relative path of a similar file in the second folder and the similarity score.
    """

    files1 = folder1.list
    files2 = folder2.list

    pairs = [(file1, file2) for file1 in files1 for file2 in files2]

    if same_parent_only:
        pairs = [(file1, file2) for file1, file2 in pairs if os.path.dirname(
            file1) == os.path.dirname(file2)]

    if mode == SYNC:
        similar_files = {}

        for file1, file2 in tqdm(pairs, desc="Comparing files", unit="pair"):
            file1_fulpath = os.path.join(folder1.folder_path, file1)
            file2_fulpath = os.path.join(folder2.folder_path, file2)

            similarity = comparer.cmp(
                (file1_fulpath, file1), (file2_fulpath, file2))

            if similarity >= threshold:
                if os.path.relpath(file1, folder1.path) not in similar_files:
                    similar_files[os.path.relpath(file1, folder1.path)] = []
                similar_files[os.path.relpath(file1, folder1.path)].append(
                    (os.path.relpath(file2, folder2.path), similarity))

        return similar_files

    elif mode == ASYNC or mode == ASYNC_AND_MULTIPROCESS:
        return asyncio.run(async_find_similar_files(pairs, folder1, folder2, threshold, comparer, mode))
    else:
        raise ValueError("Invalid Mode")


async def async_find_dissimilar_files(pairs: tuple[tuple[str]], dissimilar_files_folder1: dict, dissimilar_files_folder2: dict, folder1: Folder, folder2: Folder, comparer: Similarity, mode: int) -> tuple[dict[str, float], dict[str, float]]:
    """
    Asynchronously finds dissimilar files between two folders.

    Args:
        pairs (tuple[tuple[str]]): A tuple of tuples, where each tuple contains the names of two files to be compared.
        dissimilar_files_folder1 (dict): A dictionary where each key is the relative path of a file in the first folder and each value is the maximum similarity score of the file with any file in the second folder.
        dissimilar_files_folder2 (dict): A dictionary where each key is the relative path of a file in the second folder and each value is the maximum similarity score of the file with any file in the first folder.
        folder1 (Folder): The first folder object, which contains the first file in each pair.
        folder2 (Folder): The second folder object, which contains the second file in each pair.
        comparer (Similarity): The similarity comparer object used to compare the files.
        mode (int): The mode of operation. If set to ASYNC, the function will use asynchronous I/O. If set to ASYNC_AND_MULTIPROCESS, the function will use both asynchronous I/O and multiprocessing.

    Raises:
        ValueError: If an invalid mode is given.

    Returns:
        tuple[dict[str, float], dict[str, float]]: A tuple containing two dictionaries. The first dictionary stores the highest similarity score for each file in folder1, and the second dictionary stores the highest similarity score for each file in folder2.
    """

    loop = asyncio.get_event_loop()
    tasks = [async_compare_files(
        file1, file2, folder1, folder2, loop, comparer) for file1, file2 in pairs]

    if mode == ASYNC:
        results = []
        for task in tqdm_asyncio.as_completed(tasks, total=len(tasks), desc="Comparing files", unit="pair"):
            results.append(await task)
    elif mode == ASYNC_AND_MULTIPROCESS:
        results = await tqdm_asyncio.gather(*tasks, total=len(tasks), desc="Comparing files", unit="pair")
    else:
        raise ValueError("Invalid Mode")

    for result in tqdm(results, desc="Filtering results", unit="pair"):
        file1, file2, similarity = result

        dissimilar_files_folder1[file1] = max(
            similarity, dissimilar_files_folder1[file1])
        dissimilar_files_folder2[file2] = max(
            similarity, dissimilar_files_folder2[file2])

    return dissimilar_files_folder1, dissimilar_files_folder2


def find_dissimilar_files_pairwise(folder1: Folder, folder2: Folder, threshold: float, same_parent_only: bool, comparer: Similarity, mode: int) -> dict[str, Union[list[str],  bool]]:
    """
    Finds dissimilar files between two folders in a pairwise manner.

    Args:
        folder1 (Folder): The first folder object, which contains the files to be compared.
        folder2 (Folder): The second folder object, which contains the files to be compared.
        threshold (float): The similarity threshold. Only pairs of files with a similarity score below this threshold will be included in the result.
        same_parent_only (bool): If set to True, only files with the same parent directory will be compared.
        comparer (Similarity): The similarity comparer object used to compare the files.
        mode (int): The mode of operation. If set to SYNC, the function will use synchronous I/O. If set to ASYNC, the function will use asynchronous I/O. If set to ASYNC_AND_MULTIPROCESS, the function will use both asynchronous I/O and multiprocessing.

    Raises:
        ValueError: If an invalid mode is given.

    Returns:
        dict[str, Union[list[str],  bool]]: A dictionary with three keys: 'folder1', 'folder2', and 'is_similar'. The value of 'folder1' is a list of the relative paths of the dissimilar files in the first folder. The value of 'folder2' is a list of the relative paths of the dissimilar files in the second folder. The value of 'is_similar' is a boolean indicating whether the two folders are similar.
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

    dissimilar_files_folder1 = {i: 0 for i in files1_list}
    dissimilar_files_folder2 = {i: 0 for i in files2_list}

    if mode == SYNC:
        for file1, file2 in tqdm(pairs, desc="Comparing files", unit="pair"):
            if dissimilar_files_folder1[file1] >= threshold and dissimilar_files_folder2[file2] >= threshold:
                continue

            file1_fulpath = os.path.join(folder1.folder_path, file1)
            file2_fulpath = os.path.join(folder2.folder_path, file2)

            similarity = comparer.cmp(
                (file1_fulpath, file1), (file2_fulpath, file2))

            dissimilar_files_folder1[file1] = max(
                similarity, dissimilar_files_folder1[file1])
            dissimilar_files_folder2[file2] = max(
                similarity, dissimilar_files_folder2[file2])

    elif mode == ASYNC or mode == ASYNC_AND_MULTIPROCESS:
        dissimilar_files_folder1, dissimilar_files_folder2 = asyncio.run(async_find_dissimilar_files(pairs, dissimilar_files_folder1, dissimilar_files_folder2, folder1, folder2,
                                                                                                     comparer, mode))
    else:
        raise ValueError("Invalid Mode")

    dissimilar_files_folder1 = [os.path.relpath(i[0], folder1.path) for i in filter(
        lambda item: item[1] < threshold, dissimilar_files_folder1.items())]
    dissimilar_files_folder2 = [os.path.relpath(i[0], folder2.path) for i in filter(
        lambda item: item[1] < threshold, dissimilar_files_folder2.items())]

    is_similar = not (dissimilar_files_folder1 or dissimilar_files_folder2)

    result = {
        "folder1": dissimilar_files_folder1,
        "folder2": dissimilar_files_folder2,
        "is_similar": is_similar
    }

    return result
