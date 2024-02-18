from ironpdf import *
import easyocr
import cv2
from pyzbar.pyzbar import decode
import os
import tempfile


class OcrTools:
    def __init__(self, pdfPath):
        self.pdfPath = pdfPath

    def pdfToImg(pdfPath="", locationFile=""):
        pdf = PdfDocument.FromFile(pdfPath)
        # Extract all pages to a folder as image files
        pdf.RasterizeToImageFiles(locationFile, DPI=300)
        return locationFile

    def easyOCR(typeOfOcr='Text', locationFile="",
                area={'offset_x_min': 0, 'offset_y_min': 0,
                      'width': 0, 'height': 0},
                dataCheck=['valueForCheck'],
                languageOcr=['th', 'en'],
                deviation=50
                ):
        temp = tempfile.mkdtemp(prefix="pre_",suffix="_suf")
        name, extension = os.path.splitext(locationFile)
        if extension == ".pdf":
            root = locationFile.find("/")
            if root > 0:
                newFileLocation = locationFile.rsplit('/', 1)[1]
            else:
                newFileLocation = "."
            imageLocation = OcrTools.pdfToImg(
                locationFile, temp+"\\"+newFileLocation+".png")
            print(imageLocation)
        area_xMax = area['offset_x_min']+area['width']
        area_yMax = area['offset_y_min']+area['height']
        if typeOfOcr == 'Text':
            allResultDetective = []
            reader = easyocr.Reader(languageOcr)
            allResults = reader.readtext(imageLocation)
            for result in allResults:
                pos1, pos2, pos3, pos4 = result[0]
                xMin = round(min([pos1[0], pos2[0], pos3[0], pos4[0]]))
                xMax = round(max([pos1[0], pos2[0], pos3[0], pos4[0]]))
                yMin = round(min([pos1[1], pos2[1], pos3[1], pos4[1]]))
                yMax = round(max([pos1[1], pos2[1], pos3[1], pos4[1]]))
                if (area['offset_x_min'] in range(xMin-deviation, xMin+deviation)):
                    if (area['offset_y_min'] in range(yMin-deviation, yMin+deviation)):
                        if (area_xMax in range(xMax-deviation, xMax+deviation)):
                            if (area_yMax in range(area_yMax-deviation, area_yMax+deviation)):
                                word = result[1]
                                if word in dataCheck:
                                    valid = True
                                else:
                                    valid = False
                                accuracy_percent = str(
                                    round(result[2]*100))+"%"
                                allResultDetective.append({
                                    'coordinates': result[0],
                                    'value': word,
                                    'valid': valid,
                                    'accuracy_percent': accuracy_percent,
                                })
            os.remove(imageLocation)
            return allResultDetective
        elif typeOfOcr == 'qrcode':
            image = cv2.imread(imageLocation)
            cropped_image = image[area['offset_y_min']:area_yMax, area['offset_x_min']:area_xMax]
            result = decode(cropped_image)
            os.remove(imageLocation)
            if result:
                return {
                    'coordinates': [area['offset_y_min'], area_yMax, area['offset_x_min'], area_xMax],
                    'value': result[0].data,
                    'valid': True,
                    'accuracy_percent': '-',
                }
            else:
                return {
                    'coordinates': [area['offset_y_min'], area_yMax, area['offset_x_min'], area_xMax],
                    'value': result,
                    'valid': False,
                    'accuracy_percent': '-',
                }
