#!/usr/bin/node

const fs = require('fs');
const request = require('request');

const url = process.argv[2];
const filePath = process.argv[3];

request(url, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  if (response.statusCode !== 200) {
    console.error(`Failed to fetch data. Status code: ${response.statusCode}`);
    return;
  }

  fs.writeFile(filePath, body, 'utf-8', (err) => {
    if (err) {
      console.error(err);
      return;
    }
    console.log(`Content has been saved to ${filePath}`);
  });
});
