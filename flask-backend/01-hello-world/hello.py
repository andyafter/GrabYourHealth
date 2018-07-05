from flask import Flask
from flask import jsonify
from random import shuffle

app = Flask(__name__)

count = 0

@app.route('/')
def index():
    return "<h1>Hello, World!</h1>"

@app.route('/cards/')
def user():
    shuffle(cards)
    return jsonify(cards[0])   

@app.route('/quote/')
def profile():
    return "success"

@app.route('/count/')
def profile():
    count += 1
    return jsonify(count)


if __name__ == '__main__':
    app.run(debug=True)
    pass

cards = [
    {
        "title": "An Apple A Day Keeps The Doctor Away", 
        "imageUrl": "https://s.hswstatic.com/gif/apple-a-day-drl-668x375.jpg",
        "description": "The Cornell researchers suggest that a combination of plant chemicals, collectively known as phytochemicals, found mainly in the skin of apples, provide the bulk of the fruit's anticancer and antioxidant properties. The cooperative activity of these phytochemicals, they argue, has health benefits that are superior to those found in single compounds like vitamin C, vitamin E, and beta-carotene, which have been widely studied for their antioxidant activities.\n\nSo eat up!",
        "cta": "I had an apple today!", 
    }, 
    
    {
        "title": "Strong Bones",
        "imageUrl": "http://projectmecentral.com/wp-content/uploads/2015/02/calcium-and-bones.jpg", 
        "description": "Get your daily calcium by drinking milk or eating yoghurt. It’ll keep your bones strong. Remember that your bone density declines after the age of 30. You need at least 200 milligrams daily, which you should combine with magnesium, or it simply won't be absorbed.\n\n If you happen to be lactose intolerant, try other options like soy milk, coconut milk, almond milk, or rice milk!",
        "cta":"I have my glass of milk today!",
    },
    {
        "title": "Stretch It Out", 
        "imageUrl": "http://www.khabar.com/03_13-FitnessLifestyle.jpg?w=400", 
        "description": "When you stretch, ease your body into position until you feel the stretch and hold it for about 25 seconds. Breathe deeply to help your body move oxygen-rich blood to those sore muscles. Don't bounce or force yourself into an uncomfortable position.\n\nTry a 10-minute stretching routine after work today! Start from your head and work your way down to your neck, shoulders, arms, then end your stretching session at your ankles.", 
        "cta": "I did my stretching today!", 
    },
    {
        "title": "Let's not sugar coat this", 
        "imageUrl": "https://1.bp.blogspot.com/-b-6lP52rRl8/UvVaDn1GrmI/AAAAAAAAFXk/MOxOM7yy0_U/s1600/sugarlipsW.jpg", 
        "description": "More than 80% of type 2 diabetics die of heart disease, so make sure you control your glucose levels, and watch your blood pressure and cholesterol counts.\n\nHave an Americano instead of your usual latte for the day! (Kopi o kosong works too!)", 
        "cta": "I chose the sugar-free option today!", 
    }, 
    {
        "title": "Berry Belly", 
        "imageUrl":"https://data.whicdn.com/images/48786802/large.jpg", 
        "description": "Blueberries, strawberries and raspberries contain plant nutrients known as anthocyanidins, which are powerful antioxidants. Blueberries rival grapes in concentrations of resveratrol – the antioxidant compound found in red wine that has assumed near mythological proportions. Resveratrol is believed to help protect against heart disease and cancer.",
        "cta": "I had my berries today!",
        
    }, 
    {
        "title": "Sunscreen or smokescreen",
        "imageUrl": "https://www.greenandgrowing.org/wp-content/uploads/2017/07/sunscreen-sun-drawing.png",
        "description": "Sunscreen is unlikely to stop you from being sunburned, or to reduce your risk of developing skin cancer. That’s because most people don’t apply it properly, and stay in the sun too long. The solution? Slather on sunscreen daily and reapply it often, especially if you’ve been in the water. How much? At least enough to fill a shot glass.", 
        "cta": "I  applied sunscreen today!"
    }, 
    {
        "title": "Drink Up!", 
        "imageUrl": "https://imgix.bustle.com/rehost/2016/9/13/7cb35a7c-9942-437d-819a-1e2c53c4fa26.jpg", 
        "description": "Drinking enough water can improve your mood, make your skin glow and keep you regular. Staying hydrated also plays a role in appetite suppression and weight management.\n\nHave at least 8 glasses of water today.",
        "cta": "I had 8 glasses of water today!",        
    }
]
