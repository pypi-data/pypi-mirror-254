from setuptools import setup, find_packages

setup(
    name='hebill_multiple_settings',
    version='1.0.0',
    packages=find_packages(),
    install_requires=[
        # 添加其他依赖项
    ],
    python_requires='>=3.11',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',

)
