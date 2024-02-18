from __future__ import annotations

import asyncio
import os
from time import time

from nonebot import get_driver, logger
from playwright.async_api import async_playwright, Playwright, Browser, Error

from .config import config

_driver = get_driver()

_PLAYWRIGHT: Playwright | None = None
_BROWSER: Browser | None = None


def get_playwright() -> Playwright:
    assert _PLAYWRIGHT is not None, "Playwright is not initialized"
    return _PLAYWRIGHT


def get_browser() -> Browser:
    assert _BROWSER is not None, "Browser is not initialized"
    return _BROWSER


async def browser_init(**kwargs):
    global _PLAYWRIGHT, _BROWSER
    if config.playwright_browser in ["chromium", "chrome", "chrome-beta", "msedge", "msedge-beta", "msedge-dev"]:
        _BROWSER = await _PLAYWRIGHT.chromium.launch(**kwargs)
    elif config.playwright_browser in ["firefox", "firefox-asan"]:
        _BROWSER = await _PLAYWRIGHT.firefox.launch(**kwargs)
    else:
        _BROWSER = await _PLAYWRIGHT.webkit.launch(**kwargs)


def playwright_install(browser: str, download_host: str = config.playwright_download_host):
    os.environ["PLAYWRIGHT_DOWNLOAD_HOST"] = download_host
    logger.opt(colors=True).info(f"<y>Installing {browser}...</y>")
    from playwright.__main__ import main as playwright_main
    import sys
    sys.argv = ["", "install", browser, "--with-deps"]
    try:
        playwright_main()
    except SystemExit as e:
        if e.code == 0:
            logger.info("playwright install success")
        else:
            logger.error("playwright install failed")


@_driver.on_startup
async def playwright_init():
    global _PLAYWRIGHT
    default_kwargs = {
        "channel": config.playwright_browser,
        "headless": config.playwright_headless,
        "executable_path": config.playwright_executable_path
    }
    default_kwargs.update(config.playwright_extra_kwargs)
    _PLAYWRIGHT = await async_playwright().start()
    try:
        await browser_init(**default_kwargs)
    except Error as e:
        if config.playwright_executable_path is None:
            playwright_install(config.playwright_browser)
            await browser_init(**default_kwargs)
        else:
            raise e
    if config.playwright_executable_path:
        logger.opt(colors=True).info(f"<y>Playwright executable path: {config.playwright_executable_path}</y>")
    logger.opt(colors=True).info(f"<y>Playwright started: {config.playwright_browser}</y>")


async def playwright_close():
    global _PLAYWRIGHT, _BROWSER
    logger.opt(colors=True).debug("<y>Closing browser...</y>")
    if _BROWSER:
        await _BROWSER.close()
    logger.opt(colors=True).debug("<y>Stopping playwright...</y>")
    if _PLAYWRIGHT:
        await _PLAYWRIGHT.stop()


async def bad():
    global _PLAYWRIGHT, _BROWSER
    start = time()

    while True:
        if _PLAYWRIGHT or _BROWSER:
            if time() - start > config.playwright_shutdown_timeout:
                raise TimeoutError("Playwright shutdown timeout")
            else:
                await asyncio.sleep(0.5)
        else:
            return


@_driver.on_shutdown
async def playwright_shutdown():
    try:
        await asyncio.gather(bad(), playwright_close())
        logger.opt(colors=True).info("<y>Playwright stopped</y>")
    except TimeoutError as e:
        logger.opt(colors=True).exception(e)
        logger.opt(colors=True).error("<y>out of time, force shutdown</y>")


__all__ = [
    "get_playwright", "get_browser", "browser_init", "playwright_install", "playwright_init", "playwright_close",
]
