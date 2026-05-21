#!/usr/bin/env python3
import qrcode
import os

# Base URL - will be updated once deployed to GitHub Pages
base_url = "https://krrulz.github.io/wish-book/wishes/"

wishes = [
    ("01", "slow-sunday"),
    ("02", "butter-toast"),
    ("03", "afterglow"),
    ("04", "cloud-nine"),
    ("05", "vanilla-sky"),
    ("06", "pillow-fort"),
    ("07", "velvet"),
    ("08", "polaroid"),
    ("09", "gold-rush"),
    ("10", "crown"),
    ("11", "mirage"),
    ("12", "firefly"),
    ("13", "passport"),
    ("14", "detour"),
    ("15", "compass"),
    ("16", "lantern"),
    ("17", "matchbox"),
    ("18", "side-quest"),
    ("19", "red-lantern"),
    ("20", "spice-route"),
    ("21", "midnight-snack"),
    ("22", "barrel-room"),
    ("23", "takeout"),
    ("24", "cherry-pop"),
    ("25", "moonlight"),
    ("26", "time-capsule"),
    ("27", "open-book"),
    ("28", "blueprint"),
    ("29", "ink"),
    ("30", "anchor"),
    ("31", "white-flag"),
    ("32", "vinyl"),
    ("33", "stardust")
]

# Create qr_codes directory
os.makedirs("/home/claude/wish-book/qr_codes", exist_ok=True)

for num, codename in wishes:
    url = f"{base_url}{num}-{codename}.html"
    
    # Create QR code
    qr = qrcode.QRCode(
        version=5,  # Size of QR code
        error_correction=qrcode.constants.ERROR_CORRECT_H,  # High error correction for dot-to-dot
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)
    
    # Create image
    img = qr.make_image(fill_color="black", back_color="white")
    
    # Save
    img_path = f"/home/claude/wish-book/qr_codes/wish-{num}.png"
    img.save(img_path)
    
    print(f"✓ Generated QR code for Wish #{num}: {codename}")

print(f"\n✨ All 33 QR codes generated successfully!")
print(f"📁 Saved in: /home/claude/wish-book/qr_codes/")
