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
读取`requirements.txt`配置文件，使用for循环以列表方式逐个读取每个用户的数据，使用`aes.js`加密模块对明文密码进行加密并且重新赋值。POST请求登录提交数据而后发邮件通知。
### 三、注意事项
1.实测仅提交表单并不能完成当日报平安统计。所以将所有post请求都加上了。<br>
2.关于发件邮箱账号密码，源文档里面是我的小号，建议改成自己的,采取SMTP协议。<br>
3.`user_data.txt` 用户数据文档必须严格安装规范填写一共13个参数，编号开始，end结束，空格隔开。<br>
例如：<br>
    `1 180107xxxx password 李xx 必须是详细准确的系名称 178xxxxxxxx 山东省菏泽市曹县 1 3 xx区  耕文路419号 154xxxxxxx@qq.com end`<br>
分别对应<br>
    `序号,学号,密码,姓名,所在系,手机号,地址（到区县）,体温参数1（取值范围1-3）,体温参数2（取值范围1-3）,地址（县）,目前所在详细位置,通知邮箱,固定结束参数“end”`<br>
