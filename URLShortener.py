from flask import Flask, render_template, request, redirect, url_for
from data import add_url, read_url
from config import SERVER_ADDR, PORT

app = Flask(__name__)
form_data = {'url': '', 'new_url': ''}
errors = []


@app.route('/')
def index():
    """ Отрисовка главной страницы с формой """
    global form_data, errors
    response = render_template('index.html', url=form_data['url'], new_url=form_data['new_url'], errors=errors)
    form_data = {'url': '', 'new_url': ''}
    errors = []
    return response


@app.route('/new', methods=['POST'])
def new_url():
    """ Создание нового URL по нажатию кнопки "сократить" """
    global form_data, errors
    if request.form['url'] == '':
        errors.append('Please, fill the URL field')
        return redirect(url_for('index'))
    url = add_url(normalize(request.form['url']), request.form['new-url'])
    if url is None:
        errors.append('Sorry! Short name you\'ve chosen is already in use')
        form_data['url'] = request.form['url']
        form_data['new_url'] = request.form['new-url']
        return redirect(url_for('index'))
    return redirect('/added/' + url)


@app.route('/added/<url>')
def result(url):
    """ Отрисовка страницы результата с новым URL """
    new_url = 'http://' + SERVER_ADDR + ':' + str(PORT) + '/get/' + url
    return render_template('result.html', url=new_url)


@app.route('/get/<url>')
def get_url(url):
    """ Обращение по короткому URL """
    return redirect(read_url(url))


def normalize(url):
    if url[:7] == 'http://' or url[:8] == 'https://':
        return url
    else:
        return 'http://' + url
