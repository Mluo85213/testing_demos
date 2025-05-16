# SQL 数据驱动接口测试项目

本项目为一个完整的接口测试 Demo，结合 Flask mock 接口、pytest 测试框架、sqlite 数据驱动、日志记录与 HTML 报告输出，适用于测试开发/自动化测试实习岗的简历项目展示。

---

## 📁 项目结构说明

```
sql_driven_demo/
├── data/                # 存放 sqlite 数据库文件 test.db
├── logs/                # 自动生成测试执行日志
├── mock_server/         # Flask mock 接口服务代码
│   └── app.py
├── report/              # pytest-html 报告输出目录
├── testcases/           # 接口测试用例目录
│   └── test_user_api.py
├── utils/               # 通用工具模块（数据库操作、日志配置）
│   ├── db_utils.py
│   └── logger.py
├── pytest.ini           # pytest 配置文件
└── README.md            # 项目说明文档（当前文件）
```

---

## 🚀 使用方式

### ✅ 1. 安装依赖

```bash
pip install pytest pytest-html flask requests
```

### ✅ 2. 启动 mock 接口服务

```bash
cd mock_server
python app.py
```

启动成功后监听地址为：`http://127.0.0.1:5000/user_info?id=1`

### ✅ 3. 执行测试 + 生成报告

```bash
cd sql_driven_demo
pytest testcases/ --html=report/report.html
```

---

## 🔍 功能模块说明

- **接口调用**：使用 `requests.get()` 请求 mock 接口
- **数据库断言**：调用 `utils/db_utils.py` 对 sqlite 中用户信息进行校验
- **日志记录**：通过 `utils/logger.py` 记录测试执行过程
- **HTML 报告**：使用 `pytest-html` 生成结构化测试报告

---

## 📌 后续拓展建议

- 增加接口链路模拟（注册 → 登录 → 查询）
- 用 Postman 导出接口调试文档（作为测试依据）
- 项目上传 GitHub，配合 GitHub Actions 实现 CI/CD
- 提供命令行参数支持（如 pytest.ini 中参数化配置）

---

## 🖼️ 示例截图（可选）

建议附加一张 `report/report.html` 的展示截图，放在项目仓库主页，用于简历展示。

---

项目作者：@momo ｜ 更新时间：2025.04.19