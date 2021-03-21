import asyncio
from pyppeteer import launch


async def main():
    browser = await launch()

    page = await browser.newPage();

    await page.setViewport({"width": 1200, "height": 1000})

    urls = ['http://ec2-18-188-154-67.us-east-2.compute.amazonaws.com:8888/html%20pages/GW-Releases-0.html',
            'http://ec2-18-188-154-67.us-east-2.compute.amazonaws.com:8888/html%20pages/GW-Releases-1.html',
            'http://ec2-18-188-154-67.us-east-2.compute.amazonaws.com:8888/html%20pages/Release.html',
            'http://ec2-18-188-154-67.us-east-2.compute.amazonaws.com:8888/html%20pages/VMs-1.html',
            'http://ec2-18-188-154-67.us-east-2.compute.amazonaws.com:8888/html%20pages/VMs-2.html',
            'http://ec2-18-188-154-67.us-east-2.compute.amazonaws.com:8888/html%20pages/VMs-3.html',
            'http://ec2-18-188-154-67.us-east-2.compute.amazonaws.com:8888/html%20pages/VMs-4.html'
            ]

    for url in urls:
        await page.goto(url)
        pic = url[74:]
        await page.screenshot({'path': 'tmp/' + pic + '.png'})
    await browser.close()

asyncio.get_event_loop().run_until_complete(main())