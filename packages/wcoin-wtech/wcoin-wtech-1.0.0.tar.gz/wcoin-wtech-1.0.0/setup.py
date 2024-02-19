from setuptools import setup, find_packages

setup(
    name='wcoin-wrech',
    version='0.0.1',
    description='Hello There!',
    author='Wangtry',
    author_email='wangtry3417@gmail.com',
    url='https://github.com/wangtry3417/wcoin.git',
    packages=find_packages(),
    install_requires=[
        'cryptography',
        'requests',
        # 添加其他依赖项
    ],
    py_modules=['wcoin', 'wtech'],
)