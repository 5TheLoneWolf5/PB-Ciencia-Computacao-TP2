#!/bin/python3

from PIL import Image, ImageFilter
import os
import requests
import asyncio
import time

def _process_image(path, dir):
	img = Image.open(path)
	img = img.filter(ImageFilter.BLUR)
	img.save(os.path.join(dir, os.path.basename(path)))

async def process_image(sem, path, dir):
	async with sem:
		await asyncio.to_thread(_process_image, path, dir)

async def main():
	input_dir = "input_images"
	output_dir = "output_images"
	os.makedirs(input_dir, exist_ok=True)
	os.makedirs(output_dir, exist_ok=True)

	img_1 = requests.get("https://cdn.pixabay.com/photo/2024/11/11/17/39/dog-9190504_1280.jpg").content
	with open(f"{input_dir}/img_1.jpg", "wb") as handler:
		handler.write(img_1)

	img_2 = requests.get("https://cdn.pixabay.com/photo/2023/05/22/18/11/guitar-8011240_1280.jpg").content
	with open(f"{input_dir}/img_2.jpg", "wb") as handler:
		handler.write(img_2)

	img_3 = requests.get("https://cdn.pixabay.com/photo/2016/07/25/01/02/dice-1539658_1280.jpg").content
	with open(f"{input_dir}/img_3.jpg", "wb") as handler:
		handler.write(img_3)

	images = [os.path.join(input_dir, img) for img in os.listdir(input_dir) if img.endswith(".jpg")]
	concurrency = [1, 2, 4, 8, 16]
	for i in concurrency:
		sem = asyncio.Semaphore(i)
		start = time.perf_counter()
		await asyncio.gather(*(process_image(sem, img, output_dir) for img in images))
		end = time.perf_counter()
		print(f"Execução assíncrona com {i} tasks levou {end - start:.6f} segundos.")

if __name__ == "__main__":
	asyncio.run(main())