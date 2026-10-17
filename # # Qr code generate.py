# # Qr code generate
import qrcode
files_code=input('enter massege for qr code:')
files_code_qr=qrcode.make(files_code)
files_code_qr.save(' all files python qr.png')
files_code_qr.show()