from setuptools import setup, find_packages

setup(
    name="netforge",
    version="1.0.0",
    description="NetForge Enterprise Network Simulation & Proxy Framework",
    author="Bhanu",
    packages=find_packages(),
    python_requires=">=3.9",
    install_requires=[
        "urllib3>=1.26.0",
        "requests>=2.28.0",
    ],
    entry_points={
        "console_scripts": [
            "netforge=main:main",
        ],
    },
)
