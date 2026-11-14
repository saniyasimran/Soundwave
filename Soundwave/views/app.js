const express = require("express");

const app = express();
const PORT = 3000;

// EJS setup
app.set("view engine", "ejs");

// Static files
app.use(express.static("public"));

// App details
const appName = "SoundWave";
const tagline = "Your Music, Your Mood, Your Sound";

// Songs data
const songs = [
    {
        title: "Perfect",
        artist: "Ed Sheeran",
        genre: "Pop"
    },
    {
        title: "Believer",
        artist: "Imagine Dragons",
        genre: "Rock"
    },
    {
        title: "Shape of You",
        artist: "Ed Sheeran",
        genre: "Pop"
    },
    {
        title: "Blinding Lights",
        artist: "The Weeknd",
        genre: "Pop"
    },
    {
        title: "Let Me Love You",
        artist: "Justin Bieber",
        genre: "R&B"
    },
    {
        title: "Counting Stars",
        artist: "OneRepublic",
        genre: "Pop Rock"
    }
];

// Home page
app.get("/", (req, res) => {
    res.render("index", {
        appName: appName,
        tagline: tagline
    });
});

// Songs page
app.get("/songs", (req, res) => {
    res.render("songs", {
        appName: appName,
        songs: songs
    });
});

// Start server
app.listen(PORT, () => {
    console.log(`Server running at http://localhost:${PORT}`);
});