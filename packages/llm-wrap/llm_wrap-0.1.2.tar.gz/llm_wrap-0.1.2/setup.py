from setuptools import setup, find_packages

setup(
    name='llm_wrap',
    version='0.1.2',
    author='Akihito Sudo',
    author_email="akihito.s.gm@gmail.com",
    url="https://github.com/sudodo/llm_wrap",
    packages=find_packages(),
    install_requires=[
        'openai==1.3.3',
    ],
    # Optional: if you have any package data
    package_data={
        # If any package contains *.txt or *.rst files, include them:
        'llm_wrap': ['*.txt', '*.rst'],
    },
    # And so on...
)
