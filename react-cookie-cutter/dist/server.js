const express = require('express')

const app = express()

const PORT = 5000

app.get('/', (req, res) => res.render("index"))

app.listen(PORT, () => console.log(
    `App server listening on port localhost:${PORT}!`))
