# Installation Guide
First, download all required modules through `pip install -r requirements.txt`

Currently, the Flask web app is operational and the extension doesn't have the appropriate tasks yet to display the result after pressing the button.
To view the Flask web application, simply run 'python model.py' first to instantiate the model, then run `python app.py`

To install the Chrome extension:
- Access `chrome://extensions/`
- Check `Developer mode`
- Click on `Load unpacked extension`
- Select the `extension` folder

# Model
The flask application is integrated with a model that predicts whether the input text is Real News or Fake news.

# App
app.py contains all the required for flask and to manage APIs.
