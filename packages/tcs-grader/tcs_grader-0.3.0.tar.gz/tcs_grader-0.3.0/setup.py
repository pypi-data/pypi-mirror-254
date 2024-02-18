from setuptools import setup, find_packages

setup(
    name='tcs_grader',
    version='0.3.0',
    author='Emani Stanton',
    author_email='emani04@mit.edu',
    description='A short description of your package',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)