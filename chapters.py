from flask import Flask,render_template
app = Flask(__name__)
@app.route('/')
def contents() -> 'html':
    return render_template('contents.html')
@app.route('/mysql')
def mysql() -> 'html':
    return render_template('mysql.html')
@app.route('/flask')
def flask() -> 'html':
    return render_template('flask.html')
@app.route('/sitepackages')
def sitepackage() -> 'html':
    return render_template('includeModuleToSitepackages.html')
@app.route('/jinja2')
def jinja2() -> 'html':
    return render_template('jinja2.html', chapter = 'This sentence  is being rendered from chapters.py.Look in the code.')
@app.route('/commandline')
def commandline() -> 'html':
    return render_template('commandlineSyntax.html')
@app.route('/csv')
def csv() -> 'html':
    return render_template('csv.html')
@app.route('/connectingToDatabase')
def connectingToDatabase() -> 'html':
    return render_template('connectingToDatabase.html')
@app.route('/python')
def pythonessentials() -> 'html':
	return render_template('python.html')
@app.route('/css')
def css() -> 'html':
	return render_template('css.html')
@app.route('/html')
def html() -> 'html':
	return render_template('htmlTricks.html')
@app.route('/js')
def js() -> 'html':
	return render_template('js.html')
@app.route('/jira')
def jira() -> 'html':
	return render_template('jira.html')
if __name__ == '__main__':
    app.run(debug=True,port=8080)