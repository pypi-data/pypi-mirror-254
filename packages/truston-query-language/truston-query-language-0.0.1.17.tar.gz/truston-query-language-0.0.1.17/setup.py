import setuptools
import os
import shutil



with open('./current_version.txt', 'r') as f:
    a,b,c,d = list(map(lambda x: int(x), f.readline().split(".")))
    order = f.readline()

if order == 'a++':
    a += 1
    b = 0
    c = 0
    d = 0
elif order == 'b++':
    c = 0
    d = 0
    b += 1
elif order == 'c++':
    d = 0
    c += 1
elif order == 'd++':
    d += 1

with open('./current_version.txt', 'w') as f:
    f.write(f"{a}.{b}.{c}.{d}\n{order}")

if os.path.exists('dist'):
    shutil.rmtree('dist')

setuptools.setup(
    name="truston-query-language",
    version=f"{a}.{b}.{c}.{d}",
    license='MIT',
    author="qmse",
    author_email="",
    description="qmse",
    long_description=open('README.md').read(),
    url="https://github.com",
    packages=setuptools.find_packages(),
    classifiers=[
        # 패키지에 대한 태그
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
)
