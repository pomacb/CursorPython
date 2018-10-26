from factory import run_app

app = run_app()


@app.route('/home')
def home_page():
    return render_template('home.html', data=db)


if __name__ == "__main __":
    app.run()
