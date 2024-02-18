from __future__ import annotations

from contextlib import asynccontextmanager
from pathlib import Path
from typing import AsyncIterator, AsyncGenerator

from nonebot import require
from nonebot.params import Depends
from playwright.async_api import Page
from typing_extensions import Annotated

from .browser import get_browser

_if_localstore = False

try:
    require("nonebot_plugin_localstore")
    _if_localstore = True
    from nonebot_plugin_localstore import get_data_dir

    plugin_data_dir: Path = get_data_dir("nonebot_plugin_playwright")

except RuntimeError:
    pass


@asynccontextmanager
async def get_new_page(
        *, name: str | None = None, use_store: bool = True, save_store: bool = True, **kwargs
) -> AsyncGenerator[Page, None]:
    browser = get_browser()
    if _if_localstore and use_store and kwargs.get("storage_state") is None and name is not None:
        if (_p := plugin_data_dir / f"{name}.json").exists():
            kwargs["storage_state"] = _p
    async with await browser.new_context(**kwargs) as context:
        yield await context.new_page()
        if _if_localstore and save_store:
            if kwargs.get("storage_state") is not None:
                await context.storage_state(path=plugin_data_dir / f"{kwargs.get('storage_state')}.json")
            elif name is not None:
                await context.storage_state(path=plugin_data_dir / f"{name}.json")


def GetNewPage(**kwargs):
    """
    使用方式:
    page: Page = GetNewPage(...)
    page: Annotated[Page, GetNewPage(...)]
    """

    async def _():
        async with get_new_page(**kwargs) as page:
            yield page

    return Depends(_)


def NewPage(**kwargs):
    """
    使用方式:
    page: NewPage(...)
    """

    async def _():
        async with get_new_page(**kwargs) as page:
            yield page

    return Annotated[Page, Depends(_)]
