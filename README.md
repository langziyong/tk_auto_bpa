# 2021/3/29 初始版本
同科报平安自动化，仅供学习参考！！

# 说明
### 一、文件结构
1.`Auto_bpa_version.py` 主程序<br>
2.`aes.js` 密码在通过POST请求时会进行AES算法加密传输，该文件就是学校用的加密模块，里面已经添加相关函数可以直接调用。<br>
3.`requirements.txt`  python项目中必须包含一个 requirements.txt 文件，用于记录所有依赖包及其精确的版本号。<br>
以便新环境部署。使用 pip install -r requirements.txt 命令进行安装。<br>
4.`user_data.txt` 用户数据文档<br>
### 二、实现方式
读取`requirements.txt`配置文件，
