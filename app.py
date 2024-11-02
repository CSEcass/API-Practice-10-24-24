from flask import Flask, render_template, jsonify
import requests
import random
import json

app = Flask(__name__)
@app.route('/')
def Startup():
    return render_template('start.html', )
@app.route('/<name>/<day>')
def home_page(name, day):
    if name == "home":
        return render_template('index.html', day=day)
    elif name == "secret":
        return "Hi :D, today is " + day
    else:
        return "The Page You Are Looking For, Does Not Exist. Today is " + day + "."
    
# @app.route('/<num>')
    def num_page(num):
        num = int(num)
        if num > 10:
            return "The number " + str(num) + " is greater than 10."
        elif num < 10:
            return "The number " + str(num) + " is less than 10."
        elif num == 10:
            return "The number " + str(num) + " is equal to 10."

@app.route('/cat')
def cat_api():
    res = requests.get('https://api.thecatapi.com/v1/images/search?limit=10')
    data = res.json()
    return render_template('cat.html', data=data)

# idea: My API will display different art themes or color palletes
@app.route('/api', methods=['GET'])
def art_api():
    art_theme_dict = [{'name': 'Abstract', 'img_url': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQWZKSiGyNRFKmhIeO42KslgVTVVg4ExsJDKw&s'},
                 {'name': 'Society and Politics', 'img_url': 'https://d16kd6gzalkogb.cloudfront.net/magazine_images/Diego-Rivera-Man-at-the-Crossroads-1934-detail.jpg'},
                 {'name': 'Death and Mortality', 'img_url': 'https://breakingbreadtheology.com/wp-content/uploads/2023/01/memento-mori-1.jpg?w=1568'},
                 {'name': 'Time', 'img_url': 'https://cdn.shopify.com/s/files/1/0377/1226/5354/articles/A-2.-Gazhur-A.-ZHivoe-vremya-305h253.jpg?v=1705768603'},
                 {'name': 'Portrait', 'img_url': 'https://i.pinimg.com/236x/81/69/31/8169312bf4380dcb25db274e67b51508.jpg'}]
    art_palette_dict = [{'color1': '#383D3B', 'color2': '#EEE5E9', 'color3': '#7C7C7C'},
                   {'color1': '#ACBEA3', 'color2': '#40476D', 'color3': '#826754'},
                   {'color2': '#A41623', 'color2': '#F85E00', 'color3': '#FFB563'},
                   {'color3': '#3A0CA3', 'color2': '#4361EE', 'color3': '#4CC9F0'},]
    art_theme = random.choice(art_theme_dict)
    print(art_theme)
    art_palette = random.choice(art_palette_dict)
    art_dict = {'art_theme': art_theme, 'art_pallete': art_palette}
    print(art_dict)
    return jsonify(art_dict)

@app.route('/my')
def art_api_request():
    return render_template('mypswd.html')

@app.route('/my/<name>')
def art_api_get(name):
    # API VV
    art_theme_dict = [{'name': 'Abstract', 'img_url': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQWZKSiGyNRFKmhIeO42KslgVTVVg4ExsJDKw&s'},
        {'name': 'Society and Politics', 'img_url': 'https://d16kd6gzalkogb.cloudfront.net/magazine_images/Diego-Rivera-Man-at-the-Crossroads-1934-detail.jpg'},
        {'name': 'Death and Mortality', 'img_url': 'https://breakingbreadtheology.com/wp-content/uploads/2023/01/memento-mori-1.jpg?w=1568'},
        {'name': 'Time', 'img_url': 'https://cdn.shopify.com/s/files/1/0377/1226/5354/articles/A-2.-Gazhur-A.-ZHivoe-vremya-305h253.jpg?v=1705768603'},
        {'name': 'Portrait', 'img_url': 'https://i.pinimg.com/236x/81/69/31/8169312bf4380dcb25db274e67b51508.jpg'}]
    art_palette_dict = [{'color1': '#383D3B', 'color2': '#EEE5E9', 'color3': '#7C7C7C'},
        {'color1': '#ACBEA3', 'color2': '#40476D', 'color3': '#826754'},
        {'color1': '#A41623', 'color2': '#F85E00', 'color3': '#FFB563'},
        {'color1': '#3A0CA3', 'color2': '#4361EE', 'color3': '#4CC9F0'},]
    art_theme = random.choice(art_theme_dict)
    print(art_theme)
    
    # special page VV
    if name == 'cassidy':
        return render_template('cass.html', name=name)
    # name part VV
    coloredName = {}
    for i in name:
        art_palette = random.choice(art_palette_dict)
        coloredName[i] = art_palette['color' + str(random.randint(1, 3))]
    print(coloredName)
    return render_template('my.html', art_theme=art_theme, art_palette=art_palette, name=name, coloredName=coloredName)

app.run(host='0.0.0.0', port=8080)