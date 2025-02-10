#!/bin/python3

import asyncio
import aiohttp
import time

async def download_url(sem, session, url):
	async with sem:
		async with session.get(url) as response:
			content = await response.text()
			print(f"Downloaded URL: {url}\n{len(content)} bytes")

async def main():
	urls = ["https://en.wikipedia.org/wiki/C_(programming_language)", 
			"https://docs.aiohttp.org/en/stable/index.html", 
			"https://docs.python.org/3/library/asyncio.html",
			"https://www.youtube.com/", 
			"https://www.goodreads.com/",
			"https://www.britannica.com/", 
			"https://www.djangoproject.com/",
			"https://www.thebeatles.com/",
			"https://en.wikipedia.org/wiki/C_(programming_language)",
			"https://docs.aiohttp.org/en/stable/index.html", 
			"https://docs.python.org/3/library/asyncio.html",
			"https://en.wikipedia.org/wiki/C_(programming_language)", 
			"https://docs.aiohttp.org/en/stable/index.html", 
			"https://docs.python.org/3/library/asyncio.html",
			"https://en.wikipedia.org/wiki/C_(programming_language)",
			"https://docs.aiohttp.org/en/stable/index.html"]
	concurrency = [1, 2, 4, 8, 16]
	for i in concurrency:
		sem = asyncio.Semaphore(i)
		start = time.perf_counter()
		async with aiohttp.ClientSession() as session:
			await asyncio.gather(*(download_url(sem, session, url) for url in urls))
		end = time.perf_counter()
		print(f"Execução assíncrona com {i} tasks levou {end - start:.6f} segundos.")

if __name__ == "__main__":
	asyncio.run(main())