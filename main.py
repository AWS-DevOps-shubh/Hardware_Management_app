from flask import Flask, render_template, request, redirect
from controllers.asset_controller import AssetController
from models.asset import Asset

app = Flask(__name__)
controller = AssetController()

@app.route('/')
def home():
    assets = controller.list_assets()
    return render_template('index.html', assets=assets)

@app.route('/add', methods=['POST'])
def add_asset():
    name = request.form['name']
    category = request.form['category']
    serial_number = request.form['serial_number']
    location = request.form['location']
    asset = Asset(name, category, serial_number, location)
    controller.add_asset(asset)
    return redirect('/')

@app.route('/delete/<int:asset_id>')
def delete_asset(asset_id):
    controller.delete_asset(asset_id)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)

