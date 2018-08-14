process.stdin.setEncoding("utf8");

const readline = require("readline");

const terminal = readline.createInterface({
  input: process.stdin,
  terminal: false
});

terminal.on("line", readLine);

/**
 * Function for working with terminal
 */

function readLine(line) {
  if (line !== "\n") {
    var numbersInString = line.toString().split(" ");

    var a = parseInt(numbersInString[0], 10);
    var b = parseInt(numbersInString[1], 10);

    process.exit();
  }
}
