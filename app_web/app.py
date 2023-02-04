from flask import Flask,render_template, request, redirect, url_for, session

def create_app():
    # create and configure the app
    app = Flask(__name__)
    app.secret_key = 'shit123kjnsdf(()*3kj'

    # Simple route
    @app.route('/', methods=['GET', 'POST'])
    @app.route('/search')
    def search():
        if request.method == 'POST':
            session['keyword'] = request.form['keyword']
            return redirect('/result')
        else:
            return render_template('search.html')

    @app.route('/result')
    def result():
        keyword=session['keyword']
        return render_template('result.html',keyword=keyword)
    return app 


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)

