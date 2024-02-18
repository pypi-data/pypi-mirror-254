from setuptools import setup, find_packages
import os

print("Current Working Directory:", os.getcwd())
readme_file = "README.md"

if os.path.exists(readme_file):
    print(f"Found {readme_file}")
    with open(readme_file, "r") as fh:
        long_description = fh.read()
else:
    print(f"Did not find {readme_file}")
    long_description = ""

setup(
    name='BANOS',
    version='0.1.5',
    packages=['BANOS'],
    description='Set of metrics to assess behavior annotations of videos.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Benoit Girad and Giuseppe Chindemi',
    author_email='benoit.girard@unige.ch',
    url='https://github.com/BelloneLab/BANOS',
    install_requires=[
        'pandas>=1.0.5',
        'numpy>=1.18.5',
        'matplotlib>=3.2.2',
        'seaborn>=0.10.1'
    ],
    python_requires='>=3.7',
    project_urls={
        'Source': 'https://github.com/BelloneLab/BANOS',
        'Tracker': 'https://github.com/BelloneLab/BANOS/issues',
    },
    keywords='behavior analysis, annotation, video, metrics',
    license='MIT',
)
