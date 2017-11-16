#from flask import Flask, session, redirect, url_for, escape, request
from flask import Flask, render_template
import json
import math

app = Flask(__name__)

@app.route('/')
def index():
    with open('/shared/data.json', 'r') as fp:
        feeds = json.load(fp)

    i = len(feeds)
    j = int(math.ceil(float(i)/3))
    k = int(math.ceil(float(i)/3*2))
    feeds_left = feeds[0:j]
    feeds_mid = feeds[j:k]
    feeds_right = feeds[k:i]

    # maybe split into smaller templates

    return render_template('index.html', feeds_left=feeds_left, feeds_mid=feeds_mid, feeds_right=feeds_right)

#@app.route('/login', methods=['GET', 'POST'])
#def login():
#    if request.method == 'POST':
#        session['username'] = request.form['username']
#        return redirect(url_for('index'))
#    return '''
#        <form method="post">
#            <p><input type=text name=username>
#            <p><input type=submit value=Login>
#        </form>
#    '''
#
#@app.route('/logout')
#def logout():
#    # remove the username from the session if it's there
#    session.pop('username', None)
#    return redirect(url_for('index'))
#
## set the secret key.  keep this really secret:
#app.secret_key = b'\x9f\t{\xaf\x85q\xce\xcc\xb7\xd7\x809v\xa0\x18\xb6\x1aQM\x13\xe0~U(\xb9\xf7)G\x1d\x8eQ\x90'
if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
