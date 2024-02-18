from setuptools import setup, find_packages

setup(
    name='scriptedsketches',
    version='0.1.0',  # You can define your package's version number here
    packages=find_packages(),
    description='A package that allows you to create terminal art powered by GPT-4',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',  # If your README is in Markdown
    author='Jacob Lapkin',
    author_email='jacobglapkin@gmail.com',
    url='https://github.com/yourusername/scriptedsketches',  # Replace with your actual URL
    license='MIT',  # Or your chosen license
    install_requires=[
        'annotated-types>=0.6.0',
        'anyio>=4.2.0',
        'certifi>=2024.2.2',
        'distro>=1.9.0',
        'h11>=0.14.0',
        'httpcore>=1.0.2',
        'httpx>=0.26.0',
        'idna>=3.6',
        'openai>=1.10.0',
        'pydantic>=2.6.0',
        'pydantic_core>=2.16.1',
        'python-dotenv>=1.0.1',
        'tqdm>=4.66.1',
        'typing_extensions>=4.9.0',
        # 'pip' and 'setuptools' are not typically listed in install_requires
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',  # Specify the minimum required Python version
    include_package_data=True,
    keywords='terminal art gpt-4-turbo',
    entry_points={
        'console_scripts': [
            'scriptedsketches=scriptedsketches.cli:main'  # Assuming your CLI is in cli.py
        ]
    })