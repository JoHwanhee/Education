import express from 'express'
import bodyParser from 'body-parser';

import path from 'path'
import wines from './models/wine.js'
import { addUser, getUser } from './models/user.js';


const __dirname = path.resolve();
const app = express()
app.set('view engine', 'ejs');
app.set('views', path.join(__dirname, 'views'));
app.use(express.static(path.join(__dirname, 'public')));
app.use(bodyParser.urlencoded({ extended: true }));

// 가입
app.get('/signup', (req, res) => {
    res.render('signup');
});

app.post('/signup', (req, res) => {
    // console.log(req.body);
    // addUser(req.body.user_id, req.body.user_pw, req.body.user_name, '', '')
    
    
    // const body = req.body
    // addUser(body.user_id, body.user_pw, body.user_name, '', '')

    const {
        user_id, user_pw, user_name
    } = req.body
    addUser(user_id, user_pw, user_name, '', '')

    res.render('login');
});


// login
app.get('/login', (req, res) => {
    res.render('login');
});

app.post('/login', (req, res) => {
    const {
        user_id, user_pw
    } = req.body

    const user = getUser(user_id)
    if (user.password === user_pw) {
        res.render('wine');
    }
    else {
        res.render('error');
    }    
});


app.get('/wine', (req, res) => {
    res.render('wine');
});

app.listen(3000, () => {
    console.log('Server is running on port 3000');
});