from setuptools import setup, find_packages

requirements = [
        'flask==2.3.2',  # 依赖项列表
        'loguru==0.7.0',
    ]

setup(
    name='flock-sdk',  # 包名称
    version='0.0.3',  # 包版本
    author='FLock.io',  # 作者名称
    author_email='info@flock.io',  # 作者邮箱
    description='An SDK for building applications on top of FLock V1',  # 简短描述
    long_description=open('README.md').read(),  # 长描述，通常是README
    long_description_content_type='text/markdown',  # 长描述的内容类型，例如：text/markdown 或 text/plain
    url='https://github.com/FLock-io/v1-sdk',  # 项目主页链接
    packages=find_packages(),  # 自动查找包含 '__init__.py' 的目录
    keywords=[
        "blockchain",
        "federated learning",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",  # 支持的 Python 版本
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',  # 许可证
        'Operating System :: OS Independent',  # 操作系统
    ],
    install_requires=requirements,
    python_requires='>=3.7',  # Python 版本要求
)
