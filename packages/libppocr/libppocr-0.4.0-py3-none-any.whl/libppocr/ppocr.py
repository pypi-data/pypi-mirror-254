import json
from ctypes import *
import sys

import numpy as np
from typing import Union, Any
from pathlib import Path


class OCRError(Exception):
    pass


class PPOCR:
    ppocr = CDLL(str(Path(__file__).parent / ('libppocr.dll' if sys.platform == 'win32' else 'libppocr.so')))
    ppocr.init.restype = c_void_p
    ppocr.OCR.restype = c_char_p
    ppocr.OCR_ARRAY.restype = c_char_p
    ppocr.OCR_BYTES.restype = c_char_p

    # res_template = re.compile(r'^det boxes: (\[.*])rec text: (.*?) rec score:(.*)$')

    def __init__(self, cpp_only=False):
        self.model = c_void_p(self.ppocr.init())
        if not cpp_only:
            try:
                from PIL import Image
                self._pil = True
            except ImportError:
                self._pil = False
            try:
                import cv2
                self._cv2 = True
            except ImportError:
                self._cv2 = False
            try:
                import requests
                self.requests = True

            except ImportError:
                self.requests = False

        else:
            self._pil = False
            self._cv2 = False

    def predict(self, input_: Union[np.ndarray, list[str], str, bytes, Any]):
        try:
            if self._pil:
                from PIL import Image
                if isinstance(input_, Image.Image):
                    return self._deal_res(self._ocr_pil(input_))

            if isinstance(input_, str):
                return self._deal_res(self._ocr_str(input_))
            elif isinstance(input_, list):
                return self._deal_res(self._ocr_batch_str(input_))
            elif isinstance(input_, bytes):
                pass
            elif isinstance(input_, np.ndarray):
                return self._deal_res(self._ocr_array(input_))
            else:
                raise TypeError(
                    f"Input type error!Expects [PIL.Image | np.ndarray | List[str] | str | byte ] and receive {type(input_)}")
        except OSError as e:
            raise OCRError(*e.args) from e

    def _ocr_batch_str(self, images: list[str]):
        json_imgs = json.dumps(images, ensure_ascii=False).encode()
        res = self.ppocr.OCR(self.model,
                             json_imgs).decode('utf8')
        return res

    def _ocr_str(self, image: str):
        if image.startswith("http") and self.requests:
            import requests
            response = requests.get(image)
            if response.status_code != 200:
                raise ValueError("Cant not fetch image from url")
            res = self._ocr_bytes(response.content)
            return res

        if self._cv2:
            import cv2
            img = cv2.imread(image)
            res = self._ocr_array(img)
            return res
        elif self._pil:
            from PIL import Image
            image = Image.open(image)
            return self._ocr_pil(image)
        else:
            return self._ocr_batch_str([image])

    def _ocr_array(self, image: np.ndarray):
        row, col, ch = image.shape
        img_c = np.ctypeslib.as_ctypes(image)
        res = self.ppocr.OCR_ARRAY(self.model, img_c, row, col, ch).decode('utf8')
        return res

    def _ocr_bytes(self, image: bytes):
        size: int = len(image)
        image: c_void_p = cast(image, c_void_p)
        res = self.ppocr.OCR_BYTES(self.model, image, size).decode('utf8')
        return res
        # raise ValueError("Bytes not support!")

    def _ocr_pil(self, image):

        ch = len(image.getbands())
        if ch > 3:
            ch = 3
            image = image.convert('RGB')
        row, col, ch = image.height, image.width, ch
        array_type = np.array(image).copy()
        res = self.ppocr.OCR_ARRAY(self.model, np.ctypeslib.as_ctypes(array_type), row, col,
                                   ch).decode('utf8')
        return res

    @staticmethod
    def _deal_res(res: str):
        return json.loads(res)


if __name__ == '__main__':
    ocr = PPOCR()
    from PIL import Image

    print(ocr.predict("https://member.neea.cn/login/createCode"))

    # image = Image.open("D:/whl/Download/1.png")
    # print(ocr.predict(image))
