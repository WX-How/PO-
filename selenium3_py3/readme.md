## 项目目标

　> 对百度登录页面（https://passport.baidu.com/v2/?login）进行登录测试

## 功能实现
1. 自动运行用例
2. 自动生成测试报告
3. 自动断言与测试截图
4. 自动将最新测试报告发送到指定邮箱
5. PageObject + Unittest + 数据驱动

## 目录结构

common：基础共享包，通用定位元素方式封装
config：配置文件、配置信息存放的地方
util：存放第三方模块，发送邮件、读取报告等数据操作
page_obj：实现登录时，目标元素定位、自动发送信息等
business：执行page_obj包中相关py文件，逻辑操作等
case：内置程序main文件，真正case用例
report：测试报告 + 测试error截图
