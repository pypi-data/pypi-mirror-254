from setuptools import setup, find_packages

setup(
    name="ara-tools",
    version="0.1.4.18",
    packages=find_packages(),
    include_package_data=True,  # Add this line
    entry_points={
        "console_scripts": [
            "ara = ara_tools.__main__:cli",
        ],
    },
    install_requires=[
        'langchain',
        'langchain-community',
        'openai',
        # Add your package dependencies here
    ],
)
