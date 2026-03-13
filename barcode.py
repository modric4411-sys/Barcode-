import warnings
import barcode
from barcode.writer import ImageWriter
url = input("Enter barcode url:")

code128 = barcode.get_barcode_class("code128")
obj = code128(url,writer=ImageWriter())

filename = obj.save("barcode.png")

print(f"Barcode.saved{filename}.png.")
warnings.filterwarnings("ignore", category =UserWarning)
