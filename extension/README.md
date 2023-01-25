# Installation Guide
First, download all required modules through `pip install -r requirements.txt`

Currently, the Flask web app is operational and the extension doesn't have the appropriate tasks yet to display the result after pressing the button.
To view the Flask web application, simply run `python app.py`

To install the Chrome extension:
- Access `chrome://extensions/`
- Check `Developer mode`
- Click on `Load unpacked extension`
- Select the `extension` folder

# Model
The flask-salary-predictor project predicts the salary of the employee based on the experience.
model.py trains and saves the model to the disk.
model.pkb the pickle model 

# App
app.py contains all the requiered for flask and to manage APIs.