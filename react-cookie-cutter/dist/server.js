const express = require('express')

const app = express()

const PORT = 5000

app.set("view engine", "ejs")
app.use(express.static("static"))

app.get('/', (req, res) => res.render("index"))

app.listen(PORT, () => console.log(
    `App server listening on port localhost:${PORT}!`))
