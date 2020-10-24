## Overview

The web client is built using React framework, as suggested by the prompt. The server uses the Flask Python framework. I use React to build a set of static files and then serve those static files and my server endpoints on the Flask server.

## How to test

If you want to run the entire app without any changes, you can do so in a virtual Python environment.

First activate the environment with `source bin/activate`.
Then run `pip3 install -r requirements.txt` to install the requirements.
Once it's activated, use `flask run` to run the Flask server.

Then open [http://localhost:3000](http://localhost:5000) to view in the browser.

## How to make changes

### Server

If you want to make changes to the server, you can make them to the `server` directory and save. The app will hot reload, which means the changes will automatically be reflected in the app without losing state.

### Client

#### `npm start`

If you want to make changes to the web client, you can make them to the `src` files.

Use this command to enter development mode. Then open [http://localhost:3000](http://localhost:3000) to view it in the browser.

The page will reload if you make edits.<br />
You will also see any lint errors in the console.

#### `npm run build`

Once you're done making changes, run this command to build the app for production to the `build` folder.<br />
It correctly bundles React in production mode and optimizes the build for the best performance.
