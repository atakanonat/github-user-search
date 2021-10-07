# Imports
from flask import Flask, render_template, request
import requests

# Initialize Flask application
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get searched github username and search through github API
        github_name = request.form.get('github_name')
        response = requests.get('https://api.github.com/users/' + github_name)
        userInfo = response.json()

        # Check if user found
        if 'message' in userInfo:
            return render_template('index.html', error='User cannot found...')
        else:
            # Take repositories informations
            repos = requests.get(userInfo["repos_url"]).json()
            return render_template('index.html', user=userInfo, repos=repos)

    else:
        return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
