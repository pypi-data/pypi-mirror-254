from setuptools import setup, find_packages
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = fh.read()
setup(
    name = 'girow',
    version = '0.0.1',
    author = 'Deepesh Kalura',
    author_email = 'deepeshkalurs@gmail.com',
    license = 'MIT License',
    description = 'Girow is a Python-based CLI tool that helps create a workflow so that user can create better functions. It provides functionalities to create a new learning branch, install Jupyter Notebook, create a new Jupyter Notebook file, and merge changes from the learning branch back to the main branch.',
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = 'https://github.com/DeepeshKalura/girow',
    py_modules = ['app'],
    packages = find_packages(),
    install_requires = [requirements],
    python_requires='>=3.7',
    classifiers=[
        "Programming Language :: Python :: 3.11",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
    ],
    entry_points = '''
        [console_scripts]
        girow=app.girow:app
    '''
)



