# react-cookie-cutter

A sample react app to start with.

## Getting started

Keeping the steps to a minimum, scripts and base configuration files are already present in the root directory.

1. Clone the repository, or download and extract the zip package.
   `git clone https://github.com/icyi2i/react-cookie-cutter.git`

2. Rename the outer folder `react-cookie-cutter` to name of the project.
3. Run `python setup.py` in cmd or bash. (Configure npm package.)

   ``` shell
   root@lab:~/projects/tooth_fairy# python3 setup.py
   # Initializing new empty git repository...
   Initialized empty Git repository in /root/projects/tooth_fairy/react-cookie-cutter/.git/
   # Installing required node modules...

   added 867 packages, and audited 868 packages in 8s

   found 0 vulnerabilities
   Enter the following details. Leave empty for default values:
   - name (react-cookie-cutter) :tooth_fairy
   - description (A minimal react setup for rapid development!) :A simple tooth fairy app!
   - keywords (['react', 'cookiecutter', 'template', 'express']) :Teeth, Fairies, react, app
   root@lab:~/projects/tooth_fairy#
   ```

   **Note** : This will remove any previous git repo files (.git folder)

4. Star the repository (Optional :)

## Build the app

Within the app folder run the command `npm run dev:bundler`.
This bundles all js components from **src** folder into **dist/static/main.js** file.

   ``` shell
   root@lab:~/projects/tooth_fairy/tooth_fairy# npm run dev:bundler

   > tooth_fairy@1.0.0 dev:bundler
   > webpack -w --mode=development

   asset main.js 1 MiB [emitted] (name: main)
   runtime modules 937 bytes 4 modules
   modules by path ./node_modules/ 982 KiB
   modules by path ./node_modules/scheduler/ 26.3 KiB 4 modules
   modules by path ./node_modules/react/ 70.6 KiB 2 modules
   modules by path ./node_modules/react-dom/ 875 KiB 2 modules
   ./node_modules/object-assign/index.js 2.06 KiB [built] [code generated]
   ./node_modules/style-loader/dist/runtime/injectStylesIntoStyleTag.js 6.67 KiB [built] [code generated]
   ./node_modules/css-loader/dist/runtime/api.js 1.57 KiB [built] [code generated]
   modules by path ./src/ 1.37 KiB
   modules by path ./src/styles/*.css 738 bytes
      ./src/styles/App.css 330 bytes [built] [code generated]
      ./node_modules/css-loader/dist/cjs.js!./src/styles/App.css 408 bytes [built] [code generated]
   ./src/index.js 192 bytes [built] [code generated]
   ./src/components/App.js 338 bytes [built] [code generated]
   ./src/helpers/index.js 132 bytes [built] [code generated]
   webpack 5.38.1 compiled successfully in 2027 ms
   ```

## Start the app

After successful build, express server can be started from **dist** folder
using command `node server.js`

``` bash
root@lab:~/projects/tooth_fairy/tooth_fairy/dist# node server.js
App server listening on port localhost:5000!
```

## Edit application

Add/Make changes to the components in **src/components** folder, build and run.

## Future plans

- Enhance express structure for multiple react apps.
- Add react extensions and related libraries.
