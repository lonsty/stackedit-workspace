```sh
.
├── CEE_SC01  # 程序目录
│   ├── CEE-SC01_test.log  # 程序运行log
│   ├── FunctionTest.ipynb  # UI界面的ipython jupyter notebook文件
│   ├── L10_FT12.sh  # L10的测试项目
│   ├── L6_FT.sh  # L6的测试项目
│   ├── _version.py  # 程序版本
│   ├── config.ini  # 配置文件，可调整UI和一些测试行为
│   ├── config.py  # 读写配置文件的类
│   ├── function_test.py  # 功能测试主程序，包含命令函数，功能测试函数，UI界面更新函数，UI事件定义等
│   ├── logger.py  # 程序运行log格式定义
│   ├── mount_share_disk.py  # 连接SFC，进行数据交互的类
│   ├── my_serial.py  # 通过串口连接被测机，进行交互的类
│   ├── scripts  # 功能脚本
│   │   └── usb_test.sh  # 用于传送到DUT，测试USB功能的脚本
│   ├── ui_widgets.py  # UI基础组件
│   └── utils.py  # 工具函数
├── docs  # 安装、使用和版本更新说明文件
│   ├── ConfigurationSettingManual-v0.3.1-20190723.xlsx  # 配置文件设置手册
│   ├── DeploymentManual-v0.1.docx  # 软件部署手册
│   ├── FTCommandsManual-v0.2.xlsx  # 命令使用手册
│   ├── OperationGuide-v0.1.1.docx  # 操作手册
│   ├── ReleaseHistory-v0.3.2-20190724.docx  # 版本历史更新记录
│   └── release note-V0.2.xlsx  # 版本历史更新记录
└── ipywidgets-master  # 依赖包
	├── install.bat  # 依赖包安装脚本
	└── ...
```
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTEzNDYwNjE5ODNdfQ==
-->