# Remove cookcie-cutter repo and Initialize new git repository
rm -rf .git/
git init
# Initialize your application
npm init
# Web server - express
npm i express
# Development debugging server
npm i nodemon --save-dev
# Core react - react and react-dom
npm i react react-dom --save-dev
# Build and packing - webpack
npm i webpack webpack-cli --save-dev
# JSX transpiler - Babel
npm i babel-loader @babel/core @babel/node @babel/preset-env @babel/preset-react --save-dev
# Linting - eslint
npm i eslint babel-eslint eslint-plugin-react eslint-plugin-react-hooks --save-dev
# Testing - jest
npm i jest babel-jest react-test-renderer --save-dev

# Clean up (Avoid accidently calling this)
rm setup.sh
