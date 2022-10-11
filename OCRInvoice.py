from paddleocr import PaddleOCR
import re
from PIL import Image

class OCRInvoice:
    def __init__(self):
        self.HorL='快速'

    def LowOrHigh(self):
        if self.HorL=='快速':
            self.ActOCR = PaddleOCR()
        else:
            self.ActOCR = PaddleOCR(rec_model_dir=r'E:\Python\Python38\Lib\site-packages\paddleocr\2.1\rec\ch',
                        cls_model_dir=r'E:\Python\Python38\Lib\site-packages\paddleocr\2.1\cls',
                        det_model_dir=r'E:\Python\Python38\Lib\site-packages\paddleocr\2.1\det\ch')
    def RunOCR(self,path):
        result = self.ActOCR.ocr(path)
        inform = []
        for line in result:
            inform.append(line[1][0])

        String2 = '【' + '】【'.join(inform) + '】'

        if '发' in String2 or '票' in String2:
            print('YEs')
        else:
            print('no')
            # image = cv2.imread(path)
            # print(image)
            # rotated = imutils.rotate(image, 180)
            # cv2.imwrite(path, rotated)
            im = Image.open(path)
            out = im.transpose(Image.ROTATE_180)
            out.save(path)
            result = self.ActOCR.ocr(path)
            inform = []
            for line in result:
                inform.append(line[1][0])

            String2 = '【' + '】【'.join(inform) + '】'



        #发票号码
        try:
            self.number = re.findall('【([0-9]{8})】', String2)[0]
        except:
            self.number=''

        invoice2 = re.sub('[a-zA-Z]', '', String2)

        #发票代码
        try:
            self.daima = re.findall('【([0-9]{10,12})】', invoice2)[0]
        except:
            self.daima = ''

        #发票日期
        try:
            patter = '([0-9]*[年|月|日].*?)】'
            dateo = re.findall(patter, invoice2)[0]
            print(dateo)
            year = ''.join(re.findall('(2019)|(2020)|(2021)|(2022)', dateo)[0])
            print(year)
            month = ''.join(re.findall('(01)|(02)|(03)|(04)|(05)|(06)|(07)|(08)|(09)|(10)|(11)|(12)', dateo)[1])
            date = dateo[-3:-1]
            self.ymd = year + month + date
        except:
            self.ymd =''

        #发票金额
        try:
            amounts = re.findall('([0-9]*?\..*?)】', invoice2)
            amounts = [float(i) for i in amounts]
            amounts.sort()
            self.amount = amounts[-2]
            
#             """建议修改部分"""
#             amounts = re.findall('([0-9]*?\..[0-9]*?)】', invoice2)
#             amounts = [float(i) for i in amounts]
#             amounts = list(set(amounts))
#             amounts.sort()
#             # 发票总金额
#             self.totalAmount = amountslst[-1]
#             # 无税金额
#             self.amount = amountslst[-2]
#             # 发票税额
#             self.totalTax = amountslst[-3]
        except:
            self.amount = ''

        self.OneInv = [path,self.daima, self.number, self.ymd, self.amount]
#             """同步修改部分"""
#         self.OneInv = [path,self.daima, self.number, self.ymd, self.totalAmount, self.amount, self.totalTax]
        #print(self.OneInv)
        return self.OneInv

if __name__ == '__main__':
    ocrAct = OCRInvoice()
    Invoicepath = 'INV/Invoice (2).JPG'
    ocrAct.LowOrHigh()
    ocrAct.HorL='快速'
    ocrAct.RunOCR(Invoicepath)
