import qrcode

data = "BEGIN:VCARD" + "\n"
data += "VERSION:3.0" + "\n"
data += "FN:Hello People" + "\n"
data += "TEL;TYPE=WORK;CELL:YOU BABO" + "\n"
data += "EMAIL;TYPE=WORK:TOO LATE" + "\n"
data += "URL;TYPE=IG:https://www.instagram.com\n"
data += "END:VCARD" + "\n"

img = qrcode.make(data)

#img.save('c:/Users/samsung/PythonQR/new/myqrcode.png')

qr = qrcode.QRCode(version = 8, box_size = 10, border = 1)

qr.add_data(data)

qr.make(fit=True)

img = qr.make_image(back_color=('#FFA98F'),edge_color=('#FFE0C6','#FFC7AD'),center_color=('#FFE0C6','#FFC7AD'))

img.save('c:/Users/samsung/PythonQR/new/myqrcode8.png')