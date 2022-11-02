from flask import Flask
import random

app = Flask(__name__)

@app.route('/')
def homepage():
    return '<h1>Guess a number between 0 and 9</h1>' \
           '<img src=https://media0.giphy.com/media/Y6PTZZsQyTghjeNU7D/200w.webp?cid=ecf05e478cepbqejvrd85g0ncvozcoogfcbjibpngc7udi5e&rid=200w.webp&ct=g width=600>'


random_number = random.randint(0, 10)
print(random_number)


@app.route('/<int:input_number>')
def check_number(input_number):
    if input_number < random_number:
        return '<h1 style="color: red"> Too low</h1>' \
               '<img src= "https://media3.giphy.com/media/Vgfj6Ovp3AqMvn4j5J/giphy.webp?cid=ecf05e4748w7uts6pyj4kehaduwl7dyhlvzqvnildqit123f&rid=giphy.webp&ct=g">'
    if input_number > random_number:
        return '<h1 style="color: red"> Too high <h1/>' \
               '<img src="https://media1.giphy.com/media/KAx8nhFtGmu1W/giphy.webp?cid=ecf05e47y16c0hgsemvyz2m5zky0al57b5sovvi9vlmcgkuf&rid=giphy.webp&ct=g">'
    else:
        return '<h1 style ="color: green">Yay, you got it </h1>' \
               '<img src="https://media4.giphy.com/media/3ndAvMC5LFPNMCzq7m/giphy.webp?cid=ecf05e474rod9vxj2phvno8986pipxa837hhnkfdavfs92hc&rid=giphy.webp&ct=g">'


if __name__ == '__main__':
    app.run(host="localhost", port=5008, debug=True)