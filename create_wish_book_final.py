#!/usr/bin/env python3
from reportlab.lib.pagesizes import A5
from reportlab.lib.units import mm
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor
from PIL import Image
import random
import math

# A5 dimensions
width, height = A5

# Extended color palette for scrapbook aesthetic
CREAM = HexColor('#FFF8E7')
SOFT_PINK = HexColor('#FFB6C1')
ROSE = HexColor('#D4837A')
WARM_BROWN = HexColor('#8B6B47')
GOLD = HexColor('#DAA520')
LIGHT_GRAY = HexColor('#E0E0E0')
PEACH = HexColor('#FFDAB9')
LAVENDER = HexColor('#E6E6FA')
MINT = HexColor('#98D8C8')

wishes_data = [
    {"num": "01", "codename": "Slow Sunday", "theme": "relax", "icons": ["☕", "🛋️", "😴", "📺", "🥱", "💤", "🌙", "☁️"], "color": LAVENDER},
    {"num": "02", "codename": "Butter Toast", "theme": "food", "icons": ["🍞", "🧈", "☕", "🥐", "🍳", "🥞", "🧇", "🍯"], "color": PEACH},
    {"num": "03", "codename": "Afterglow", "theme": "romance", "icons": ["🕯️", "💕", "🌹", "💑", "✨", "💝", "🌟", "💖"], "color": SOFT_PINK},
    {"num": "04", "codename": "Cloud Nine", "theme": "relax", "icons": ["☁️", "💆", "🛁", "🌸", "🧖", "✨", "🌺", "💅"], "color": LAVENDER},
    {"num": "05", "codename": "Vanilla Sky", "theme": "romance", "icons": ["☕", "💐", "💌", "🌸", "💝", "✨", "🌹", "💕"], "color": SOFT_PINK},
    {"num": "06", "codename": "Pillow Fort", "theme": "fun", "icons": ["🎬", "🍿", "🎥", "🛋️", "🎭", "📺", "🎪", "🎨"], "color": MINT},
    {"num": "07", "codename": "Velvet", "theme": "food", "icons": ["🍽️", "🥂", "🍷", "🍴", "✨", "🌹", "🕯️", "🥗"], "color": PEACH},
    {"num": "08", "codename": "Polaroid", "theme": "adventure", "icons": ["☕", "📸", "🏠", "✨", "🎨", "💝", "🖼️", "📷"], "color": MINT},
    {"num": "09", "codename": "Gold Rush", "theme": "fun", "icons": ["🛍️", "👗", "💳", "✨", "👜", "💄", "👠", "💍"], "color": GOLD},
    {"num": "10", "codename": "Crown", "theme": "romance", "icons": ["👑", "💝", "✨", "🌹", "💕", "💖", "🌟", "💎"], "color": SOFT_PINK},
    {"num": "11", "codename": "Mirage", "theme": "adventure", "icons": ["🎭", "❓", "✨", "🎁", "💝", "🎉", "🎪", "🌟"], "color": MINT},
    {"num": "12", "codename": "Firefly", "theme": "fun", "icons": ["📸", "📷", "✨", "💕", "🌟", "💝", "🎨", "🖼️"], "color": MINT},
    {"num": "13", "codename": "Passport", "theme": "adventure", "icons": ["✈️", "🏖️", "🗺️", "🎒", "📸", "🌍", "🌴", "🗼"], "color": MINT},
    {"num": "14", "codename": "Detour", "theme": "adventure", "icons": ["🚗", "🗺️", "🛣️", "🌄", "📸", "✨", "🌅", "🏞️"], "color": MINT},
    {"num": "15", "codename": "Compass", "theme": "romance", "icons": ["🧭", "💝", "✨", "🎁", "💕", "🌟", "💖", "🎀"], "color": SOFT_PINK},
    {"num": "16", "codename": "Lantern", "theme": "romance", "icons": ["🌅", "📸", "💑", "✨", "🌞", "💝", "🌄", "🌇"], "color": SOFT_PINK},
    {"num": "17", "codename": "Matchbox", "theme": "fun", "icons": ["🎨", "✨", "🎭", "💡", "🌟", "💝", "🎪", "🎡"], "color": MINT},
    {"num": "18", "codename": "Side Quest", "theme": "fun", "icons": ["✅", "🎉", "✨", "🎁", "💝", "🌟", "🎊", "🎈"], "color": MINT},
    {"num": "19", "codename": "Red Lantern", "theme": "food", "icons": ["🥡", "🍜", "🥟", "🍲", "🥢", "🍱", "🥠", "🍵"], "color": PEACH},
    {"num": "20", "codename": "Spice Route", "theme": "food", "icons": ["🍛", "🍚", "🫓", "🌶️", "🍲", "✨", "🫕", "🥘"], "color": PEACH},
    {"num": "21", "codename": "Midnight Snack", "theme": "food", "icons": ["🍰", "🍦", "🌙", "✨", "🍪", "🍩", "🧁", "🍫"], "color": PEACH},
    {"num": "22", "codename": "Barrel Room", "theme": "fun", "icons": ["🍺", "🥃", "🍻", "✨", "🌙", "💝", "🍷", "🥂"], "color": GOLD},
    {"num": "23", "codename": "Takeout", "theme": "food", "icons": ["🍕", "🍔", "🍜", "🥡", "🍱", "✨", "🌮", "🍟"], "color": PEACH},
    {"num": "24", "codename": "Cherry Pop", "theme": "food", "icons": ["🍰", "🧁", "🍪", "🍩", "🍫", "✨", "🍬", "🍭"], "color": PEACH},
    {"num": "25", "codename": "Moonlight", "theme": "romance", "icons": ["💃", "🎵", "🌙", "💑", "✨", "💝", "🎶", "💕"], "color": SOFT_PINK},
    {"num": "26", "codename": "Time Capsule", "theme": "romance", "icons": ["📸", "💕", "💭", "✨", "💝", "🌟", "📷", "🖼️"], "color": SOFT_PINK},
    {"num": "27", "codename": "Open Book", "theme": "romance", "icons": ["💬", "💝", "❓", "✨", "💕", "🌟", "💖", "📖"], "color": SOFT_PINK},
    {"num": "28", "codename": "Blueprint", "theme": "romance", "icons": ["🗺️", "💭", "✨", "💝", "🌟", "💕", "🎯", "💖"], "color": SOFT_PINK},
    {"num": "29", "codename": "Ink", "theme": "romance", "icons": ["✍️", "💌", "📜", "💝", "✨", "💕", "🖋️", "💖"], "color": SOFT_PINK},
    {"num": "30", "codename": "Anchor", "theme": "romance", "icons": ["⚓", "💝", "🤗", "✨", "💕", "🌟", "💖", "🫂"], "color": SOFT_PINK},
    {"num": "31", "codename": "White Flag", "theme": "fun", "icons": ["🏳️", "😊", "✨", "💝", "😄", "💕", "😌", "🤝"], "color": MINT},
    {"num": "32", "codename": "Vinyl", "theme": "fun", "icons": ["🎵", "🎶", "🎧", "💿", "✨", "💝", "🎼", "🎤"], "color": MINT},
    {"num": "33", "codename": "Stardust", "theme": "romance", "icons": ["✨", "🎁", "❓", "💝", "🌟", "💕", "⭐", "💖"], "color": GOLD}
]

def draw_decorative_corner(c, x, y, size, rotation=0):
    """Draw ornate corner decoration"""
    c.saveState()
    c.translate(x, y)
    c.rotate(rotation)
    
    # Ornate corner flourish
    c.setStrokeColor(ROSE)
    c.setLineWidth(1.5)
    
    # Curved lines
    path = c.beginPath()
    path.moveTo(0, 0)
    path.curveTo(size*0.3, size*0.1, size*0.5, size*0.3, size*0.6, size*0.6)
    c.drawPath(path)
    
    path = c.beginPath()
    path.moveTo(0, 0)
    path.curveTo(size*0.1, size*0.3, size*0.3, size*0.5, size*0.6, size*0.6)
    c.drawPath(path)
    
    # Small dots
    c.setFillColor(GOLD)
    for i in range(3):
        c.circle(i*size*0.2, i*size*0.2, 1, fill=1)
    
    c.restoreState()

def draw_floral_border(c, x, y, w, h):
    """Draw decorative floral border"""
    c.setStrokeColor(ROSE)
    c.setLineWidth(2)
    c.roundRect(x, y, w, h, 5*mm)
    
    c.setLineWidth(1)
    c.setStrokeColor(SOFT_PINK)
    c.roundRect(x+2*mm, y+2*mm, w-4*mm, h-4*mm, 4*mm)

def draw_scattered_hearts(c, positions, sizes):
    """Draw scattered decorative hearts"""
    c.setFont("Helvetica", 12)
    colors = [ROSE, SOFT_PINK, GOLD]
    
    for i, (x, y) in enumerate(positions):
        c.setFillColor(colors[i % 3])
        size = sizes[i % len(sizes)]
        c.setFontSize(size)
        c.drawCentredString(x, y, "♥")

def draw_star_cluster(c, x, y, count=5):
    """Draw a cluster of decorative stars"""
    c.setFillColor(GOLD)
    c.setFont("Helvetica", 10)
    
    for i in range(count):
        angle = (i * 72) * (3.14159 / 180)
        sx = x + 8 * math.cos(angle)
        sy = y + 8 * math.sin(angle)
        size = 14 if i % 2 == 0 else 10
        c.setFontSize(size)
        c.drawCentredString(sx, sy, "✦")

def draw_themed_decorations(c, theme, positions):
    """Draw theme-specific decorative elements"""
    c.setFont("Helvetica", 16)
    
    if theme == "romance":
        # Hearts and sparkles pattern
        for i, (x, y) in enumerate(positions):
            if i % 2 == 0:
                c.setFillColor(ROSE)
                c.drawCentredString(x, y, "♥")
            else:
                c.setFillColor(GOLD)
                c.setFontSize(12)
                c.drawCentredString(x, y, "✨")
                c.setFontSize(16)
    
    elif theme == "food":
        # Decorative food elements
        c.setStrokeColor(WARM_BROWN)
        c.setLineWidth(1.5)
        for x, y in positions[:4]:
            # Fork and knife pattern
            c.line(x-3, y, x-3, y+8)
            c.line(x+3, y, x+3, y+8)
    
    elif theme == "adventure":
        # Compass points and paths
        for x, y in positions:
            c.setFillColor(WARM_BROWN)
            c.setFontSize(14)
            c.drawCentredString(x, y, "✦")
    
    elif theme == "fun":
        # Confetti pattern
        colors = [ROSE, GOLD, SOFT_PINK, MINT]
        for i, (x, y) in enumerate(positions):
            c.setFillColor(colors[i % 4])
            c.circle(x, y, 2, fill=1)
    
    elif theme == "relax":
        # Peaceful waves and clouds
        c.setStrokeColor(LAVENDER)
        c.setLineWidth(1.5)
        for x, y in positions[:4]:
            path = c.beginPath()
            path.moveTo(x-5, y)
            path.curveTo(x-3, y+3, x-1, y+3, x+1, y)
            path.curveTo(x+3, y-3, x+5, y-3, x+7, y)
            c.drawPath(path)

def draw_icon_with_background(c, x, y, icon, bg_color, size=14):
    """Draw icon with decorative background"""
    # Background circle
    c.setFillColor(bg_color)
    c.circle(x, y, size*0.8, fill=1, stroke=0)
    
    # Border
    c.setStrokeColor(ROSE)
    c.setLineWidth(1)
    c.circle(x, y, size*0.8, fill=0, stroke=1)
    
    # Icon
    c.setFont("Helvetica", size)
    c.setFillColor(WARM_BROWN)
    c.drawCentredString(x, y-size*0.3, icon)

def draw_cover_page(c):
    """Draw the beautiful cover page"""
    c.setFillColor(CREAM)
    c.rect(0, 0, width, height, fill=1, stroke=0)
    
    # Outer decorative border
    c.setStrokeColor(ROSE)
    c.setLineWidth(3)
    c.roundRect(12*mm, 12*mm, width-24*mm, height-24*mm, 8*mm)
    
    # Inner border
    c.setStrokeColor(GOLD)
    c.setLineWidth(1.5)
    c.roundRect(16*mm, 16*mm, width-32*mm, height-32*mm, 6*mm)
    
    # Background pattern
    c.setFillColor(HexColor('#FFF5EE'))
    c.setFillAlpha(0.3)
    c.circle(width/2, height/2, 50*mm, fill=1, stroke=0)
    c.setFillAlpha(1)
    
    # Corner decorations
    corners = [
        (20*mm, height-20*mm, 0),
        (width-20*mm, height-20*mm, 90),
        (20*mm, 20*mm, 270),
        (width-20*mm, 20*mm, 180)
    ]
    for x, y, rot in corners:
        draw_decorative_corner(c, x, y, 15, rot)
    
    # Title with shadow
    c.setFillColor(LIGHT_GRAY)
    c.setFont("Helvetica-Bold", 28)
    c.drawCentredString(width/2+1, height-38*mm, "33 Wishes")
    c.setFillColor(ROSE)
    c.drawCentredString(width/2, height-39*mm, "33 Wishes")
    
    c.setFont("Helvetica", 20)
    c.setFillColor(WARM_BROWN)
    c.drawCentredString(width/2, height-50*mm, "for Melu")
    
    # Decorative divider
    c.setStrokeColor(GOLD)
    c.setLineWidth(2)
    c.line(30*mm, height-58*mm, width-30*mm, height-58*mm)
    
    # Heart clusters
    draw_star_cluster(c, width/2-25*mm, height-65*mm, 5)
    draw_star_cluster(c, width/2+25*mm, height-65*mm, 5)
    
    # Scattered hearts
    heart_positions = [(width/2-30*mm, height-75*mm), (width/2, height-78*mm), (width/2+30*mm, height-75*mm)]
    c.setFont("Helvetica", 18)
    c.setFillColor(ROSE)
    for x, y in heart_positions:
        c.drawCentredString(x, y, "♥")
    
    # Bottom instructions
    c.setFont("Helvetica-Oblique", 11)
    c.setFillColor(WARM_BROWN)
    c.drawCentredString(width/2, 38*mm, "Scan each QR code")
    c.drawCentredString(width/2, 33*mm, "to unlock your wish")
    
    # Decorative border at bottom
    c.setFont("Helvetica", 12)
    c.setFillColor(GOLD)
    for i in range(7):
        x = 25*mm + i * 15*mm
        c.drawCentredString(x, 25*mm, "✦")
    
    c.showPage()

def draw_letter_page(c):
    """Draw the love letter page"""
    c.setFillColor(CREAM)
    c.rect(0, 0, width, height, fill=1, stroke=0)
    
    # Decorative border
    draw_floral_border(c, 12*mm, 12*mm, width-24*mm, height-24*mm)
    
    # Corner hearts
    c.setFont("Helvetica", 18)
    c.setFillColor(ROSE)
    c.drawCentredString(22*mm, height-22*mm, "♥")
    c.drawCentredString(width-22*mm, height-22*mm, "♥")
    
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
        c.drawString(20*mm, y_pos, line)
        y_pos -= line_height
    
    # Bottom decoration
    heart_positions = [(width/2-20*mm, 15*mm), (width/2-10*mm, 18*mm), (width/2, 16*mm), 
                       (width/2+10*mm, 18*mm), (width/2+20*mm, 15*mm)]
    sizes = [14, 16, 18, 16, 14]
    draw_scattered_hearts(c, heart_positions, sizes)
    
    c.showPage()

def draw_wish_page(c, wish_num, codename, theme, icons, bg_color, qr_path):
    """Draw individual wish page with QR code and rich decorations"""
    c.setFillColor(CREAM)
    c.rect(0, 0, width, height, fill=1, stroke=0)
    
    # Background color wash
    c.setFillColor(bg_color)
    c.setFillAlpha(0.15)
    c.rect(0, 0, width, height, fill=1, stroke=0)
    c.setFillAlpha(1)
    
    # Decorative border
    draw_floral_border(c, 10*mm, 10*mm, width-20*mm, height-20*mm)
    
    # Corner decorations
    corners = [(18*mm, height-18*mm, 0), (width-18*mm, height-18*mm, 90),
               (18*mm, 18*mm, 270), (width-18*mm, 18*mm, 180)]
    for x, y, rot in corners:
        draw_decorative_corner(c, x, y, 12, rot)
    
    # Title area with decorative background
    title_bg_color = bg_color
    c.setFillColor(title_bg_color)
    c.setFillAlpha(0.3)
    c.roundRect(16*mm, height-36*mm, width-32*mm, 22*mm, 4*mm, fill=1, stroke=0)
    c.setFillAlpha(1)
    
    c.setStrokeColor(ROSE)
    c.setLineWidth(1.5)
    c.roundRect(16*mm, height-36*mm, width-32*mm, 22*mm, 4*mm, fill=0, stroke=1)
    
    # Title
    c.setFillColor(ROSE)
    c.setFont("Helvetica-Bold", 18)
    c.drawCentredString(width/2, height-23*mm, codename)
    
    c.setFillColor(WARM_BROWN)
    c.setFont("Helvetica", 10)
    c.drawCentredString(width/2, height-30*mm, f"Wish #{wish_num}")
    
    # Decorative icons around the page (8 icons positioned decoratively)
    icon_positions = [
        # Top area
        (25*mm, height-45*mm), (width/2-15*mm, height-42*mm), 
        (width/2+15*mm, height-42*mm), (width-25*mm, height-45*mm),
        # Bottom area
        (25*mm, 30*mm), (width/2-15*mm, 27*mm),
        (width/2+15*mm, 27*mm), (width-25*mm, 30*mm)
    ]
    
    for i, (x, y) in enumerate(icon_positions[:len(icons)]):
        draw_icon_with_background(c, x, y, icons[i], bg_color, 13)
    
    # Theme-specific decorative elements
    random.seed(int(wish_num))
    decoration_positions = [
        (30*mm, height/2+20*mm), (width-30*mm, height/2+20*mm),
        (30*mm, height/2-20*mm), (width-30*mm, height/2-20*mm),
        (width/2-25*mm, height/2+25*mm), (width/2+25*mm, height/2+25*mm),
        (width/2-25*mm, height/2-25*mm), (width/2+25*mm, height/2-25*mm)
    ]
    draw_themed_decorations(c, theme, decoration_positions)
    
    # QR Code in center with decorative frame
    qr_size = 45*mm
    qr_x = (width - qr_size) / 2
    qr_y = height/2 - qr_size/2
    
    # QR background with shadow
    c.setFillColor(HexColor('#FFFFFF'))
    c.roundRect(qr_x-3*mm, qr_y-3*mm, qr_size+6*mm, qr_size+6*mm, 3*mm, fill=1, stroke=0)
    
    # QR border
    c.setStrokeColor(ROSE)
    c.setLineWidth(2)
    c.roundRect(qr_x-3*mm, qr_y-3*mm, qr_size+6*mm, qr_size+6*mm, 3*mm, fill=0, stroke=1)
    
    # Inner decorative border
    c.setStrokeColor(GOLD)
    c.setLineWidth(1)
    c.roundRect(qr_x-2*mm, qr_y-2*mm, qr_size+4*mm, qr_size+4*mm, 2*mm, fill=0, stroke=1)
    
    # QR Code
    c.drawImage(qr_path, qr_x, qr_y, qr_size, qr_size, preserveAspectRatio=True, mask='auto')
    
    # Corner decorations around QR
    qr_corners = [
        (qr_x-6*mm, qr_y+qr_size+6*mm), (qr_x+qr_size+6*mm, qr_y+qr_size+6*mm),
        (qr_x-6*mm, qr_y-6*mm), (qr_x+qr_size+6*mm, qr_y-6*mm)
    ]
    c.setFillColor(GOLD)
    c.setFont("Helvetica", 10)
    for x, y in qr_corners:
        c.drawCentredString(x, y, "✦")
    
    # Instruction at bottom with decorative frame
    c.setFillColor(bg_color)
    c.setFillAlpha(0.3)
    c.roundRect(16*mm, 10*mm, width-32*mm, 12*mm, 3*mm, fill=1, stroke=0)
    c.setFillAlpha(1)
    
    c.setStrokeColor(ROSE)
    c.setLineWidth(1)
    c.roundRect(16*mm, 10*mm, width-32*mm, 12*mm, 3*mm, fill=0, stroke=1)
    
    c.setFillColor(WARM_BROWN)
    c.setFont("Helvetica-Oblique", 9)
    c.drawCentredString(width/2, 17*mm, "Scan the QR code with your phone")
    c.drawCentredString(width/2, 12*mm, "to unlock this wish! ✨")
    
    # Small decorative stars at bottom corners
    c.setFont("Helvetica", 8)
    c.setFillColor(GOLD)
    c.drawCentredString(20*mm, 16*mm, "✦")
    c.drawCentredString(width-20*mm, 16*mm, "✦")
    
    c.showPage()

def create_final_wish_book():
    pdf_path = "/home/claude/wish-book/Melus_33_Wishes_Book_FINAL.pdf"
    c = canvas.Canvas(pdf_path, pagesize=A5)
    
    print("Creating FINAL wish book PDF with QR codes and rich decorations...")
    print("  ✨ Actual QR codes (no dot-to-dot)")
    print("  🎨 Rich decorative elements on each page")
    print("  💝 Themed icons and colors")
    print("  📸 Ready to scan immediately")
    print()
    
    # Cover page
    print("  ✓ Drawing ornate cover page...")
    draw_cover_page(c)
    
    # Letter page
    print("  ✓ Drawing love letter page...")
    draw_letter_page(c)
    
    # Individual wish pages
    for wish in wishes_data:
        qr_path = f"/home/claude/wish-book/qr_codes/wish-{wish['num']}.png"
        
        print(f"  ✓ Wish {wish['num']}: {wish['codename']} - {len(wish['icons'])} icons, theme: {wish['theme']}")
        
        draw_wish_page(c, wish['num'], wish['codename'], wish['theme'], 
                      wish['icons'], wish['color'], qr_path)
    
    # Save PDF
    c.save()
    print(f"\n✨ FINAL wish book created successfully!")
    print(f"📁 Saved as: {pdf_path}")
    print(f"📄 Total pages: {len(wishes_data) + 2} (cover + letter + 33 wishes)")
    print(f"\n🎨 Features:")
    print(f"   • Actual QR codes ready to scan")
    print(f"   • 8 themed emoji icons per page")
    print(f"   • Rich decorative borders and flourishes")
    print(f"   • Color-coded by wish theme")
    print(f"   • Ornate corner decorations")
    print(f"   • Scrapbook aesthetic with beautiful layouts")
    
    return pdf_path

if __name__ == "__main__":
    create_final_wish_book()
