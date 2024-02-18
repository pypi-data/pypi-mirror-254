from setuptools import setup

setup(
    name='WinDirectInput',
    version='1.0.4',  # Update the version number as needed
    author='AbdulRahim Khan',
    author_email='abdulrahimpds@gmail.com',
    description='A Windows-specific package for simulating keyboard and mouse inputs',
    long_description=open('README.md', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    py_modules=['directinput'],
    install_requires=[
        'opencv-python',
        'numpy',
        'mss',
        'pyscreeze',
        'pillow',
        'pyperclip'
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: Microsoft :: Windows',
    ],
)
