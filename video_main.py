import asyncio
from playwright.async_api import async_playwright

js = """
    var v = document.querySelector(".jwvideo > video:nth-child(1)");
    v.currentTime=v.duration;
    """

url="http://180.76.151.202"

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False,channel="msedge")
        context = await browser.new_context()
        page = await context.new_page()
        await page.goto(url)
        input("请进入**章节导航**后，按回车键继续")
        await page.wait_for_selector('.lecture-action')
        elements = await page.locator('.lecture-action').all()
        for element in elements:
            html=await element.inner_html()
            text=await element.inner_text()
            if "icon-play-done" in html:
                print('\n'+"已完成"+'\n'+text)
            else:
                print('\n'+"未完成"+'\n'+text)
                if "edit" in html:
                    print("跳过非视频")
                else:
                    print("视频未看完，即将开始播放")
                    await element.click()
                    await page.wait_for_selector('.jwvideo > video:nth-child(1)')
                    await page.evaluate(js)
                    await asyncio.sleep(1)
                    print("视频已看完")
                    await page.go_back()
        await page.reload()
        input("程序执行完毕，按回车键退出")

print("请等待浏览器启动")
asyncio.run(main())