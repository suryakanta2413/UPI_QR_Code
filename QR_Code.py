# pip install qrcode
# pip install pillow

import qrcode

#Taking UPI id as input from user
upi_id = input("Enter your UPI ID: ")

# upi://pay?pa=UPI_ID&pn=NAME&am=AMOUNT&cu=CURRENCY&tn=MESSAGE
#pa = user UPI ID
#pn = Recipient Name
#am = Amount
#cu = Currency
#tn = Transaction Note

phonepe_link = f"upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234"
paytm_link = f"upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234"
googlepay_link = f"upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234"

#Generating QR code 
phonepe_qr = qrcode.make(phonepe_link)
paytm_qr = qrcode.make(paytm_link)
googlepay_qr = qrcode.make(googlepay_link)

#Saving the images
phonepe_qr.save("phonepe_upi_qr.png")
paytm_qr.save("paytm_upi_qr.png")
googlepay_qr.save("googlepay_upi_qr.png")

#Displaying the QR code
phonepe_qr.show()
paytm_qr.show()
googlepay_qr.show()