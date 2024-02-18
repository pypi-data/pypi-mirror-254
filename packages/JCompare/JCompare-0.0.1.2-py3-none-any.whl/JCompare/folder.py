import os
import shutil
import tempfile
import patoolib
import sys
from io import StringIO, BytesIO
from .tree import dict2list


def execute_python_code(code: str) -> str | None:
    """
    Executes the given Python code and captures its output.

    Args:
        code (str): The Python code to execute.

    Returns:
        Optional[str]: The output of the executed code as a string, or None if an error occurred during execution.
    """

    try:
        original_stdout = sys.stdout
        captured_output = StringIO()
        sys.stdout = captured_output
        exec(code)
        sys.stdout = original_stdout
        return captured_output.getvalue()
    except Exception as e:
        print(f"Error: {e}")
        return None


class Folder:
    def __init__(self, path: str, exclude_files: list[str] = ["Thumbs.db", ".DS_Store"], lazy: bool = True, dissolve: bool = True) -> None:
        """
        Initializes a new instance of the Folder class.

        Args:
            path (str): The path to the folder or compressed file.
            exclude_files (list[str], optional): A list of filenames to exclude. Defaults to ["Thumbs.db", ".DS_Store"].
            lazy (bool, optional): If set to True, compressed files will not be extracted when initialized. Defaults to True.
            dissolve (bool, optional): If set to True, the **only** top-level directory of a compressed file will be ignored if its name equals the archive's. Defaults to True.
        """

        self.path = path

        self.exclude_files = set(exclude_files)
        self.is_compressed = not os.path.isdir(self.path)
        self.extracted = False
        self.dissolved = None

        if self.is_compressed:
            self.auto_dissolve = dissolve
            if not lazy:
                self.extracted_path = self.extract()

    @property
    def folder_path(self) -> str:
        """
        Gets the path to the folder.

        Returns:
            str: The path to the folder. If the folder is compressed, this will be the path to the extracted folder.
        """

        if self.is_compressed:
            return self.extracted_path
        else:
            return self.path

    @property
    def list(self) -> list[str]:
        """
        Gets a list of all files in the folder.

        Returns:
            list[str]: A list of all files in the folder, represented as relative paths.
        """

        return ["/".join(i) for i in dict2list(self.tree)]

    @property
    def tree(self) -> dict:
        """
        Gets a tree representation of the folder.

        Returns:
            dict: A nested dictionary representing the folder structure. Each key-value pair represents a node and its subtree.
        """

        tree = {}

        if self.is_compressed and not self.extracted:
            output = execute_python_code(
                f"patoolib.list_archive(\"{self.path}\")")
            file_list = list(filter(lambda x: os.path.basename(
                x) not in self.exclude_files, output.splitlines()))

            if self.is_compressed and self.auto_dissolve and len(tree.keys()) == 1 and list(tree.keys())[0] == os.path.splitext(os.path.basename(self.path))[0]:
                tree = tree[list(tree.keys())[0]]
        else:
            file_list = []
            for root, _, files in os.walk(self.folder_path):
                for file in files:
                    if file not in self.exclude_files:
                        file_list.append(os.path.relpath(
                            os.path.join(root, file), self.folder_path))

        for file_path in file_list:
            parts = file_path.strip('/').split('/')
            node = tree
            for i, part in enumerate(parts):
                if i == len(parts) - 1 and not file_path.endswith('/'):
                    node[part] = None
                else:
                    node = node.setdefault(part, {})

        return tree

    def extract(self) -> str:
        """
        Extracts the folder if it is compressed.

        Returns:
            str: The path to the extracted folder.
        """

        temp_folder = tempfile.mkdtemp(prefix="temp_folder_")
        patoolib.extract_archive(self.path, outdir=temp_folder)
        self.extracted = True
        self.extracted_path = temp_folder

        dirs = next(os.walk(temp_folder))[1]

        archive_name = os.path.splitext(os.path.basename(self.path))[0]

        if self.is_compressed and self.auto_dissolve and len(dirs) == 1 and dirs[0] == archive_name:
            self.extracted_path = os.path.join(temp_folder, archive_name)

        return self.extracted_path

    def get_file(self, file_path: str) -> BytesIO:
        """
        Gets a file from the folder.

        Args:
            file_path (str): The relative path to the file.

        Raises:
            Exception: If the folder is compressed and has not been extracted.
            FileNotFoundError: If the file does not exist.

        Returns:
            BytesIO: A binary stream of the file content.
        """

        if self.is_compressed and not self.extracted:
            raise Exception("The folder is not extracted.")
        full_path = os.path.join(self.folder_path, file_path)
        if os.path.exists(full_path):
            return open(full_path, 'rb')
        else:
            raise FileNotFoundError(f"The file '{file_path}' does not exist.")

    def close(self) -> None:
        """
        Closes the folder and cleans up any extracted files.
        """

        if self.is_compressed and self.extracted:
            try:
                shutil.rmtree(self.extracted_path)
            except:
                pass
