import asyncio
import time 

get_time = time.time()


async def tes():
  print("Percobaan Pertama")
  print(f"Selesai at{time.time() - get_time} second\n")
  await asyncio.sleep(3) # Menunggu Selama 3 deitk
  print("Percobaan Kedua")
  print(f"Selesai at{time.time() - get_time} second\n")

async def get():
  await asyncio.gather(tes())

asyncio.run(get())