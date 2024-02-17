from setuptools import setup, find_packages

# with open('readme.md', 'r', encoding='utf-8') as fh:
#     long_description = fh.read()
long_description = ""

setup(
    name='medlab',
    version='2024.02.03',
    author='yjiang',
    author_email='1900812907@qq.com',
    description='medical deep learning toolkit',
    long_description=long_description,
    long_description_content_type='text/markdown',
    license='MIT',
    url='https://gitee.com/Eason596/py-package-release-test',
    packages=find_packages(),
    # include_package_data=True,
    package_data={"medlab": ["testing/*", "configs/*/*/*/*/*", "requirements.txt"],},
    install_requires=[],
    python_requires='>=3.8',
    entry_points={
        'console_scripts': [
            'med-init-env = medlab:init_enviroment',
            'med-init-config = medlab:init_config',
            'med-train = medlab:train',
            'med-test = medlab:test',
            'med-predict = medlab:predict'
        ]
    }
)