from setuptools import setup, find_packages

setup(
    name='ToDoListDevOps',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        # Dependências do projeto aqui, por exemplo:
        'unittest',
        'requests',
        'flask',
    ],
)
