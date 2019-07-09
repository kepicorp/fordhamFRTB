from flask import Flask, redirect, session, url_for, request, jsonify
import requests, json, financial, config

app = Flask(__name__)
app.debug = True
app.secret_key = 'development'

api = config.api

@app.route('/')
def index():
    if 'token' in session:
        return get_token()
    return "Fordham Sample Flask Server is Running!"
                    
@app.route('/login')
def login():
    data = {u'grant_type': u'password', u'scope': u'access', u'username': unicode(config.username), u'password': unicode(config.password)}
    resp = requests.post(api+'cargo/oauthfull/authentication',data=data)
    if config.jsonresponse:
        session['token'] = str(json.loads(resp.text)['access_token'])
    else:
        session['token'] = resp.text[13:49]
    return redirect(url_for('compute'))

@app.route('/logout')
def logout():
    session.pop('token', None)
    return redirect(url_for('index'))

def get_token():
    return session.get('token')

@app.route('/cube')
def testcube():
    if 'token' in session:
        headers = {"Authorization": "Bearer "+get_token(), "content-type": "application/json"}
        req = requests.get(api+'cube',headers=headers)
        return str(req.text)
    return 'You must login first'

@app.route('/reports')
def testreports():
    if 'token' in session:
        headers = {"Authorization": "Bearer "+get_token(), "content-type": "application/json"}
        req = requests.get(api+'dynamic/v1/reports',headers=headers)
        return str(req.text)
    return 'You must login first'

@app.route('/compute')
def compute():
    if 'token' in session:
        name = config.report
        data = financial.compute()
        output = deleteCube(name)
        output = output + '\n' + importCube(data, name)
        output = output + '\n' + createReport(name)
        return output
    return redirect(url_for('login'))

@app.route('/computered')
def computered():
    if 'token' in session:
        return compute()
    else :
        data = {u'grant_type': u'password', u'scope': u'access', u'username': u'finastra', u'password': u'finastra'}
        resp = requests.post(api+'cargo/oauthfull/authentication',data=data)
        session['token'] = str(json.loads(resp.text)['access_token'])
        return compute()

    
def importCube(data, name='testPython'):
    headers = {"Authorization": "Bearer "+get_token(), "content-type": "text/csv"}
    req = requests.post(api+'cube/import?colsep=;&decsep=.&deleteReport=false&name='+name+'&vectorsep=|', headers=headers, data=data)
    if req.status_code == requests.codes.ok:
        return req.text
    return 'Failed to import error '+str(req.status_code)+' with '+req.text

def createReport(name='testPython'): 
    headers = {"Authorization": "Bearer "+get_token(), "content-type": "application/json"}
    data = {'name': name, 'cube': name}
    req = requests.post(api+'dynamic/v1/reports/createFromCube', json=data, headers=headers)
    if req.status_code == requests.codes.ok:
        return str(req.text)
    return 'Failed to import error '+str(req.status_code)+' with '+req.text

def deleteCube(name='testPython'):
    headers = {"Authorization": "Bearer "+get_token(), "content-type": "text/csv"}
    req = requests.delete(api+'cube/'+name, headers=headers)
    return 'done'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
