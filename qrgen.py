import segno
import sys
from datetime import datetime

d = datetime.now()
time = d.strftime("%H_%M_%S")
url = sys.argv[1]
if not url:
    url = input("Please, type the URL")

qr = segno.make_qr(url)
qr.save("qr_"+time+".png")