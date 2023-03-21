const express = require('express')
const app = express()
const port = 3000

app.set('view engine', 'ejs');

const bodyParser = require("body-parser");
app.use(bodyParser.urlencoded({ extended: true }))


const yesResponses = ['Really?', 'Are you sure?', 'Are you positive?']
const noResponses = ['Oh... really?', 'Hmm... are you sure?', 'Weird. Are you 100% sure?']


app.get('/', (req, res) => {
  res.render('index', {
    question: 'Would you like a flag?'
  })
})

app.post('/', (req, res) => {
  response = eval(req.body.question);
  if (response){
    question = yesResponses[Math.floor(Math.random()*yesResponses.length)];
  } else {
    question = noResponses[Math.floor(Math.random()*noResponses.length)];
  }
  res.render('index', {
    question: question
  })
})

app.listen(port, () => {
  console.log(`Listening on port ${port}`)
})

// TODO REALLY IMPORTANT implement getting flag from flag.txt file
