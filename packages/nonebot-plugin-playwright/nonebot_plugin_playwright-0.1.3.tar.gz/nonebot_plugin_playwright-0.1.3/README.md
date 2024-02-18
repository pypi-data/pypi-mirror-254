<p align="center">
  <a href="https://nonebot.dev/"><img src="https://nonebot.dev/logo.png" width="200" height="200" alt="nonebot"></a>
</p>

<div align="center">

# NoneBot Plugin Playwright

![License](https://img.shields.io/github/license/eya46/nonebot_plugin_nezha)
![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![NoneBot](https://img.shields.io/badge/nonebot-2.0.1+-red.svg)
</div>

## 安装方式

```shell
pip install nonebot-plugin-playwright
pip install nonebot-plugin-playwright[localstore]

poetry add nonebot-plugin-playwright
poetry add nonebot-plugin-playwright[localstore]

# ...
```

## 配置项

```dotenv
# .env
# 指定的浏览器
playwright_browser
# 下载地址
playwright_download_host
# 是否headless
playwright_headless
# 本地浏览器地址 | None
playwright_executable_path
# 额外launch参数
playwright_extra_kwargs
# playwright关闭超时时间
playwright_shutdown_timeout
```

## 依赖

```toml
nonebot2 = "^2.0.1"
playwright = "^1.0.0"
nonebot-plugin-localstore = { version = ">=0.5.0", optional = true }
```