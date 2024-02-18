import setuptools

with open("README.md ", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="samaker",
    version="1.2.2",
    author="wenbin Shi",
    author_email="shiwenbin1617@gmail.com",
    description="A TestCase maker package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),  # 自动发现所有包和子包
    classifiers=[  # 包的分类信息
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',  # Python版本要求
    include_package_data=True,  # 包含在MANIFEST.in中指定的数据文件
    entry_points={  # 添加 entry_points
        'console_scripts': [
            'samaker=samaker.cli:main',  # '命令=模块:函数'
        ],
    },
)