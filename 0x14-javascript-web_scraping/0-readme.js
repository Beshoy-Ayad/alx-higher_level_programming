#!/usr/bin/node
/**
  reads and prints the content of a file
  first argument is the file path
 */

const fs = require('fs');

const filePath = process.argv.slice(2);

fs.readFile(filePath[0], 'utf8', (err, data) => {
  if (err) {
    console.error(err);
  } else {
    console.log(data);
  }
});
