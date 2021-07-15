# InvoiceOCRer
A tiny app for OCR of Chinese VAT invoice, and to pick up the key information to Excel.

**HOW TO START**

1. Install the necessary module by pip install.They are： paddlepaddle, paddleocr, re, PIL, pandas, PyQt5, fitz.

2. Go to the PaddleOCR website https://github.com/PaddlePaddle/PaddleOCR, and donwload the inference model under the header **'Detection model'**,**'Direction classifier'**,**'Recognition model'**, subject to the **'Chinese and English general OCR model (143.4M)'**. Then you may get 3 tar files. Unzip them and place them in the folder named '**cls**','**det**','**rec**',which are usually in the following path:'your python parth'\Lib\site-packages\paddleocr\2.1\

3.Open  **OCRInvoice.py** by whatever application. Find the following code:

self.ActOCR = PaddleOCR(rec_model_dir=r'E:\Python\Python38\Lib\site-packages\paddleocr\2.1\rec\ch',
                        cls_model_dir=r'E:\Python\Python38\Lib\site-packages\paddleocr\2.1\cls',
                        det_model_dir=r'E:\Python\Python38\Lib\site-packages\paddleocr\2.1\det\ch')
                        
Replace the path with the actual path in the setp 2.

4. Run **OCRWindow.py** to get what you want.
