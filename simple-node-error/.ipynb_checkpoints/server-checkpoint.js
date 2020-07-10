const express = require("express");
const os = require("os");
const app = express();

app.get("/", (req, res, next) => {
  res.send("Welcome from host: "+ os.hostname());
});

app.listen(process.env.PORT || 8091, () => {
  console.log("Server started...");
});
