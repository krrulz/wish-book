#!/usr/bin/env python3
from reportlab.lib.pagesizes import A5
from reportlab.lib.units import mm
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from PIL import Image
import random
import math

# A5 dimensions
width, height = A5

# Colors for scrapbook aesthetic
CREAM = HexColor('#FFF8E7')
SOFT_PINK = HexColor('#FFB6C1')
ROSE = HexColor('#D4837A')
WARM_BROWN = HexColor('#8B6B47')
GOLD = HexColor('#DAA520')
LIGHT_GRAY = HexColor('#E0E0E0')

wishes_data = [
    {"num": "01", "codename": "Slow Sunday", "theme": "relax", "icons": ["☕", "🛋️", "😴", "📺", "🥱", "💤"]},
    {"num": "02", "codename": "Butter Toast", "theme": "food", "icons": ["🍞", "🧈", "☕", "🥐", "🍳", "🥞"]},
    {"num": "03", "codename": "Afterglow", "theme": "romance", "icons": ["🕯️", "💕", "🌹", "💑", "✨", "💝"]},
    {"num": "04", "codename": "Cloud Nine", "theme": "relax", "icons": ["☁️", "💆", "🛁", "🌸", "🧖", "✨"]},
    {"num": "05", "codename": "Vanilla Sky", "theme": "romance", "icons": ["☕", "💐", "💌", "🌸", "💝", "✨"]},
    {"num": "06", "codename": "Pillow Fort", "theme": "fun", "icons": ["🎬", "🍿", "🎥", "🛋️", "🎭", "📺"]},
    {"num": "07", "codename": "Velvet", "theme": "food", "icons": ["🍽️", "🥂", "🍷", "🍴", "✨", "🌹"]},
    {"num": "08", "codename": "Polaroid", "theme": "adventure", "icons": ["☕", "📸", "🏠", "✨", "🎨", "💝"]},
    {"num": "09", "codename": "Gold Rush", "theme": "fun", "icons": ["🛍️", "👗", "💳", "✨", "👜", "💄"]},
    {"num": "10", "codename": "Crown", "theme": "romance", "icons": ["👑", "💝", "✨", "🌹", "💕", "💖"]},
    {"num": "11", "codename": "Mirage", "theme": "adventure", "icons": ["🎭", "❓", "✨", "🎁", "💝", "🎉"]},
    {"num": "12", "codename": "Firefly", "theme": "fun", "icons": ["📸", "📷", "✨", "💕", "🌟", "💝"]},
    {"num": "13", "codename": "Passport", "theme": "adventure", "icons": ["✈️", "🏖️", "🗺️", "🎒", "📸", "🌍"]},
    {"num": "14", "codename": "Detour", "theme": "adventure", "icons": ["🚗", "🗺️", "🛣️", "🌄", "📸", "✨"]},
    {"num": "15", "codename": "Compass", "theme": "romance", "icons": ["🧭", "💝", "✨", "🎁", "💕", "🌟"]},
    {"num": "16", "codename": "Lantern", "theme": "romance", "icons": ["🌅", "📸", "💑", "✨", "🌞", "💝"]},
    {"num": "17", "codename": "Matchbox", "theme": "fun", "icons": ["🎨", "✨", "🎭", "💡", "🌟", "💝"]},
    {"num": "18", "codename": "Side Quest", "theme": "fun", "icons": ["✅", "🎉", "✨", "🎁", "💝", "🌟"]},
    {"num": "19", "codename": "Red Lantern", "theme": "food", "icons": ["🥡", "🍜", "🥟", "🍲", "🥢", "🍱"]},
    {"num": "20", "codename": "Spice Route", "theme": "food", "icons": ["🍛", "🍚", "🫓", "🌶️", "🍲", "✨"]},
    {"num": "21", "codename": "Midnight Snack", "theme": "food", "icons": ["🍰", "🍦", "🌙", "✨", "🍪", "🍩"]},
    {"num": "22", "codename": "Barrel Room", "theme": "fun", "icons": ["🍺", "🥃", "🍻", "✨", "🌙", "💝"]},
    {"num": "23", "codename": "Takeout", "theme": "food", "icons": ["🍕", "🍔", "🍜", "🥡", "🍱", "✨"]},
    {"num": "24", "codename": "Cherry Pop", "theme": "food", "icons": ["🍰", "🧁", "🍪", "🍩", "🍫", "✨"]},
    {"num": "25", "codename": "Moonlight", "theme": "romance", "icons": ["💃", "🎵", "🌙", "💑", "✨", "💝"]},
    {"num": "26", "codename": "Time Capsule", "theme": "romance", "icons": ["📸", "💕", "💭", "✨", "💝", "🌟"]},
    {"num": "27", "codename": "Open Book", "theme": "romance", "icons": ["💬", "💝", "❓", "✨", "💕", "🌟"]},
    {"num": "28", "codename": "Blueprint", "theme": "romance", "icons": ["🗺️", "💭", "✨", "💝", "🌟", "💕"]},
    {"num": "29", "codename": "Ink", "theme": "romance", "icons": ["✍️", "💌", "📜", "💝", "✨", "💕"]},
    {"num": "30", "codename": "Anchor", "theme": "romance", "icons": ["⚓", "💝", "🤗", "✨", "💕", "🌟"]},
    {"num": "31", "codename": "White Flag", "theme": "fun", "icons": ["🏳️", "😊", "✨", "💝", "😄", "💕"]},
    {"num": "32", "codename": "Vinyl", "theme": "fun", "icons": ["🎵", "🎶", "🎧", "💿", "✨", "💝"]},
    {"num": "33", "codename": "Stardust", "theme": "romance", "icons": ["✨", "🎁", "❓", "💝", "🌟", "💕"]}
]

def draw_decorative_border(c):
    """Draw a subtle decorative border"""
    c.setStrokeColor(ROSE)
    c.setLineWidth(0.5)
    c.rect(10*mm, 10*mm, width-20*mm, height-20*mm)

def draw_corner_decoration(c, x, y, size=4):
    """Draw small decorative element in corners"""
    c.setFillColor(SOFT_PINK)
    c.setStrokeColor(ROSE)
    c.setLineWidth(0.5)
    # Small flower
    for i in range(6):
        angle = i * 60 * (3.14159 / 180)
        px = x + size * math.cos(angle)
        py = y + size * math.sin(angle)
        c.circle(px, py, size/2.5, fill=1, stroke=1)

def convert_qr_to_improved_dots(qr_image_path, complexity='medium'):
    """Convert QR code to clearer dot-to-dot coordinates with better spacing"""
    img = Image.open(qr_image_path).convert('L')
    
    # Better sampling for clarity
    if complexity == 'simple':
        sample_rate = 10  # Much fewer, clearer dots
    else:  # medium
        sample_rate = 7   # Moderate dots for better scannability
    
    dots = []
    dot_number = 1
    
    # Create a grid pattern for more organized dots
    for y in range(0, img.height, sample_rate):
        row_dots = []
        for x in range(0, img.width, sample_rate):
            if img.getpixel((x, y)) < 128:  # Black pixel
                row_dots.append((x, y, dot_number))
                dot_number += 1
        
        # Add dots from this row
        dots.extend(row_dots)
    
    return dots, img.size

def draw_themed_icon(c, x, y, icon, size=12):
    """Draw emoji/icon as text with background"""
    c.setFont("Helvetica", size)
    c.setFillColor(SOFT_PINK)
    # Background circle
    c.circle(x, y, size*0.7, fill=1, stroke=0)
    
    # Icon text
    c.setFillColor(WARM_BROWN)
    c.drawCentredString(x, y-size*0.3, icon)

def draw_cover_page(c):
    """Draw the beautiful cover page with the love letter"""
    c.setFillColor(CREAM)
    c.rect(0, 0, width, height, fill=1, stroke=0)
    
    # Decorative border
    c.setStrokeColor(ROSE)
    c.setLineWidth(2)
    c.rect(15*mm, 15*mm, width-30*mm, height-30*mm)
    
    # Inner decorative border
    c.setStrokeColor(SOFT_PINK)
    c.setLineWidth(1)
    c.rect(18*mm, 18*mm, width-36*mm, height-36*mm)
    
    # Corner decorations
    corners = [(25*mm, height-25*mm), (width-25*mm, height-25*mm), 
               (25*mm, 25*mm), (width-25*mm, 25*mm)]
    for x, y in corners:
        draw_corner_decoration(c, x, y, 5)
    
    # Title with shadow effect
    c.setFillColor(LIGHT_GRAY)
    c.setFont("Helvetica-Bold", 26)
    c.drawCentredString(width/2+1, height-38*mm, "33 Wishes")
    c.setFillColor(ROSE)
    c.drawCentredString(width/2, height-39*mm, "33 Wishes")
    
    c.setFont("Helvetica", 18)
    c.setFillColor(WARM_BROWN)
    c.drawCentredString(width/2, height-50*mm, "for Melu")
    
    # Decorative line
    c.setStrokeColor(GOLD)
    c.setLineWidth(1.5)
    c.line(35*mm, height-56*mm, width-35*mm, height-56*mm)
    
    # Small hearts decoration
    c.setFont("Helvetica", 14)
    c.setFillColor(ROSE)
    for i in range(3):
        x = width/2 - 20*mm + i * 20*mm
        c.drawCentredString(x, height-63*mm, "♥")
    
    # Bottom text
    c.setFont("Helvetica-Oblique", 11)
    c.setFillColor(WARM_BROWN)
    c.drawCentredString(width/2, 35*mm, "Connect the dots")
    c.drawCentredString(width/2, 30*mm, "Scan the code")
    c.drawCentredString(width/2, 25*mm, "Unlock the wish")
    
    c.showPage()

def draw_letter_page(c):
    """Draw the love letter page"""
    c.setFillColor(CREAM)
    c.rect(0, 0, width, height, fill=1, stroke=0)
    
    # Simple border
    draw_decorative_border(c)
    
    # Decorative corner hearts
    c.setFont("Helvetica", 16)
    c.setFillColor(ROSE)
    c.drawCentredString(25*mm, height-20*mm, "♥")
    c.drawCentredString(width-25*mm, height-20*mm, "♥")
    
    # Letter content
    c.setFillColor(WARM_BROWN)
    c.setFont("Helvetica", 10)
    
    y_pos = height - 35*mm
    line_height = 4.8*mm
    
    letter_lines = [
        "Melu,",
        "",
        "Happy 33rd, my love.",
        "",
        "I wanted to do something different this year — something",
        "that's just... us. So here it is: 33 wishes, one for each",
        "beautiful year you've been in this world, each one",
        "waiting for you to unlock.",
        "",
        "You know, sometimes I wonder how I got so lucky. The",
        "way you care for everyone around you, how deeply you",
        "feel everything, how you make even the smallest moments",
        "feel special — that's just who you are. And I fall in love",
        "with that person over and over again.",
        "",
        "You're my partner in everything — from lazy Sundays to",
        "spontaneous adventures, from quiet conversations to the",
        "most chaotic days. You make life better, Melu. You make",
        "me better.",
        "",
        "So this book? It's my way of saying thank you. Thank you",
        "for being you, for choosing me, for filling our life with so",
        "much love and laughter. Each wish inside is a little",
        "promise — a date, a surprise, a moment I want to create",
        "just for you.",
        "",
        "Connect the dots, scan the code, and let's make this year",
        "unforgettable.",
        "",
        "I love you more than words can say.",
        "",
        "Always yours,",
        "Karthik"
    ]
    
    for line in letter_lines:
        c.drawString(22*mm, y_pos, line)
        y_pos -= line_height
    
    # Bottom decoration with hearts
    c.setFont("Helvetica", 12)
    c.setFillColor(ROSE)
    for i in range(5):
        x = width/2 - 25*mm + i * 12*mm
        c.drawCentredString(x, 15*mm, "♥")
    
    c.showPage()

def draw_wish_page(c, wish_num, codename, theme, icons, qr_dots, qr_size, complexity):
    """Draw individual wish page with clearer dot-to-dot QR code and themed icons"""
    c.setFillColor(CREAM)
    c.rect(0, 0, width, height, fill=1, stroke=0)
    
    # Simple border
    draw_decorative_border(c)
    
    # Title area with background
    c.setFillColor(HexColor('#FFF0E5'))
    c.roundRect(18*mm, height-35*mm, width-36*mm, 20*mm, 3*mm, fill=1, stroke=0)
    
    # Title
    c.setFillColor(ROSE)
    c.setFont("Helvetica-Bold", 16)
    c.drawCentredString(width/2, height-23*mm, codename)
    
    c.setFillColor(WARM_BROWN)
    c.setFont("Helvetica", 9)
    c.drawCentredString(width/2, height-30*mm, f"Wish #{wish_num}")
    
    # Draw themed icons around the page as visual clues
    random.seed(int(wish_num))  # Consistent positions per wish
    
    # Top icons (3)
    top_y = height - 12*mm
    for i, icon in enumerate(icons[:3]):
        x = 30*mm + i * 30*mm
        draw_themed_icon(c, x, top_y, icon, 11)
    
    # Bottom icons (3)
    bottom_y = 18*mm
    for i, icon in enumerate(icons[3:]):
        x = 30*mm + i * 30*mm
        draw_themed_icon(c, x, bottom_y, icon, 11)
    
    # Draw IMPROVED dot-to-dot QR code in center
    qr_center_x = width / 2
    qr_center_y = height / 2 + 3*mm
    qr_scale = 55 / qr_size[0]  # Slightly smaller for better fit
    
    # Draw connection guide lines first (very faint)
    c.setStrokeColor(LIGHT_GRAY)
    c.setLineWidth(0.3)
    c.setDash(1, 2)
    
    for i in range(len(qr_dots)-1):
        x1, y1, num1 = qr_dots[i]
        x2, y2, num2 = qr_dots[i+1]
        
        dot_x1 = qr_center_x + (x1 - qr_size[0]/2) * qr_scale
        dot_y1 = qr_center_y + (y1 - qr_size[1]/2) * qr_scale
        dot_x2 = qr_center_x + (x2 - qr_size[0]/2) * qr_scale
        dot_y2 = qr_center_y + (y2 - qr_size[1]/2) * qr_scale
        
        # Only draw line if dots are reasonably close (part of same pattern)
        distance = math.sqrt((dot_x2-dot_x1)**2 + (dot_y2-dot_y1)**2)
        if distance < 15:  # mm
            c.line(dot_x1, dot_y1, dot_x2, dot_y2)
    
    c.setDash()  # Reset dash
    
    # Draw dots with CLEAR numbers
    c.setFont("Helvetica-Bold", 7)
    
    for x, y, num in qr_dots:
        # Scale and position
        dot_x = qr_center_x + (x - qr_size[0]/2) * qr_scale
        dot_y = qr_center_y + (y - qr_size[1]/2) * qr_scale
        
        # Draw WHITE circle background for number
        c.setFillColor(HexColor('#FFFFFF'))
        c.circle(dot_x, dot_y, 2.5, fill=1, stroke=0)
        
        # Draw dot
        c.setFillColor(WARM_BROWN)
        c.circle(dot_x, dot_y, 1.2, fill=1)
        
        # Draw number OUTSIDE the dot with better positioning
        c.setFillColor(ROSE)
        
        # Alternate number positions for better readability
        if num % 2 == 0:
            # Top right
            c.drawString(dot_x + 2, dot_y + 0.5, str(num))
        else:
            # Bottom right
            c.drawString(dot_x + 2, dot_y - 2.5, str(num))
    
    # Instruction at bottom with icon
    c.setFillColor(WARM_BROWN)
    c.setFont("Helvetica-Oblique", 8)
    c.drawCentredString(width/2, 8*mm, 
        f"Connect dots 1→{len(qr_dots)} then scan to reveal your wish!")
    
    # Add small decorative element
    c.setFont("Helvetica", 10)
    c.setFillColor(GOLD)
    c.drawCentredString(width/2, 4*mm, "✦")
    
    c.showPage()

# Generate the PDF
def create_improved_wish_book():
    pdf_path = "/home/claude/wish-book/Melus_33_Wishes_Book_v2.pdf"
    c = canvas.Canvas(pdf_path, pagesize=A5)
    
    print("Creating IMPROVED wish book PDF...")
    print("  ⚡ Better dot visibility")
    print("  🔢 Clearer number guidance")
    print("  🎨 Themed icon clues on each page")
    print()
    
    # Cover page
    print("  ✓ Drawing enhanced cover page...")
    draw_cover_page(c)
    
    # Letter page
    print("  ✓ Drawing love letter page...")
    draw_letter_page(c)
    
    # Individual wish pages
    for i, wish in enumerate(wishes_data, 1):
        qr_path = f"/home/claude/wish-book/qr_codes/wish-{wish['num']}.png"
        
        # Alternate complexity for variety
        complexity = 'simple' if i % 3 == 0 else 'medium'
        
        dots, qr_size = convert_qr_to_improved_dots(qr_path, complexity)
        
        print(f"  ✓ Wish {wish['num']}: {wish['codename']} - {len(dots)} dots, icons: {' '.join(wish['icons'][:3])}")
        
        draw_wish_page(c, wish['num'], wish['codename'], wish['theme'], 
                      wish['icons'], dots, qr_size, complexity)
    
    # Save PDF
    c.save()
    print(f"\n✨ IMPROVED wish book created successfully!")
    print(f"📁 Saved as: {pdf_path}")
    print(f"📄 Total pages: {len(wishes_data) + 2} (cover + letter + 33 wishes)")
    print(f"\n🎨 Each page now has:")
    print(f"   • Clearer, larger dots")
    print(f"   • Better number positioning (alternating for readability)")
    print(f"   • Themed emoji icons as visual clues")
    print(f"   • Faint guide lines between nearby dots")
    print(f"   • Instructions showing total dot count")
    
    return pdf_path

if __name__ == "__main__":
    create_improved_wish_book()
