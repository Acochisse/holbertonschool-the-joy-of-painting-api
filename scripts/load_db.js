// this script should load the database Joy_of_Painting.db, and pass usable information to an html page to be dynamic
// the script should load the column month, and randomly select a painting from the current month

const sqlite3 = require('sqlite3').verbose();
const fs = require('fs');
const path = require('path');




// open the database
const db = new sqlite3.Database(path.join(__dirname, 'Joy_of_Painting.db'));

// select a random painting from the current month
db.serialize(function () {
    db.run(`
        SELECT month, painting FROM Joy_of_Painting
        WHERE month =?
        `, [new Date().getMonth()], function (err, row) {
        if (err) {
            console.error(err);
        }
        else {
            console.log(row);
        }
    });
    db.close();
    process.exit(0);
});
