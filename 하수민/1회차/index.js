const express = require('express')
const path = require('path');
const app = express()

app.set('view engine', 'ejs');
app.set('views', path.join(__dirname, 'views'));
app.use(express.static(path.join(__dirname, 'public')));

// API
const wines = {
    "10": {
        wine_name: "아주아주 달콤한 와인 - 10"
    },
    "9898": {
        wine_name: "아주아주 맛있느 와인 - 9898"
    },
}

// DB 접속

app.get('/wine', (req, res) => {
    const wine_id = req.query.id
    res.render('wine', wines[wine_id]);
});

app.listen(3000, () => {
    console.log('Server is running on port 3000');
});