# Geometry

geometry-python-packaging-tomge 是一个几何简易工具包。该项目是一个教学性质的软件包，旨在全面展示如何构建 Python 软件包的过程。

以下是构建流程的五个步骤：

##### 第一步：模块化

构建软件包的文件结构,并编写 pyproject.toml和 README.md 文件。

- UPLOAD_TO_PYPI/
  - -- src/
    - -- geometry-python-packaging-tomge/
      - -- draw/
      - -- plane/
      - -- solid/
  - -- tests/
  - -- pyproject.toml
  - -- README.md

##### 第二步：创建本地虚拟环境

创建虚拟环境,确保开发环境独立无干扰。env为虚拟环境名,可任意修改。
  
1.创建:

```sh
% python3 -m venv env
```

2.激活:

```sh
 % source env/bin/activate
```

##### 第三步：本地安装软件包

在本地安装软件包,并测试软件包的功能，确保一切运作正常。

```sh
% pip install .
```

##### 第四步：编译和上传软件包至 Test PyPI

1. 包编译:

```sh
% python3 -m pip install --upgrade pip
% python3 -m pip install --upgrade build
% python3 -m build
```

2. 上传包:

```sh
% python3 -m pip install --upgrade twine
% python3 -m twine upload --repository testpypi dist/*
```

3. 下载安装包:

```sh
% python3 -m pip install --index-url https://test.pypi.org/simple/ --no-deps geometry-python-packaging-tomge (此处填写以自己的包名)
```

如需通过pip进行本地安装，建议添加‘--no-deps’参数以避免安装依赖项。
*--no-deps参数，以避免安装依赖项时报错, Test Pypi主要目的是检查上传信息是否正确,所以其下载时并不包含包编译依赖项的内容.*

##### 第五步：软件包上传至 PyPI

将软件包正式发布到PyPI, 并进行下载安装和测试，以验证功能的完整性。

1. 上传包:

```sh
% twine upload dist/*
```
  
2. 下载安装包:

```sh
% pip install geometry-python-packaging-tomge
```

## 参考资料

- [Packaging Python Projects](https://packaging.python.org/en/latest/tutorials/packaging-projects/)
- [Writing your pyproject.toml](https://packaging.python.org/en/latest/guides/writing-pyproject-toml/#writing-pyproject-toml)
- [Setuptools](https://setuptools.pypa.io/en/latest/userguide/quickstart.html)
- [Modules](https://docs.python.org/3/tutorial/modules.html#packages)
- [MIT license](https://opensource.org/license/mit/)

## 版本说明

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags).

## 作者

- **Tom Ge** - *Data scientist* - [github profile](https://github.com/tomgtqq)

## License

This project is licensed under the MIT License
