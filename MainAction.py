from OCRInvoice import OCRInvoice
from PDF2IMG import pdf2img
from pandas import DataFrame
from os import listdir

def OCR_PDF(PDFPath,flag):
    InvoiceInfo = DataFrame(columns=['文件地址','发票代码','发票号码','日期','金额（不含税）'])
    Topdf = pdf2img()
    Topdf.pyMuPDF_fitz(PDFPath)
    print(Topdf.imagePath)
    ocrAct = OCRInvoice()
    ocrAct.HorL = flag
    ocrAct.LowOrHigh()
    itemNo = 1
    for filename in listdir(Topdf.imagePath):
        print(filename)
        Invoicepath = Topdf.imagePath+'/'+filename
        print(Invoicepath)
        InvoiceInfo.loc[itemNo]=ocrAct.RunOCR(Invoicepath)
        itemNo+=1
    print(InvoiceInfo)
    InvoiceInfo.to_excel(Topdf.imagePath.split('/')[-1]+'.xlsx')

def OCR_IMGS(IMGPath,flag):
    InvoiceInfo = DataFrame(columns=['文件地址','发票代码', '发票号码', '日期', '金额（不含税）'])
    ocrAct = OCRInvoice()
    ocrAct.HorL = flag
    ocrAct.LowOrHigh()
    itemNo = 1
    for filename in listdir(IMGPath):
        Invoicepath = IMGPath + '/' + filename
        print(Invoicepath)
        InvoiceInfo.loc[itemNo] = ocrAct.RunOCR(Invoicepath)
        itemNo += 1
    print(InvoiceInfo)
    InvoiceInfo.to_excel(IMGPath.split('/')[-1] + '.xlsx')

if __name__ == '__main__':

    PDFPath = 'INV\\InvoiceColored.PDF'
    IMGPath = 'E:\Python\Projects\OCR\IMG\InvoiceColored'
    #PDFPath = input('请将文件拖进来')
    OCR_PDF(PDFPath,'快速')
    #OCR_IMGS(IMGPath,'快速')