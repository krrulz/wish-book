#!/usr/bin/env python3
import os

wishes = [
    {
        "num": "01", "codename": "Slow Sunday", "title": "Lazy Guilt-Free Day Together",
        "description": "Remember those Sundays where we just... exist? No plans, no rushing, just us in our pajamas doing absolutely nothing and everything at the same time. This is that day, officially guilt-free.",
        "rules": [
            "📅 Pick any day (preferably a weekend)",
            "🛏️ Stay in pajamas all day if you want",
            "📱 No obligations, no plans, just pure lazy bliss",
            "🍕 Order in whatever you're craving",
            "💤 Naps are mandatory, productivity is banned"
        ]
    },
    {
        "num": "02", "codename": "Butter Toast", "title": "Breakfast in Bed",
        "description": "You know what's better than breakfast? Breakfast that magically appears while you're still cozy under the covers. Your favorite things on a tray, made with love, served with extra kisses.",
        "rules": [
            "☕ Any morning you choose",
            "🍳 Your favorite breakfast items",
            "📰 I handle everything, you just relax",
            "🛏️ Eat in bed, no guilt allowed",
            "💝 Made with love and probably some burnt toast attempts"
        ]
    },
    {
        "num": "03", "codename": "Afterglow", "title": "One Slow Romantic Evening",
        "description": "Candles, soft music, no distractions. Just you and me, lost in our own little world. The kind of evening where time slows down and nothing else matters.",
        "rules": [
            "🕯️ Candles, music, the whole ambiance",
            "📵 Phones away, just us",
            "🍷 Wine or your drink of choice",
            "💑 Slow dancing in the living room included",
            "⏰ No rush, just being present together"
        ]
    },
    {
        "num": "04", "codename": "Cloud Nine", "title": "Soft Life Day",
        "description": "A whole day where you don't lift a finger. Everything is taken care of, every need anticipated, every comfort provided. You just float through the day being pampered.",
        "rules": [
            "👑 You're the queen for the entire day",
            "🧹 All chores handled by me",
            "🍽️ Meals, snacks, drinks - all served",
            "💆‍♀️ Want a foot rub? Done. Head massage? You got it.",
            "✨ Your only job is to relax and enjoy"
        ]
    },
    {
        "num": "05", "codename": "Vanilla Sky", "title": "Coffee & Flowers Delivery",
        "description": "Imagine this: you're having a regular day, and suddenly there's a knock. Fresh flowers and your favorite coffee, delivered just because. No reason needed.",
        "rules": [
            "☕ Your favorite coffee/beverage",
            "💐 Fresh flowers delivered",
            "📍 At home or your workplace",
            "🎁 Surprise timing (you won't know when)",
            "💌 With a little love note from me"
        ]
    },
    {
        "num": "06", "codename": "Pillow Fort", "title": "Home Luxury Movie Night",
        "description": "We're turning our living room into a 5-star cinema. Projector, blankets, pillows everywhere, your favorite snacks, and whatever movie marathon your heart desires.",
        "rules": [
            "🎬 Your choice of movies (even the cheesy ones)",
            "🍿 Unlimited snacks and treats",
            "🛋️ Cozy setup with blankets and pillows",
            "🎭 No interruptions, phones on silent",
            "🌙 Can go as late as you want"
        ]
    },
    {
        "num": "07", "codename": "Velvet", "title": "Fancy Dinner Anywhere",
        "description": "That restaurant you've been wanting to try? The fancy one you saved on Instagram? Consider it done. Get dressed up, we're having a proper date night.",
        "rules": [
            "🍽️ Any restaurant you choose",
            "👗 Dress up and feel fancy",
            "💳 Budget: No limits on this one",
            "🚗 I'll handle reservations and transport",
            "📸 Instagram-worthy meal guaranteed"
        ]
    },
    {
        "num": "08", "codename": "Polaroid", "title": "Aesthetic Café Hopping Day",
        "description": "Let's spend a whole day discovering the cutest, most Instagram-worthy cafés. Multiple stops, lots of coffee, even more photos, and zero rush.",
        "rules": [
            "☕ Visit 3-4 aesthetic cafés in one day",
            "📸 I'm your personal photographer",
            "🍰 Try whatever looks good",
            "🗺️ I plan the route, you just enjoy",
            "⏰ No time limits, explore at your pace"
        ]
    },
    {
        "num": "09", "codename": "Gold Rush", "title": "Shopping Surprise",
        "description": "₹10,000 to spend however you want. Clothes, accessories, books, home décor - whatever makes your heart happy. And yes, I'll carry all the bags.",
        "rules": [
            "💰 ₹10,000 shopping budget",
            "🛍️ Any store(s) you choose",
            "👜 I'm the designated bag carrier",
            "⏰ Take your time, no rushing",
            "💳 My treat, your choices"
        ]
    },
    {
        "num": "10", "codename": "Crown", "title": "Princess Treatment Day",
        "description": "From the moment you wake up to when you sleep, you're treated like absolute royalty. Every wish, every whim, every request - granted immediately.",
        "rules": [
            "👑 24 hours of princess treatment",
            "🧞‍♂️ Your wish is my command",
            "🚪 Doors opened, chairs pulled, the works",
            "💝 Compliments and affection all day",
            "✨ No request too small or too silly"
        ]
    },
    {
        "num": "11", "codename": "Mirage", "title": "Surprise Date Night",
        "description": "You show up, I handle everything else. Where we're going? What we're doing? That's a surprise. Just trust me and enjoy the adventure.",
        "rules": [
            "🎭 Location and activity: surprise!",
            "👗 I'll give you a dress code hint",
            "🚗 I plan everything, you just show up",
            "📅 Pick a date, I handle the rest",
            "🎁 Guaranteed to be memorable"
        ]
    },
    {
        "num": "12", "codename": "Firefly", "title": "Instagram Husband for a Day",
        "description": "An entire day dedicated to getting you those perfect Instagram shots. I'll take 100 photos until we get THE one. Patient photographer mode: activated.",
        "rules": [
            "📸 Unlimited photo attempts",
            "📍 Any location(s) you want",
            "👗 Multiple outfit changes allowed",
            "😊 Patient photographer guaranteed",
            "✨ We don't leave until you're happy with the shots"
        ]
    },
    {
        "num": "13", "codename": "Passport", "title": "Weekend Getaway Wish",
        "description": "Pack your bags, Melu. We're escaping for 2-3 days. Beach, hills, that Insta-famous place you've been eyeing - your choice. Adventure awaits.",
        "rules": [
            "✈️ 2-3 days trip to your chosen destination",
            "💰 Budget: ₹15,000 - ₹30,000",
            "🏨 Comfortable stay included",
            "📸 Aesthetic locations guaranteed",
            "🗓️ Plan it when suits you best"
        ]
    },
    {
        "num": "14", "codename": "Detour", "title": "Spontaneous Road Trip",
        "description": "No fixed destination, just pick a direction and drive. Stop wherever looks interesting, eat at roadside dhabas, take weird detours, get lost together.",
        "rules": [
            "🚗 Start driving, see where we end up",
            "🗺️ No rigid plans, just vibes",
            "🍽️ Stop anywhere that looks good",
            "📸 Photo stops whenever you want",
            "⛽ Full tank and snacks loaded"
        ]
    },
    {
        "num": "15", "codename": "Compass", "title": "Mystery Date Voucher",
        "description": "I plan an entire date based on your mood that day. Tell me how you're feeling, and I'll create the perfect evening around it.",
        "rules": [
            "🎭 I plan based on your mood",
            "📅 Flexible timing, your call",
            "🎨 Could be adventurous, cozy, or fancy",
            "💝 Tailored completely to what you need",
            "🎁 Trust me, it'll be perfect"
        ]
    },
    {
        "num": "16", "codename": "Lantern", "title": "Golden Hour Date",
        "description": "We chase the sunset together. Find the perfect spot, watch the sky turn gold, capture those dreamy photos, and just soak in the moment.",
        "rules": [
            "🌅 Sunset timing (obviously)",
            "📸 Bring the camera for golden hour magic",
            "🍷 Drinks and snacks included",
            "📍 Scenic location scouted by me",
            "💑 Just us and the golden sky"
        ]
    },
    {
        "num": "17", "codename": "Matchbox", "title": "Try Something New Together",
        "description": "That thing we've talked about trying but never did? Let's do it. Cooking class, pottery, dance lesson, adventure sport - you pick, we try.",
        "rules": [
            "🎨 Your choice of new activity",
            "👥 We do it together",
            "💰 Budget: ₹3,000 - ₹8,000",
            "📅 Weekend activity preferably",
            "😄 It's okay to be terrible at it together"
        ]
    },
    {
        "num": "18", "codename": "Side Quest", "title": "One Full 'Yes Day'",
        "description": "For one entire day, I say yes to everything (within reason). Want ice cream for breakfast? Yes. Sudden park visit? Yes. Impromptu shopping? Yes.",
        "rules": [
            "✅ I say 'yes' to all requests for 24 hours",
            "💰 Reasonable budget limits apply",
            "🚫 Must be legal and safe (obviously)",
            "⏰ From morning to bedtime",
            "🎉 Let your spontaneous side run wild"
        ]
    },
    {
        "num": "19", "codename": "Red Lantern", "title": "Chinese Food Craving Pass",
        "description": "That Chinese food craving at 9 PM? Or 2 PM? Or midnight? Consider it handled. Order whatever you want, whenever you want.",
        "rules": [
            "🥡 Any Chinese food you're craving",
            "⏰ Any time of day (yes, even 2 AM)",
            "💰 No budget limit for this meal",
            "🚗 Delivery or dine-in, your choice",
            "🍜 Extra spring rolls? Always."
        ]
    },
    {
        "num": "20", "codename": "Spice Route", "title": "Indian Feast Date",
        "description": "Let's go all out with an Indian food adventure. That place with the amazing biryani? The one with the authentic thali? Or multiple places? You decide.",
        "rules": [
            "🍛 Indian cuisine of your choice",
            "🍽️ Dine-in at a nice restaurant",
            "💰 Order without looking at prices",
            "🥘 Multiple dishes to share and try",
            "📸 Food photography allowed (and encouraged)"
        ]
    },
    {
        "num": "21", "codename": "Midnight Snack", "title": "Dessert Run at Any Hour",
        "description": "2 AM ice cream craving? Sudden need for chocolate cake at 11 PM? Say the word, and we're driving out to get it.",
        "rules": [
            "🍰 Any dessert, any time",
            "🚗 Late night drives included",
            "🕐 Yes, even at weird hours",
            "💝 No judgment, just dessert",
            "🍨 Multiple items allowed"
        ]
    },
    {
        "num": "22", "codename": "Barrel Room", "title": "Beer/Whiskey Date Night",
        "description": "Let's explore that craft beer place or try those whiskeys you've been curious about. A proper tasting evening with good drinks and great company.",
        "rules": [
            "🍺 Beer/whiskey tasting at a nice place",
            "🌃 Evening plans, good ambiance",
            "🍽️ Appetizers and food included",
            "💰 Budget: ₹4,000 - ₹6,000",
            "🚗 Safe ride home guaranteed"
        ]
    },
    {
        "num": "23", "codename": "Takeout", "title": "Your Food Wish is My Command",
        "description": "One meal where you order EVERYTHING you've been wanting to try. That expensive sushi? Get it. Thai curry AND pizza? Why not. Go wild.",
        "rules": [
            "🍽️ Order from multiple restaurants if you want",
            "💰 No budget restrictions for this meal",
            "🥡 Takeout or delivery, your choice",
            "😋 Try everything you've been craving",
            "🎉 Zero judgment on quantity"
        ]
    },
    {
        "num": "24", "codename": "Cherry Pop", "title": "Surprise Sweet Treat",
        "description": "Random surprises are the best, right? Expect a sweet delivery - could be your favorite dessert, chocolates, or that pastry you love.",
        "rules": [
            "🍰 Surprise sweet treat delivered",
            "❓ You won't know when it's coming",
            "📍 At home or work",
            "💝 Just because you're you",
            "🎁 Sweetness guaranteed"
        ]
    },
    {
        "num": "25", "codename": "Moonlight", "title": "Dance with Me Anywhere",
        "description": "Slow dance in the living room, silly dancing in the kitchen, or an actual dance date - let's move together, even if we're terrible at it.",
        "rules": [
            "💃 Dance anywhere you want",
            "🎵 Your playlist choice",
            "🏠 Could be at home or out",
            "😊 No skills required, just fun",
            "💕 It's about being close, not perfect"
        ]
    },
    {
        "num": "26", "codename": "Time Capsule", "title": "Memory Lane Evening",
        "description": "Let's revisit our story. Old photos, places we went on early dates, remember all those moments that got us here. Bring tissues, this might get emotional.",
        "rules": [
            "📸 Go through old photos together",
            "🗺️ Visit significant places from our past",
            "💭 Share favorite memories",
            "🍷 With wine/drinks and snacks",
            "💝 Relive our love story"
        ]
    },
    {
        "num": "27", "codename": "Open Book", "title": "Ask Me Anything Night",
        "description": "One evening where you can ask me absolutely anything - deep questions, silly ones, random curiosities - and I'll answer honestly.",
        "rules": [
            "❓ Ask me anything at all",
            "💬 Complete honesty guaranteed",
            "🍷 Best done with drinks",
            "⏰ No time limit on conversations",
            "💝 Vulnerability and connection time"
        ]
    },
    {
        "num": "28", "codename": "Blueprint", "title": "Future Dreams Date",
        "description": "Let's talk about our future. Where we want to go, what we want to do, dreams we have together. Planning our adventure ahead.",
        "rules": [
            "☕ Cozy setting, cafe or home",
            "💭 Dream big together",
            "📝 Can write/plan if you want",
            "🗺️ Talk about travel, life, everything",
            "💑 Building our future together"
        ]
    },
    {
        "num": "29", "codename": "Ink", "title": "Handwritten Love Letter",
        "description": "In this digital age, a real letter. Pen, paper, my handwriting (as messy as it is), pouring out everything I feel about you.",
        "rules": [
            "✍️ Handwritten by me",
            "💌 Delivered in person or hidden for you to find",
            "📜 Proper letter, not a note",
            "💝 From the heart",
            "🎁 Keep it forever"
        ]
    },
    {
        "num": "30", "codename": "Anchor", "title": "'Tell Me What You Need' Pass",
        "description": "Sometimes you need something but don't want to ask. This is your free pass. Tell me what you need - support, space, help, company - and I'm there.",
        "rules": [
            "💬 Tell me exactly what you need",
            "🤝 Could be practical help or emotional support",
            "⏰ Use anytime you're struggling",
            "💝 No explanations needed",
            "🫂 I'm here for whatever you need"
        ]
    },
    {
        "num": "31", "codename": "White Flag", "title": "You Win This Argument Pass",
        "description": "One get-out-of-argument-free card. Even if I think I'm right, you play this, and I concede. Peace is better than being right anyway.",
        "rules": [
            "🏳️ Use during any disagreement",
            "✅ I immediately agree with you",
            "😊 No sulking allowed (from me)",
            "💝 Instant peace restored",
            "⚠️ Use wisely (it's powerful)"
        ]
    },
    {
        "num": "32", "codename": "Vinyl", "title": "Control the Playlist All Day",
        "description": "From morning to night, the music is all yours. Even if it's the same song on repeat. Even if it's that album I don't love. Your soundtrack, your day.",
        "rules": [
            "🎵 Your music choices all day",
            "🔊 Car, home, everywhere",
            "🔁 Repeats allowed",
            "😊 No complaints from me",
            "💝 24 hours of your soundtrack"
        ]
    },
    {
        "num": "33", "codename": "Stardust", "title": "Secret Surprise Wish",
        "description": "The wildcard. Something I've been planning, something special, something that's just for you. You'll have to activate it to find out.",
        "rules": [
            "🎁 It's a complete surprise",
            "✨ Could be anything amazing",
            "💰 Budget: not telling",
            "📅 Timing: when it's perfect",
            "💝 Trust me, you'll love it"
        ]
    }
]

template = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Wish #{num} - {codename}</title>
    <link rel="stylesheet" href="../assets/style.css">
</head>
<body>
    <div class="container">
        <div class="content">
            <div class="codename">{codename}</div>
            <h1 class="wish-title">{title}</h1>
            
            <p class="wish-description">
                {description}
            </p>
            
            <div class="rules">
                <h3>How it works:</h3>
                {rules_html}
            </div>
            
            <p class="wish-description">
                <span class="heart">♥</span> One of 33 ways to say I love you <span class="heart">♥</span>
            </p>
            
            <a href="{whatsapp_link}" class="activate-btn">Activate This Wish ✨</a>
            
            <p class="footer">With all my love, Karthik 💕</p>
        </div>
    </div>
</body>
</html>'''

for wish in wishes:
    rules_html = '\n                '.join([f'<p>{rule}</p>' for rule in wish['rules']])
    
    # Create WhatsApp message
    wa_message = f"Hey Karthik! 💝 I'm activating Wish #{wish['num']} - {wish['codename']}! {wish['title']}!"
    wa_link = f"https://wa.me/32465227583?text={wa_message.replace(' ', '%20').replace('!', '%21').replace('#', '%23').replace("'", '%27')}"
    
    html_content = template.format(
        num=wish['num'],
        codename=wish['codename'],
        title=wish['title'],
        description=wish['description'],
        rules_html=rules_html,
        whatsapp_link=wa_link
    )
    
    filename = f"/home/claude/wish-book/wishes/{wish['num']}-{wish['codename'].lower().replace(' ', '-')}.html"
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    print(f"✓ Created {filename}")

print(f"\n✨ All 33 wish pages created successfully!")
