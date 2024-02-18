# Just Compare

Just Compare is an open-source Python library designed to facilitate directory comparison.

## Features

- Identify identical and different files using hash algorithms.
- Compare files for similarity and dissimilarity using customizable metrics.
- Identify identical and different files based on directory structures.

## Prerequisites

Python >= 3.10.0

## Installation

To install Just Compare, run the following command in your terminal:

```
pip3 install jcompare
```

Or you can clone the repository and install:

```
git clone https://github.com/UFervor/JCompare.git
cd JComapre
pip3 install .
```

## Cheatsheet

-  `print_identical_files(folder1, folder2, same_parent_only=False, hash_algorithm=("sha256",))`
   - Prints identical files between two folders based on their hash values.
   - `same_parent_only`: If True, only files with the same parent folder will be compared.
   - `hash_algorithm`: Specifies the hash algorithms to use.

-  `print_different_files(folder1, folder2, same_parent_only=False, hash_algorithm=("sha256",))`
   - Prints different files between two folders based on their hash values.
   - `same_parent_only`: If True, only files with the same parent folder will be compared.
   - `hash_algorithm`: Specifies the hash algorithms to use.

-  `print_identical_files_by_mcs(folder1, folder2, ignore_directory_names=False, path=None)`
   - Prints identical files between two folders based on the maximum common subtree (MCS).
   - `ignore_directory_names`: If True, directory names will be ignored when comparing the folder structures.
   - `path`: Specifies the path to a subtree in the corresponding folder. If provided, only the specified subtrees will be compared.

-  `print_different_files_by_mcs(folder1, folder2, ignore_directory_names=False, path=None)`
   - Prints different files between two folders based on the maximum common subtree (MCS).
   - `ignore_directory_names`: If True, directory names will be ignored when comparing the folder structures.
   - `path`: Specifies the path to a subtree in the corresponding folder. If provided, only the specified subtrees will be compared.

-  `print_similar_files(folder1, folder2, threshold, same_parent_only=False, comparer=CompressionSimilarity("lzma2"), mode=ASYNC_AND_MULTIPROCESS)`
   - Prints similar files between two folders based on a similarity threshold.
   - `threshold`: Only files with a similarity score above this threshold will be considered similar.
   - `same_parent_only`: If True, only files with the same parent folder will be compared.
   - `comparer`: Specifies the similarity comparer to use.
   - `mode`: Specifies the mode to use for comparison.

-  `print_dissimilar_files(folder1, folder2, threshold, same_parent_only=False, comparer=CompressionSimilarity("lzma2"), mode=ASYNC_AND_MULTIPROCESS)`
   - Prints dissimilar files between two folders based on a similarity threshold.
   - `threshold`: Only files with a similarity score below this threshold will be considered dissimilar.
   - `same_parent_only`: If True, only files with the same parent folder will be compared.
   - `comparer`: Specifies the similarity comparer to use.
   - `mode`: Specifies the mode to use for comparison.

## Documentation

For advanced usage of this library, visit the project documentation.

## Usage Examples

### Comparing Files for Identical Content

```python
from JCompare import print_identical_files
from JCompare import Folder

folder1 = Folder("/path/to/folder")
folder2 = Folder("/path/to/archive.zip")

folder2.extract()

print_identical_files(folder1, folder2)
```

### Finding Similar Files

```python
from JCompare import Folder, CompressionSimilarity, print_similar_files

folder1 = Folder("/path/to/folder1")
folder2 = Folder("/path/to/folder2")

print_similar_files(folder1, folder2, threshold=0.9, comparer=CompressionSimilarity("zstd"))
```

### Comparing Files by directory structures

```python
from JCompare import print_identical_files
from JCompare import Folder

folder1 = Folder("/path/to/folder")
folder2 = Folder("/path/to/archive.zip")

print_different_files_by_mcs(folder1, folder2, ignore_directory_names=True)
```

## Contributing

This project is in its early stages, and we warmly welcome contributions! There are several areas that could benefit from your help:

- **Output Formatting**: The current output format could be optimized for better readability and usability.
- **Performance Optimization**: The performance of the similarity comparison is a critical area that needs immediate attention and optimization.
- **Similarity Classes**: We are open to more implementations of similarity classes to enhance the project's functionality.
- **Bug Reports**: We would appreciate your feedback if you encounter any bugs. Please help us improve by reporting these issues.

To contribute, please start by opening an issue or submitting a pull request. We look forward to your participation!
