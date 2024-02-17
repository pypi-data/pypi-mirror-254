import time

from ppocr import PPOCR

import sys

print(sys.platform)
if sys.platform == "win32":
    image = "D:/whl/Download/1.png"
else:
    image = "D:/whl/Download/1.png"

ocr = PPOCR()
print(ocr.predict([image]))
# print(ocr.predict("D:/whl/Download/1.png"))
# print(ocr.predict("D:/whl/Download/1.png"))
# for i in range(1, 60, 10):
#     start = time.perf_counter()
#     ocr.predict(["D:/whl/Download/1.png"] * i)
#     print(f"batch: {i} cost: {time.perf_counter() - start:.6f}s")
