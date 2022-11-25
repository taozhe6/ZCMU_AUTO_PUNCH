# 施工中
 # ZCMU自动健康打卡脚本
 > 浙江中医药大学自动健康打卡


 * 多个脚本和搜索引擎强力驱动
 * 由啥都不会，啥都想学，爱好刷机的医学牲缝合而成

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
 | TOKEN（选填） | 推送服务     | 详见 notify.py(pushplus,dingbot等) |
 |LOCATION      |定位              | 须按规范填写，后果自负|
 
 
 自用 ✔ [pushplus](http://www.pushplus.plus)，可以自行修改代码
  
 > 配置方法演示

 ![](./assets/create_secret.png)

 ![](./assets/new.png)

 ### 使用

 **程序将在每天 4:00(UTC 20:00) 自动运行，也可以在 `Aciton` 中手动触发运行。**

 **三个月左右 GitHub Action 会暂停自动运行，需要手动重新启动！**

 ![](./assets/run.png)

 ### 运行成功示例
 ![](./assets/success.png)

 ## 鸣谢
 [HDU-AutoPunch 杭州电子科技大学自动健康打卡脚本](https://github.com/YeQiuO/HDU_AUTO_PUNCH)

 [浙大城市学院健康打卡脚本](https://github.com/chansyawn/zucc-auto-check)

 [杭州电子科技大学自动健康打卡脚本](https://github.com/Eanya-Tonic/HDU-Health_checkin)

 [zkeq 自用API](https://github.com/zkeq/icodeq-api)
 
 [浙江理工大学自动健康申报（新版）](https://github.com/typenoob/zstu_report)

# TO DO
> 继续借鉴各位大佬的经验，用仅有的能力更新

* Docker环境补齐
* 简化代码，使用循环选择元素


# Coding with 💖
