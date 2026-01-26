# /// script
# dependencies = ["qrcode[pil]"]
# ///

# INSTRUCTIONS
# Simply run in the termonal `uv run qr_code_generator.py`

import qrcode

url = "https://bobiac.github.io"

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=300,
    border=1,
)
qr.add_data(url)
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")
img.save("bobiac_2026_qr_code.png")

print(f"QR code generated for {url} -> bobiac_2026_qr_code.png")