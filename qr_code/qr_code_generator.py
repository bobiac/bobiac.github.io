# /// script
# dependencies = ["qrcode[pil]"]
# ///

# INSTRUCTIONS
# Simply run in the termonal `uv run qr_code/qr_code_generator.py`

import qrcode

BOBIAC_GREEN = (132, 184, 114)
BOBIAC_BLUE = (128, 173, 185)

# url, filename pairs
urls = [
    ("https://bobiac.github.io", "bobiac_2026_qr_code"),
    ("https://forms.gle/KsrKJVZjRcQVfiGi6", "bobiac_application_2026_qr_code"),
    ("https://bobiac.github.io/bobiac-book", "bobiac_book_qr_code"),
]

for url, filename in urls:
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=100,
        border=1,
    )
    qr.add_data(url)
    qr.make(fit=True)

    colors = [
        ("black", "white", "black_white"),
        ("white", "black", "white_black"),
        (BOBIAC_GREEN, "black", "green_black"),
        ("black", BOBIAC_GREEN, "black_green"),
        (BOBIAC_BLUE, "black", "blue_black"),
        ("black", BOBIAC_BLUE, "black_blue"),    
    ]
    for fill_color, back_color, color_name in colors:
        img = qr.make_image(fill_color=fill_color, back_color=back_color)
        img.save(f"qr_code/{filename}_{color_name}.png")

        print(f"QR code generated for {url} -> {filename}_{color_name}.png")

print("All QR codes generated!")