from setuptools import setup, find_packages

setup(
    name='DjPyForms',
    version='0.1.2',
    author='Charles GBOYOU',
    author_email='gboyoucharles22@gmail.com',
    description='A tool for automatic Django form generation',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/Charl12-gb/pyform.git',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Django>=3.2', 
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Framework :: Django',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.7',
    entry_points={
        'console_scripts': [
            'DjPyForms=DjPyForms.management.commands.createform:main',
        ],
    },
)
