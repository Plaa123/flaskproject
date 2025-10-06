from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return 'Flask Home'
# 模版渲染
@app.route('/index/')
def index():
#     返回字符串
#     return '<b>Flask Index </b>'
# 模版渲染
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, port = 5001 )

