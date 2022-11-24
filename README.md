# 施工中
 # ZCMU自动健康打卡脚本

 ## ❗❗❗请遵守学校防疫政策，出现异常请关闭脚本手动进行打卡❗❗❗

 ## 使用方法

 ### 配置

 1. fork 该仓库

 2. 点击仓库中的 `Setting` 标签，选中 `Secrets`

 3. 选中 `New repository secret` 新建环境变量

 | Name          | Value            | Desc                                                       |
 | ------------- | ---------------- | ---------------------------------------------------------- |
 | USERNAME     | 学号             |    |
 | PASSWORD      | 统一身份认证密码 |    |
 | TOKEN（选填） | 微信推送服务     | 详见 notify.py |

 > 配置方法演示

 ![](./assets/create_secret.png)

 ![](./assets/new.png)

 ### 使用

 **程序将在每天 4:00(GMT 20:00) 自动运行，也可以在 `Aciton` 中手动触发运行。**

 **三个月左右 GitHub Action 会暂停自动运行，需要手动重新启动！**

 ![](./assets/run.png)

 ### 运行成功示例
 ![](./assets/success.png)

 ## 鸣谢

 [浙大城市学院健康打卡脚本](https://github.com/chansyawn/zucc-auto-check)

 [杭州电子科技大学自动健康打卡脚本](https://github.com/Eanya-Tonic/HDU-Health_checkin)

 [zkeq 自用API](https://github.com/zkeq/icodeq-api)
 
 [浙江理工大学自动健康申报（新版）](https://github.com/typenoob/zstu_report)

