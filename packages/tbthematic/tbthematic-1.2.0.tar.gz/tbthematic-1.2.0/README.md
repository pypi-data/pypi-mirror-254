# OVERVIEW
本程序实现太保项目的基础长势数据产品、自身动态阈值分级长势产品


## 私服打包步骤
1、setup.py改版本号
2、python setup.py sdist bdist_wheel
3、twine upload -r gagopy dist/tbthematic-1.2.0* (1.1.0是版本号) 注意把.pypirc文件放到根目录中
   或者twine upload --repository pypi dist/tbthematic-1.0.0*

[distutils]
index-servers =
    pypi
    gagopy

[pypi]
repository=https://upload.pypi.org/legacy/
username=zhangzhilinzy
password=zzlling518518

[gagopy]
repository=http://maven.gagogroup.cn/repository/gagopy/
username=zhangzhilin
password= zzl@@123
