const { response, request } = require('express')
const express = require('express')
var morgan = require('morgan')
const cors=require('cors')

const app = express()
app.use(express.json())
app.use(morgan('tiny'))
app.use(cors())
app.use(function(error,request,response,next){
  if(!request.body.name||!request.body.number)
  {
    response.status(400).send(`Missing fields`)
    
  }
  else{
    next()
  }
})

const generateId = () => {
  const maxId = persons.length > 0
    ? Math.max(...persons.map(n => n.id))
    : 0
  return maxId + 1
}

let persons = [
  { id :1,name: 'Arto Hellas', number: '040-123456' },
  { id:2,name: 'Ada Lovelace', number: '39-44-5323523' },
  { id:3,name: 'Dan Abramov', number: '12-43-234345' },
  { id:4,name: 'Mary Poppendieck', number: '39-23-6423122' }
]
let names=persons.map(p=>p.name)
console.log(names)

app.get('/api/persons', (request, response) => {
    response.json(persons)
  })
var d=new Date()
var l=persons.length
console.log(l)
app.get('/api/info',(request,response)=>
{
  response.send(`Phonebook has info for ${l} people`+`<br/>`+`${d}`)}
)


app.get('/api/persons/:id',(request,response)=>
{
const id=Number(request.params.id)
person=persons.find(p=>p.id===id)
if(person)response.json(person)
else response.status(404).end()
}
)

app.delete('/api/persons/:id',(request,response)=>
{
  const id=Number(request.params.id)
  persons= persons.filter(p=>p.id!==id)
  response.status(204).end()
})
app.post('/api/persons', (request, response) => {
  const p = request.body
  let names=persons.map(p=>p.name)
  
  if(names.includes(p.name))response.status(400).send(`name already exists`)
  const person={
    id:generateId(),
    name:p.name,
    number:p.number
  }
  persons=persons.concat(person)
  response.json(p)
})







const PORT=3001
app.listen(PORT)
console.log(`Server running on port ${PORT}`)

