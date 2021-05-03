# image-repository

Simple flask app to detect text or objects in the images. The app will returns google search urls for the relevant image

## How to run

1. `python -m venv venv`
1. `source venv/bin/activate`
1. `pip install -r requirements.txt`
1. `python main.py`

You will need a [Google Cloud Vison](https://cloud.google.com/vision) API Key. Rename it `service-account.json`

## Live App

The app is also availate on [Google Cloud Run](https://shopfiy-backend-ijheirxpjq-uc.a.run.app).
