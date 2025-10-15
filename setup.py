from setuptools import setup, find_packages

def get_version():
    with open("requirements.txt") as f:
        return f.read().strip()

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='feedback_notebook',
    version=get_version(),
    author='Anton Sergeev',
    author_email='kavery@mail.ru',
    description='З/П > 500 k. Блокнот для отслеживания откликов',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/Anton-Sergeev-EA/feedback_notebook',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    install_requires=[
        'openpyxl',
        'tkinter',
    ],
    entry_points={
        'console_scripts': [
            'job-tracker=main_module:main',
        ],
    },
    include_package_data=True,
)
