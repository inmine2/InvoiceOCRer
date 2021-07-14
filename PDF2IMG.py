import sys, fitz
from os import path,makedirs
import datetime

class pdf2img:
    def pyMuPDF_fitz(self,pdfPath):
        self.imagePath = ''
        startTime_pdf2img = datetime.datetime.now()  # 开始时间
        self.imagePath = pdfPath.split('/')[-1]
        self.imagePath = 'IMG/' + self.imagePath[:-4]
        pdfDoc = fitz.open(pdfPath)
        for pg in range(pdfDoc.pageCount):
            page = pdfDoc[pg]
            rotate = int(0)
            # 每个尺寸的缩放系数为1.3，这将为我们生成分辨率提高2.6的图像。
            # 此处若是不做设置，默认图片大小为：792X612, dpi=72
            zoom_x = 2  # (1.33333333-->1056x816)   (2-->1584x1224)
            zoom_y = 2
            mat = fitz.Matrix(zoom_x, zoom_y).preRotate(rotate)
            pix = page.getPixmap(matrix=mat, alpha=False)

            if not path.exists(self.imagePath):  # 判断存放图片的文件夹是否存在
                makedirs(self.imagePath )  # 若图片文件夹不存在就创建

            pix.writePNG(self.imagePath +'/' + 'images_%s.png' % pg)  # 将图片写入指定的文件夹内

        endTime_pdf2img = datetime.datetime.now()  # 结束时间
        #print('pdf2img时间=', (endTime_pdf2img - startTime_pdf2img).seconds)


if __name__ == "__main__":
    pdfPath = 'INV/InvoiceColored.PDF'
    Topdf = pdf2img()
    Topdf.pyMuPDF_fitz(pdfPath)
    print(Topdf.imagePath)

