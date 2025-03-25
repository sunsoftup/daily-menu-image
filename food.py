import asyncio
from playwright.async_api import async_playwright
import requests
from pathlib import Path

async def run():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        await page.goto("http://pf.kakao.com/_MnwHxj")
        await page.wait_for_selector(".item_profile_head img", timeout=5000)

        img = await page.query_selector(".item_profile_head img")
        img_url = await img.get_attribute("src")

        if img_url:
            print(f"✅ 이미지 URL: {img_url}")
            response = requests.get(img_url)
            Path("images").mkdir(exist_ok=True)
            with open("images/menu.jpg", "wb") as f:
                f.write(response.content)
        else:
            print("❌ 이미지 URL을 찾지 못했습니다.")

        await browser.close()

asyncio.run(run())
