import qrcode

name = input("pls enter your name for make qrcode: ")
phone_number = input("enter your phone_number: ")
email = input("enter your email: ")

imgqr = qrcode.make(name + "|" + phone_number + "|" + email)
imgqr.save("qr.jpg")
