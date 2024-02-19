from setuptools import setup, find_packages

with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='dblmapiv2',
    version='1.0.0',
    description='A updated version of DBLMAPI',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Mindset',
    author_email='gdnunuuwu@gmail.com',
    packages=find_packages(exclude=['my_docs']),
    install_requires=[
        # Add any dependencies your module may have
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)
