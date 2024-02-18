from __future__ import annotations

from nonebot.plugin import PluginMetadata

from .browser import get_playwright as get_playwright, get_browser as get_browser
from .tool import get_new_page as get_new_page, GetNewPage as GetNewPage, NewPage as NewPage
from .config import Config

__plugin_meta__ = PluginMetadata(
    name="Playwright",
    description="NoneBot Playwright插件",
    usage=(
        '声明依赖: `require("nonebot_plugin_playwright")\n'
        "使用: `from nonebot_plugin_playwright import ...`"
    ),
    type="library",
    homepage="https://github.com/eya46/nonebot_plugin_playwright",
    config=Config,
    supported_adapters=None,
)

__all__ = [
    "get_playwright",
    "get_browser",
    "get_new_page",
    "GetNewPage",
    "NewPage",
]
