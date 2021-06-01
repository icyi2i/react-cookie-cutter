# react-cookie-cutter

A sample react app to start with.

## Getting started

Keeping the steps to a minimum, scripts and base configuration files are already present in the root directory.

1. Clone the repository, or download and extract the zip package.
2. Rename the outer folder `react-cookie-cutter` to name of the project.
3. Run `python setup.py` in cmd or bash. (Configure npm package.)

   **Note** : This will remove any previous git repo files in .git folder

4. Change the scripts attribute of generated `package.json` to the following:

   ``` JSON
    "scripts": {
      "test": "jest",
      "dev:server": "nodemon --exec babel-node src/server/server.js --ignore dist/",
      "dev:bundler": "webpack -w --mode=development"
    }
   ```

5. Star the repository (Optional :)

## Future plans

- Add complete directory structure.
- Add initial files for quick bootstrapping.
