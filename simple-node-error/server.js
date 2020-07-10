const express = require("express");
const os = require("os");
const app = express();

let count = 0;

app.get("/", (req, res, next) => {
  /* Successful respond 5 times then error...*/
  count += 1;
  if (count <= 5) {
    res.send("Welcome from host: " + os.hostname());
  } else {
    res.status(400).send("Error...");
  }
});

app.listen(process.env.PORT || 8091, () => {
  console.log("Server started...");
});
