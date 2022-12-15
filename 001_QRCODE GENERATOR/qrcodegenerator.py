import qrcode
import image
qr = qrcode.QRCode(
    version = 15, #15mean the version of the qr code high the number bigger the code image and complicated picture
    box_size =10, # size of the box where qr code be discuss
    border = 5
)

data = "https://www.youtube.com/channel/UC5rps6bfIldvyo8LMw6Dksg"
# as i have given the path of my channel like the same way you can give anything
# if you don't want to redirect and create for normal text that write text in the quotes

qr.add_data(data)
qr.make(fit = True)
img = qr.make_image(fill="black",back_color = "white")
img.save("test.png")