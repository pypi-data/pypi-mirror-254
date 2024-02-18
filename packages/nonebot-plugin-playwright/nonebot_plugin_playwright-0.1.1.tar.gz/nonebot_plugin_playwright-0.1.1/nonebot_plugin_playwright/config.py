from __future__ import annotations

from typing import Literal

from nonebot import get_driver
from pydantic import BaseModel, Extra, Field


class Config(BaseModel, extra=Extra.ignore):
    playwright_browser: Literal[
        "chromium", "chrome", "chrome-beta", "msedge", "msedge-beta", "msedge-dev", "firefox", "firefox-asan", "webkit"
    ] = Field(
        "chromium", description="指定 playwright 启动的浏览器"
    )
    playwright_download_host: str = Field(
        default="https://npmmirror.com/mirrors/playwright/",
        description="指定 playwright 下载源"
    )
    playwright_headless: bool = Field(default=True, description="指定 playwright 是否以无头模式启动")
    playwright_executable_path: str | None = Field(
        default=None, description="指定 playwright...launch 执行路径"
    )
    playwright_extra_kwargs: dict = Field(default_factory=dict, description="指定 playwright...launch 额外参数")
    playwright_shutdown_timeout: int = Field(default=5, description="指定 playwright 关闭超时时间")


config: Config = Config(**get_driver().config.dict())

__all__ = ["Config", "config"]
