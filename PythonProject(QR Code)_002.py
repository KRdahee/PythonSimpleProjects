import qrcode

data = '우리집 최고의 아웃풋이 될꺼야 딱 기달류후후후'

img = qrcode.make(data)

#img.save('c:/Users/samsung/PythonQR/new/myqrcode.png')

qr = qrcode.QRCode(version = 6, box_size = 10, border = 1)

qr.add_data(data)

qr.make(fit=True)

img = qr.make_image(back_color=('#FFA98F','#FFC7AD','#FFE0C6'),edge_color=('#FFE0C6','#FFC7AD','#FFA98F'),center_color=('#FFE0C6','#FFC7AD','#FFA98F'))

img.save('c:/Users/samsung/PythonQR/new/myqrcode6.png')