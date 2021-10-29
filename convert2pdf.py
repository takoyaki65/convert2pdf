import os
import img2pdf
from PIL import Image  # img2pdfと一緒にインストールされたPillowを使う

if __name__ == '__main__':
    pdf_FileName = "output.pdf"
    img_Folder = "./jpg/"
    extension = "jpg"

    with open(pdf_FileName, "wb") as f:
        img_List = os.listdir(img_Folder)
        img_List.sort()
        # 画像フォルダの中にあるJPGファイルを取得し配列に追加、バイナリ形式でファイルに書き込む
        f.write(img2pdf.convert(
            [Image.open(img_Folder+j).filename for j in img_List if j.endswith(extension)]))
