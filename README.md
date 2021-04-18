# react-cookie-cutter

A sample react app to start with.

## Getting started

Keeping the steps to a minimum, scripts and base configuration files are already present in the root directory.

1. Clone the repository, or download and extract the zip package.
2. Rename the outer folder `react-cookie-cutter` to name of the project.
3. Run `setup.sh` in cmd or bash. (Initializes npm package and installs the dependencies.)
4. Change the scripts attribute of generated `package.json` to the following:
  ```
    "scripts": {
      "test": "jest",
      "dev:server": "nodemon --exec babel-node src/server/server.js --ignore dist/",
      "dev:bundler": "webpack -w --mode=development"
    }
  ```
5. Star the repository (Optional :)
