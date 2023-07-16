const express = require('express')
const path = require('path');
const app = express()
const bodyParser = require('body-parser');

app.set('view engine', 'ejs');
app.set('views', path.join(__dirname, 'views'));
app.use(express.static(path.join(__dirname, 'public')));
app.use(bodyParser.urlencoded({ extended: true }));

const wines = {
    "10": {
        wine_name: "아주아주 달콤한 와인 - 10"
    },
    "9898": {
        wine_name: "아주아주 맛있느 와인 - 9898"
    },
}

app.get('/login', (req, res) => {
    res.render('login');
});

app.post('/login', function(req, res) {
    const userId = req.body.user_id;
    const userPw = req.body.user_pw;

    console.log('Received ID:', userId);
    console.log('Received PW:', userPw);

    res.redirect('/');
});

app.get('/wine', (req, res) => {
    const wine_id = req.query.id
    res.render('wine', wines[wine_id]);
});

app.listen(3000, () => {
    console.log('Server is running on port 3000');
});