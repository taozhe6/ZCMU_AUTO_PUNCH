 # ZCMU自动健康打卡脚本 ![](https://img.shields.io/badge/%E6%89%93%E5%8D%A1-ZCMU-brightgreen)![](https://img.shields.io/github/workflow/status/OopsSnap/ZCMU_AUTO_PUNCH/ZCMU%20Auto%20Punch?style=plastic)
~~低调使用，建议私有库运行~~
 > 浙江中医药大学自动健康打卡


 * 多个脚本和搜索引擎强力驱动
 * 由啥都不会，啥都想学，爱好刷机的医学牲缝合而成

 ## ❗❗❗请遵守学校防疫政策，出现异常请关闭脚本手动进行打卡❗❗❗
 ## ⚠⚠⚠   仅供学习交流使用，请于下载后24小时内删除   ⚠⚠⚠

 ## 使用方法

 ### 配置

 1. fork 该仓库

 2. 点击仓库中的 `Setting` 标签，选中 `Secrets`

 3. 选中 `New repository secret` 新建环境变量

 | Name          | Value            | Desc                                                       |
 | ------------- | ---------------- | ---------------------------------------------------------- |
 | USERNAME     | 学号             |   支持多用户登录，以','分隔 |
 | PASSWORD      | 统一身份认证密码 |   https://ias.zcmu.edu.cn/cas/login |
 | DD_BOT_TOKEN（选填） | 推送服务     | 钉钉推送(DD_BOT_TOKEN和DD_BOT_SECRET两者必需)官方文档 ,只需https://oapi.dingtalk.com/robot/send?access_token=XXX 等于=符号后面的XXX即可 |
 | DD_BOT_SECRET(选填)  |推送服务      | (DD_BOT_TOKEN和DD_BOT_SECRET两者必需) ,密钥，机器人安全设置页面，加签一栏下面显示的SEC开头的SECXXXXXXXXXX等字符 , 注:钉钉机器人安全设置只需勾选加签即可，其他选项不要勾选|
 |PUSH_PLUS_TOKEN(选填) ||','分隔|
 |LOCATION      |定位              | 须按规范填写，后果自负|
 
### 推送说明
 > 自用 ✔ dingdingbot，可以自行修改代码
 > 主用户使用DingDingBot，其余用户使用[pushplus](http://www.pushplus.plus)
 
 > 主用户监测所有用户打卡情况，其余用户各自分别推送各自的情况
  
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
 [浙江理工大学自动健康申报（新版）](https://github.com/typenoob/zstu_report)(大部分代码，打卡系统为杭州某多)
  
 [HDU-AutoPunch 杭州电子科技大学自动健康打卡脚本](https://github.com/YeQiuO/HDU_AUTO_PUNCH)(Github Action环境)

 [浙大城市学院健康打卡脚本](https://github.com/chansyawn/zucc-auto-check)

 [杭州电子科技大学自动健康打卡脚本](https://github.com/Eanya-Tonic/HDU-Health_checkin)

 [zkeq 自用API](https://github.com/zkeq/icodeq-api)
 


# TO DO
> 继续借鉴各位大佬的经验，用仅有的能力更新

* 了Docker环境补齐
* 简化代码，使用循环选择元素
* ✅多用户登录 
* ✅多用户推送


# Coding with ❤
