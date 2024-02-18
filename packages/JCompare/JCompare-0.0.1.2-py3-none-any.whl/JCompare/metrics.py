import lzma
import brotli
import zstandard


class Similarity:
    """
    Base class for implementing similarity metrics.

    This class provides a structure for implementing different similarity metrics. 
    Subclasses should override the `cmp` method to provide their own similarity calculation logic.
    """

    def __init__(self) -> None:
        """
        Initializes a new instance of the Similarity class.
        """

        ...

    def cmp(self, file1: tuple[str, str], file2: tuple[str, str]) -> float:
        """
        Compares two files for similarity.

        Args:
            file1 (tuple[str, str]): A tuple containing the full path and the relative path of the first file.
            file2 (tuple[str, str]): A tuple containing the full path and the relative path of the second file.

        Raises:
            NotImplementedError: This method must be implemented in a subclass.

        Returns:
            float: The similarity score between the two files. The score is a float between 0 and 1, where 0 means completely dissimilar and 1 means identical.
        """

        fullpath1, relpath1 = file1
        fullpath2, relpath2 = file2

        raise NotImplementedError(
            "This method must be implemented in a subclass")


class CompressionSimilarity(Similarity):
    """
    A class used to compare the similarity between two files based on their compression ratio.

    This class inherits from the `Similarity` base class and overrides the `cmp` method to provide a similarity metric based on the compression ratio of the files. The compression ratio is calculated using a specified compression algorithm.
    """

    def __init__(self, algorithm: str, level: None | int = None, chuck_size: int = 64 * 1024) -> None:
        """
        Initializes a new instance of the CompressionSimilarity class.

        Args:
            algorithm (str): The compression algorithm to use. Supported algorithms are 'lzma', 'lzma2', 'zstd', and 'brotli'.
            level (int, optional): The compression level. If not provided, a default level will be used based on the algorithm.
            chunk_size (int, optional): The size of the chunks to read from the files. Defaults to 64 kilobytes.

        Raises:
            ValueError: If an unsupported algorithm is given.
        """

        super().__init__()
        self.algorithm = algorithm
        self.chunk_size = chuck_size
        if level is None:
            if algorithm == 'lzma':
                self.level = 6
            elif algorithm == 'lzma2':
                self.level = 6
            elif algorithm == 'zstd':
                self.level = 13
            elif algorithm == 'brotli':
                self.level = 8
            else:
                raise ValueError("Unsupported Algorithm")
        else:
            self.level = level

    def cmp(self, file1: tuple[str, str], file2: tuple[str, str]) -> float:
        """
        Compares two files for similarity based on the compression ratio.

        Args:
            file1 (tuple[str, str]): A tuple containing the full path and the relative path of the first file.
            file2 (tuple[str, str]): A tuple containing the full path and the relative path of the second file.

        Raises:
            ValueError: If an unsupported algorithm is given.

        Returns:
            float: The similarity score between the two files. The score is a float between 0 and 1, where 0 means completely dissimilar and 1 means identical.
        """

        fullpath1, relpath1 = file1
        fullpath2, relpath2 = file2

        def compress_files(filepaths, algorithm):
            compressor = None
            compressed_length = 0

            if algorithm == 'lzma':
                compressor = lzma.LZMACompressor(format=lzma.FORMAT_ALONE, filters=[
                                                 {"id": lzma.FILTER_LZMA1, "preset": self.level}])
            elif algorithm == 'lzma2':
                compressor = lzma.LZMACompressor(format=lzma.FORMAT_XZ, filters=[
                                                 {"id": lzma.FILTER_LZMA2, "preset": self.level}])
            elif algorithm == 'zstd':
                compressor = zstandard.ZstdCompressor(
                    level=self.level).compressobj()

            elif algorithm == 'brotli':
                compressor = brotli.Compressor(quality=self.level)
                for filepath in filepaths:
                    with open(filepath, 'rb') as f:
                        for chunk in iter(lambda: f.read(self.chunk_size), b''):
                            compressed_chunk = compressor.process(chunk)
                            compressed_length += len(compressed_chunk)
                compressed_length += len(compressor.finish())

                return compressed_length

            else:
                raise ValueError("Unsupported Algorithm")

            for filepath in filepaths:
                with open(filepath, 'rb') as f:
                    for chunk in iter(lambda: f.read(self.chunk_size), b''):
                        compressed_chunk = compressor.compress(chunk)
                        compressed_length += len(compressed_chunk)
            compressed_length += len(compressor.flush())

            return compressed_length

        c1_len = compress_files([fullpath1], self.algorithm)
        c2_len = compress_files([fullpath2], self.algorithm)
        cc_len = compress_files([fullpath1, fullpath2], self.algorithm)

        similarity = min(
            max(1 - (cc_len - min(c1_len, c2_len)) / (max(c1_len, c2_len)), 0), 1)
        return similarity
