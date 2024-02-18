from setuptools import setup, find_packages


with open('README.md', 'r', encoding='utf-8') as fh:
    long_description = fh.read()


setup(
    name='JCompare',
    python_requires='>=3.10.0',
    description="""A folder compare utility.""",
    long_description_content_type='text/markdown',
    long_description=long_description,
    author="_Fervor_",
    url="https://github.com/UFervor/JCompare",
    version='0.0.1.1',
    packages=find_packages(),
    install_requires=[
        'tqdm',
        'patool',
        'dict_hash',
        'zstandard',
        'brotli',
    ],
)
