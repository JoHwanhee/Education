const express = require('express')
const path = require('path');
const app = express()

app.set('view engine', 'ejs');
app.set('views', path.join(__dirname, 'views'));
app.use(express.static(path.join(__dirname, 'public')));

app.get('/test', (req, res) => {
    res.render('index', { message: 'Hello, World!' });
});
  
app.listen(3000, () => {
    console.log('Server is running on port 3000');
});
