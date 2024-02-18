from setuptools import setup, find_packages

setup(
    name="hubstudio",
    version="0.2",
    packages=find_packages(),
    author_email="2831926323@qq.com",
    author="Alex",
    install_requires=[
        "aiohttp",
        "psutil",
        "inflection"
    ],
    # 其他元数据
)
