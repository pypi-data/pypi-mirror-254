from setuptools import setup, find_packages

setup(
    name="NarrativeForge",
    version="0.1.4",
    description='A package for adding text and ai generated voice to videos.',
    author='supun nadeera',
    readme = "README.md",
    url='https://github.com/supunnadeera/NarrativeForge',
    packages=find_packages(),
    install_requires=[
        "numpy",
        "moviepy",
        "openai",
        "click",
    ],
    entry_points={
        "console_scripts": [
            "NarrativeForge=NarrativeForge:main",
        ],
    },
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3.10',
    ],
    project_urls={ 
        'Source': 'https://github.com/supunnadeera/NarrativeForge',
    },
)