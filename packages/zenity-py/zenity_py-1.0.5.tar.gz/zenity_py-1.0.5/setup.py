from setuptools import setup
from pathlib import Path

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name='zenity_py',
    long_description_content_type='text/markdown',
    long_description=long_description,
    keywords="zenity",
    version='1.0.5',
    packages=['zenity'],
    url="https://github.com/Marko2155/zenity_py",
    license='MIT',
    author='Marko Camandioti',
    author_email='camandiotimarko@gmail.com',
    description="A Python library for the CLI tool zenity.",
    project_urls={
        'Documentation': 'https://github.com/Marko2155/zenity_py#readme',
        'Source': 'https://github.com/Marko2155/zenity_py',
        'Tracker': 'https://github.com/Marko2155/zenity_py/issues',
    }
)
