## FAQ

### What does each UI parameter mean?
 
- 双击参数标题会弹出该参数的帮助文档


### How to save/load presets?

- 点菜单: `File > Save Preset` 或者 `File > Load Preset`


### How to reset a parameter to default?

- 右击参数标题，选择 `Reset`
- 点击 UI 左下角的 Reset 将重置所有参数


### How to search for a parameter?

- 点击 UI 左上角的搜索框，输入关键词；之后右侧的参数列表会自动筛选出匹配的参数
- 输入关键字后所有导航页上的参数都会被筛选


### How to open User Guide？

- 点菜单: `Help > Open Help`；或者快捷键 `F1`


### How to debug a runtime issue?

- 点菜单: `Help > Open Diagnostics`
  - 系统文件管理器会自动打开最近一次执行的 session 文件夹


### How to report a problem?

- 前提条件：你要有内部 JIRA 和共享盘（Z:）的权限，参考文档 [access miHoYo JIRA](https://km.mihoyo.com/articleBase/4714/420081?sT=Accessing_JIRA#Accessing_JIRA)
- 点菜单: `Help > Report A Problem`, 等待下面的流程自动执行完:
  - 程序新建 JIRA 工单（issue）在: [miHoYo JIRA](https://yo-jira.mihoyo.com/secure/Dashboard.jspa)
  - 程序打包上传最近执行的 session 诊断信息到共享盘: Z:/Audio/Users/_bugreports
  - 程序发企业微信通知给研发组
- 之后:
  - 研发组会有人处理工单
  - 你会被设为工单的 Reporter
  - 随后工单更新会自动通知给你，前提是你已经 [注册了企业微信群机器人](https://km.mihoyo.com/articleBase/4713/487397) 到 Flow Launcher 
- 若上述都失败了，请联系技术音频组


### About the UI of Flow Tools, why do they all look alike?

- 所有 Flow 服务在 Tool模式下 的 UI 为代码自动生成，因此看起来都很像
- UI 采用类似的单页应用布局，即左侧导航栏 + 右侧参数列表 + 底部按钮栏
- 参数都有上下文帮助文档
- 所有参数可独立重置为默认值，也可全部重置
- `File` 菜单提供一些常用功能，比如保存/加载参数配置、退出程序等
- `Help` 菜单提供一些常用功能，比如打开帮助文档、报告问题等
