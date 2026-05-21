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

wishes_data = [
    {"num": "01", "codename": "Slow Sunday", "theme": "relax"},
    {"num": "02", "codename": "Butter Toast", "theme": "food"},
    {"num": "03", "codename": "Afterglow", "theme": "romance"},
    {"num": "04", "codename": "Cloud Nine", "theme": "relax"},
    {"num": "05", "codename": "Vanilla Sky", "theme": "romance"},
    {"num": "06", "codename": "Pillow Fort", "theme": "fun"},
    {"num": "07", "codename": "Velvet", "theme": "food"},
    {"num": "08", "codename": "Polaroid", "theme": "adventure"},
    {"num": "09", "codename": "Gold Rush", "theme": "fun"},
    {"num": "10", "codename": "Crown", "theme": "romance"},
    {"num": "11", "codename": "Mirage", "theme": "adventure"},
    {"num": "12", "codename": "Firefly", "theme": "fun"},
    {"num": "13", "codename": "Passport", "theme": "adventure"},
    {"num": "14", "codename": "Detour", "theme": "adventure"},
    {"num": "15", "codename": "Compass", "theme": "romance"},
    {"num": "16", "codename": "Lantern", "theme": "romance"},
    {"num": "17", "codename": "Matchbox", "theme": "fun"},
    {"num": "18", "codename": "Side Quest", "theme": "fun"},
    {"num": "19", "codename": "Red Lantern", "theme": "food"},
    {"num": "20", "codename": "Spice Route", "theme": "food"},
    {"num": "21", "codename": "Midnight Snack", "theme": "food"},
    {"num": "22", "codename": "Barrel Room", "theme": "fun"},
    {"num": "23", "codename": "Takeout", "theme": "food"},
    {"num": "24", "codename": "Cherry Pop", "theme": "food"},
    {"num": "25", "codename": "Moonlight", "theme": "romance"},
    {"num": "26", "codename": "Time Capsule", "theme": "romance"},
    {"num": "27", "codename": "Open Book", "theme": "romance"},
    {"num": "28", "codename": "Blueprint", "theme": "romance"},
    {"num": "29", "codename": "Ink", "theme": "romance"},
    {"num": "30", "codename": "Anchor", "theme": "romance"},
    {"num": "31", "codename": "White Flag", "theme": "fun"},
    {"num": "32", "codename": "Vinyl", "theme": "fun"},
    {"num": "33", "codename": "Stardust", "theme": "romance"}
]

def draw_doodle_heart(c, x, y, size=5):
    """Draw a simple heart doodle"""
    c.setStrokeColor(ROSE)
    c.setLineWidth(1)
    # Simple heart shape
    c.bezier(x, y, x-size, y+size, x-size, y+size*1.5, x, y+size*2)
    c.bezier(x, y, x+size, y+size, x+size, y+size*1.5, x, y+size*2)

def draw_doodle_star(c, x, y, size=4):
    """Draw a simple star doodle"""
    c.setStrokeColor(GOLD)
    c.setLineWidth(1)
    # 5-pointed star
    points = []
    for i in range(10):
        angle = (i * 36 - 90) * (3.14159 / 180)
        r = size if i % 2 == 0 else size / 2
        points.append((x + r * math.cos(angle), y + r * math.sin(angle)))
    
    path = c.beginPath()
    path.moveTo(points[0][0], points[0][1])
    for px, py in points[1:]:
        path.lineTo(px, py)
    path.close()
    c.drawPath(path)

def draw_doodle_flower(c, x, y, size=5):
    """Draw a simple flower doodle"""
    c.setStrokeColor(SOFT_PINK)
    c.setFillColor(SOFT_PINK)
    c.setLineWidth(1)
    # Petals
    for i in range(6):
        angle = i * 60 * (3.14159 / 180)
        px = x + size * math.cos(angle)
        py = y + size * math.sin(angle)
        c.circle(px, py, size/2, fill=1)
    # Center
    c.circle(x, y, size/2.5, fill=1)

def draw_food_doodles(c, positions):
    """Draw food-themed doodles"""
    for x, y in positions:
        choice = random.choice(['bowl', 'cup', 'utensil'])
        c.setStrokeColor(ROSE)
        c.setLineWidth(1.5)
        if choice == 'bowl':
            c.arc(x-5, y-5, x+5, y+5, 0, 180)
        elif choice == 'cup':
            c.rect(x-3, y, 6, 8)
            c.line(x+3, y+2, x+7, y+2)
        else:
            c.line(x, y, x, y+10)

def draw_adventure_doodles(c, positions):
    """Draw adventure-themed doodles"""
    for x, y in positions:
        choice = random.choice(['mountain', 'compass', 'path'])
        c.setStrokeColor(WARM_BROWN)
        c.setLineWidth(1.5)
        if choice == 'mountain':
            c.line(x-6, y, x, y+8)
            c.line(x, y+8, x+6, y)
        elif choice == 'compass':
            c.circle(x, y, 4)
            c.line(x, y-4, x, y+4)
            c.line(x-4, y, x+4, y)
        else:
            c.setDash(2, 2)
            c.line(x-5, y, x+5, y+3)
            c.setDash()

def draw_romance_doodles(c, positions):
    """Draw romance-themed doodles"""
    for x, y in positions[:3]:
        draw_doodle_heart(c, x, y, 4)
    for x, y in positions[3:]:
        draw_doodle_star(c, x, y, 3)

def draw_fun_doodles(c, positions):
    """Draw fun-themed doodles"""
    for i, (x, y) in enumerate(positions):
        if i % 2 == 0:
            draw_doodle_star(c, x, y, 3)
        else:
            # Spiral
            c.setStrokeColor(SOFT_PINK)
            c.setLineWidth(1)
            path = c.beginPath()
            for t in range(0, 360, 10):
                angle = t * (3.14159 / 180)
                r = t / 60
                px = x + r * math.cos(angle)
                py = y + r * math.sin(angle)
                if t == 0:
                    path.moveTo(px, py)
                else:
                    path.lineTo(px, py)
            c.drawPath(path)

def draw_relax_doodles(c, positions):
    """Draw relaxation-themed doodles"""
    for x, y in positions:
        choice = random.choice(['cloud', 'wave'])
        c.setStrokeColor(SOFT_PINK)
        c.setLineWidth(1.5)
        if choice == 'cloud':
            c.circle(x-3, y, 3)
            c.circle(x, y+2, 3)
            c.circle(x+3, y, 3)
        else:
            # Wave
            path = c.beginPath()
            path.moveTo(x-5, y)
            path.curveTo(x-3, y+3, x-1, y+3, x+1, y)
            path.curveTo(x+3, y-3, x+5, y-3, x+7, y)
            c.drawPath(path)

def convert_qr_to_dots(qr_image_path, num_dots='medium'):
    """Convert QR code to dot-to-dot coordinates"""
    img = Image.open(qr_image_path).convert('L')
    
    # Determine sampling based on complexity
    if num_dots == 'simple':
        sample_rate = 8  # Less dots
    else:  # medium
        sample_rate = 5  # More dots
    
    dots = []
    dot_number = 1
    
    # Sample the QR code at regular intervals
    for y in range(0, img.height, sample_rate):
        for x in range(0, img.width, sample_rate):
            if img.getpixel((x, y)) < 128:  # Black pixel
                dots.append((x, y, dot_number))
                dot_number += 1
    
    return dots, img.size

def draw_cover_page(c):
    """Draw the beautiful cover page with the love letter"""
    c.setFillColor(CREAM)
    c.rect(0, 0, width, height, fill=1, stroke=0)
    
    # Decorative border
    c.setStrokeColor(ROSE)
    c.setLineWidth(2)
    c.rect(15*mm, 15*mm, width-30*mm, height-30*mm)
    
    # Corner decorations
    corners = [(20*mm, height-20*mm), (width-20*mm, height-20*mm), 
               (20*mm, 20*mm), (width-20*mm, 20*mm)]
    for x, y in corners:
        draw_doodle_heart(c, x, y, 6)
    
    # Title
    c.setFillColor(ROSE)
    c.setFont("Helvetica-Bold", 24)
    c.drawCentredString(width/2, height-40*mm, "33 Wishes")
    
    c.setFont("Helvetica", 16)
    c.drawCentredString(width/2, height-50*mm, "for Melu")
    
    # Decorative line
    c.setStrokeColor(GOLD)
    c.setLineWidth(1)
    c.line(30*mm, height-55*mm, width-30*mm, height-55*mm)
    
    # Add small stars
    for i in range(5):
        x = 25*mm + i * 20*mm
        draw_doodle_star(c, x, height-60*mm, 3)
    
    c.showPage()

def draw_letter_page(c):
    """Draw the love letter page"""
    c.setFillColor(CREAM)
    c.rect(0, 0, width, height, fill=1, stroke=0)
    
    # Decorative corner hearts
    draw_doodle_heart(c, 20*mm, height-20*mm, 5)
    draw_doodle_heart(c, width-20*mm, height-20*mm, 5)
    
    # Letter content
    c.setFillColor(WARM_BROWN)
    c.setFont("Helvetica", 11)
    
    y_pos = height - 35*mm
    line_height = 5*mm
    
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
        c.drawString(25*mm, y_pos, line)
        y_pos -= line_height
    
    # Bottom decoration
    for i in range(3):
        x = width/2 - 15*mm + i * 15*mm
        draw_doodle_flower(c, x, 15*mm, 4)
    
    c.showPage()

def draw_wish_page(c, wish_num, codename, theme, qr_dots, qr_size, complexity):
    """Draw individual wish page with dot-to-dot QR code"""
    c.setFillColor(CREAM)
    c.rect(0, 0, width, height, fill=1, stroke=0)
    
    # Title
    c.setFillColor(ROSE)
    c.setFont("Helvetica-Bold", 18)
    c.drawCentredString(width/2, height-25*mm, codename)
    
    c.setFillColor(WARM_BROWN)
    c.setFont("Helvetica", 10)
    c.drawCentredString(width/2, height-30*mm, f"Wish #{wish_num}")
    
    # Draw themed doodles around the page
    random.seed(int(wish_num))  # Consistent positions per wish
    
    # Generate positions for doodles (avoiding center QR area)
    doodle_positions = []
    for _ in range(6):
        x = random.randint(int(20*mm), int(width-20*mm))
        y_top = random.randint(int(height-40*mm), int(height-15*mm))
        y_bottom = random.randint(int(15*mm), int(35*mm))
        
        if len(doodle_positions) < 3:
            doodle_positions.append((x, y_top))
        else:
            doodle_positions.append((x, y_bottom))
    
    # Draw theme-specific doodles
    if theme == 'food':
        draw_food_doodles(c, doodle_positions)
    elif theme == 'adventure':
        draw_adventure_doodles(c, doodle_positions)
    elif theme == 'romance':
        draw_romance_doodles(c, doodle_positions)
    elif theme == 'fun':
        draw_fun_doodles(c, doodle_positions)
    elif theme == 'relax':
        draw_relax_doodles(c, doodle_positions)
    
    # Draw dot-to-dot QR code in center
    qr_center_x = width / 2
    qr_center_y = height / 2
    qr_scale = 60 / qr_size[0]  # Scale to about 60mm wide
    
    c.setFillColor(WARM_BROWN)
    c.setFont("Helvetica", 6)
    
    for x, y, num in qr_dots:
        # Scale and position
        dot_x = qr_center_x + (x - qr_size[0]/2) * qr_scale
        dot_y = qr_center_y + (y - qr_size[1]/2) * qr_scale
        
        # Draw dot
        c.circle(dot_x, dot_y, 0.8, fill=1)
        
        # Draw number next to dot
        c.drawString(dot_x + 2, dot_y - 1.5, str(num))
    
    # Instruction at bottom
    c.setFillColor(WARM_BROWN)
    c.setFont("Helvetica-Oblique", 9)
    c.drawCentredString(width/2, 10*mm, 
        "Connect the dots in order, then scan the QR code to reveal your wish!")
    
    c.showPage()

# Generate the PDF
def create_wish_book():
    pdf_path = "/home/claude/wish-book/Melus_33_Wishes_Book.pdf"
    c = canvas.Canvas(pdf_path, pagesize=A5)
    
    print("Creating wish book PDF...")
    
    # Cover page
    print("  ✓ Drawing cover page...")
    draw_cover_page(c)
    
    # Letter page
    print("  ✓ Drawing love letter page...")
    draw_letter_page(c)
    
    # Individual wish pages
    for i, wish in enumerate(wishes_data, 1):
        qr_path = f"/home/claude/wish-book/qr_codes/wish-{wish['num']}.png"
        
        # Alternate complexity
        complexity = 'simple' if i % 3 == 0 else 'medium'
        
        dots, qr_size = convert_qr_to_dots(qr_path, complexity)
        
        print(f"  ✓ Drawing wish page {wish['num']}: {wish['codename']} ({len(dots)} dots)")
        
        draw_wish_page(c, wish['num'], wish['codename'], wish['theme'], 
                      dots, qr_size, complexity)
    
    # Save PDF
    c.save()
    print(f"\n✨ Wish book created successfully!")
    print(f"📁 Saved as: {pdf_path}")
    print(f"📄 Total pages: {len(wishes_data) + 2} (cover + letter + 33 wishes)")
    
    return pdf_path

if __name__ == "__main__":
    create_wish_book()
