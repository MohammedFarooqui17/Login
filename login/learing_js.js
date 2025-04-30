// // ARRAYS
// const name3 = ["steve","jhon","jordan"]
// const name4 = ["steven","jhonson","jorge"]  
// // name.push(name1)// this will not return new array
// const all = name3.concat(name4)// this will return new array
// // console.log(name);
// console.log(all);

// const spread = [...name3, ...name4] // this is called spread(...) opeartor which is act same like concat
// console.log(spread);


// // flat() : is used for the concetinations when we have multiple arrays in a single array like below example
// const name5 = ["steven","jhonson","jorge",[1,2,3,],999,[9087,2685],90,[999,1,2,3,4]]//exact depts of this 3
// const op = name5.flat(3)// this will return a single array : flat(infinity)-> when we dont want to mentions depth
// console.log(op)

// console.log(Array.from("Moammed"))//Array.from -> this will make the new array if they are not
// const score1 = 100
// const score2 = 200
// const score3 = 300
// console.log(Array.of(score1,score2,score3));// this will also create the array

//----------------------------------------------------------

// OBJECTS

// const mysym = Symbol("name")
// let user = {
//     "name":"xyz",
//     [mysym]:"name1",
//     "age":1,
//     "email":"xyz@gamil.com"
// }
// console.log(user);
// console.log(typeof user[mysym]);


// user.name="Mohammed"


// // const test = new Object()// this is called singleton objects or we are creating by using constructor 
// const test = {}
// test.id="1"
// test.name='Mohammed'
// console.log(test);


// const obj1 = {"a":1,"b":2}
// const obj2 = {"c":3,"d":4}
// const obj3 = {"e":5,"f":6}
// const final1 = Object.assign(obj1,obj2,obj3)  // used to merge or concatinate multiple objects in a single object
// const final2 = Object.assign({},obj1,obj2,obj3)

// const final3 = {...obj1, ...obj2, ...obj3}// used to merge or concatinate multiple objects in a single object
// console.log(final1)
// console.log(final2)
// console.log(final3)

// console.log(Object.keys(test))//return keys :["name","age"]
// console.log(Object.values(test))//return values: ["Mohammed",24]
// console.log(Object.entries(test))//return key and value: [{"name:"Mohammed"},{"age:24}]
// console.log(test.hasOwnProperty("name"))//if it will be there then return true alse false 

// object de-structure and json Api

//de structure
// const course={
//     "name":"xyz",
//     "price":2000,
//     "coursestructure":"Mohammed"
// }

// const {coursestructure:name}=course // this is nothing but de-structure {coursestructure:name}
// const {name,price}=Course; // de-structure or unpack the object variable
// console.log(name);




//----------------------------------------------------------------------

// FUNCTIONS:

// function add(num1,num2){
//     return num1 * num2
// }
// const result = add(2,8)// when we return somthing inside functions then only we can store in a variable
// console.log(result)



// ... -> this three dost is called rest operator also spread operator 
// when we use inside functions is called rest operator

// function calculatecartprice(...num){
//     return num
// }
// console.log(calculatecartprice(2,3,4,5,6,900000)) // all the value will return in a array


// functions with object 
// const user ={
//     username:"Mohammed",
//     price:100000,
// }

// function myobject(anyobj){  // anyobject is nothing but we can consider as a genric like any object will com then also it will handle
//     console.log(`${anyobj.username} and ${anyobj.price}`)
// }

// myobject(user)//--> the user object is compulsory to pass inside the function when we are calling the functions 


// const user2 = {
//     username:"Mohammed",
//     price:1900000,

//     welcome: function(){
//         console.log(`${this.username}`)// this indicate the current context
//     }
// }
// user2.welcome()
// console.log(this);// this will return empty object but if we run this inside browser it will return the windows object 


// function one(){
//     let username="Mohammed"// this context we cannot use inside the functions we only use inside the object
//     console.log(this.username)// this will not work because this context work only when we sre using the object 
//     console.log(this)// when we use this key inside the functions it returns many things 
// }
// one()


// // types of function

// const chai = function(){
//     let username= "Mohammed"
//     console.log(this.username)
// }
// chai()


// const chai2 = () =>{
//     let username= "Mohammed"
//     console.log(this.username)
// }
// chai2()

// const chai3 = () =>{
//     let username= "Mohammed"
//     console.log(this)// when we use this keysword inside the arrow functions it return empty object but whn we use in normal functions it return many things which is the main diffrence between arrow functions and normal functions 
// }
// chai3()


// if we use curly braces then it must use to the return keyword when we use parenthesis then we do not use return keyword
// const chai4 = (num1,num2) =>{
//     return num1+num2
// }
// console.log(chai4(6,8))



// // implicit arrow function 
// const chai5 = (num1,num2) => num1+num2
// console.log(chai5(6,8))

// const chai6 = (num1,num2) => ({username:"xyz"})// when we return any object those object should be pas inside the parenthesis
// console.log(chai6(6,8))

//------------------------------

//IIFE: immediately invoke function expression 

// (function(){
//     console.log()
// }
// )(); // this ; is very important when we write two iife 


// (()=>{

// }

// )();


// //--------------------------------------

// // EXECUTIONS CONTEXT: how to execute the file what we have created

// // 1)GLOBAL EXECUTIONS CONTEXT:
// // 2) FUNTIONAL EXECUTION OBJECT
// // 3) EVAL EXECUTION OBJECT

// // code execute in two face : 1) MEMORY CREATIONS PHASE   2) EXECUTION PHASE 

// // call stack :It is a stack data structure that works on the Last In, 
// // First Out (LIFO) principle, which means that the last function that gets called is the first one to be executed
// //  and removed from the stac

// //-----------------------------------------------------------

// // CONTROL FLOW:

// const score =100
// if (score<190){
//     console.log("scrore is less 100")
// }
// else{
//     console.log("score is less than 100");
    
// }

// // short hand
// const balance = 10000
// if (balance>500) console.log("test")


// // switch:
// const month = "april"
// switch(march){
//     case "march":
//         console.log("March")
//         break;
//     case "april":
//         console.log("April")
//         break;
//     case "may":
//         console.log("May")
//         break;
//     default:
//         console.log("month checking")
// }

// // falsy value : 0,-0,bigint 0n ,"", null , undefined, nan
// //truthy values: "0","false"," ", [] , {} , function(){}

// const userEmail = []
// if(userEmail.length===0)                                           {
//     console.log("Array is empty");
    
// }


// const emptyobj = {}
// if(Object.keys(emptyobj).length===0){
//     // Object.keys(emptyobj): this return us array
//     console.log("object is empty");
    
// }


// // false==0
// // true

// // false==""
// // true

// // 0==""
// // true


// nullish coalescing opeartor(??): null undefined // this is used for to handle the null and undefined values
// let val;
// val= 5??9
// val1=null??10
// val2=nul??undefined??10
// console.log(val)
// console.log(val1)
// console.log(va2)


// terniary Oprator
// condition? true : false


// const iceTeaPrice=80
// iceTeaPrice>=80? console.log("less than 80"):console.log("more than 80")

//----------------------------------------------------------------------------


for (let index = 0; index < 10; index++) {
    const element = index;
    if(element==6){
        break;
    }
    // console.log(element);
}


for (let i = 1; i <=10; i++) {
    // console.log(`outer loop value:${i}`);
    for (let j = 1; j <=10; j++) {
        // console.log(`inner loop value :${j} and inner loop:${i}`)
        // console.log(i + '*' + j + '=' + i * j )
         
    }
}

let myarray = ["python", "javascripts","java"]
for (let index = 0; index <myarray.length; index++) {
    const element = myarray[index];
    // console.log(element)  
}


for (let index = 0; index < myarray.length; index++) {
    const element = myarray[index];
    if(element==="java"){
        break;
    }
    // console.log(`${element}`)
}




for (let index = 0; index <=10; index++) {
    const element = index;
    if(element==6){
        // console.log("six will be skipped")
        continue;
    }
    // console.log(index)
    
}


// while loo and do wile loop

let i=0
while(i<10){
    // console.log(i)
    i++;
}


do{
    // console.log(i)
    i++;
}while(i<11)

//--------------------------------------------------->

// for of loop

const arr = [1,2,3,4,5]
for (const val of arr) {
    // console.log(val)
}

const greet = "hello world!"
for (const greeting of greet) {
    // console.log(greeting)
}

// Maps: it store the unique values and hold the key and value pair and rememeber the original insertion orderof the keys
// map is also not iterable

const map = new Map()
map.set('in',"india")
map.set('usa',"united state of america")
map.set('fr',"france")
// console.log(map)
for (const [key, values] of map) {
    // console.log(key,values)
}
//[key, values]=> this destructure


//----------------------

// const myobj = {
//     'name':"Mohammed",
//     "age":10
// }
// this loop will not work when we are working with object
// for (const [keys,values] of myobj) {
//     console.log(keys,values)
// }


// for in loop  is use full for both object and arrys
// ------------------------------------------

const myobj = {
    'name':"Mohammed",
    "age":10
}
for (const key in myobj) {
    // console.log(myobj[key])
}


const test =["js","python","java"]
for (const key in test) {
    //  console.log(key)// this will return the index number of the arrays elements
    console.log(test[key])// this will return the value of the arrys
}

//---------------------------------------------------------

// foreach loop: this loop is not return anything

const coding = ["python","javascript","java","c++"]
// forEach(callbackfn: (value: string, index: number, array: string[]) => void, thisArg?: any): void
// for each mathod takes a calllbackfunction without any name which we are using below


// coding.forEach( function(item){
//          console.log(item)
// } )

// const coding = ["python","javascript","java","c++"]
// for each with arrow functions
// coding.forEach((item)=>{
//     console.log(item)
// })

function myname(item){
    console.log(item)
}
mylist = [1,2,3,4]
mylist.forEach(myname)


mydict = {"name":"xyz","age":17}
Object.keys(mydict).forEach(function(item){
     console.log(item)
})


mydict = {"name":"xyz","age":17}
Object.values(mydict).forEach(function(item){
     console.log(item)
})

mydict = {"name":"xyz","age":17}
Object.entries(mydict).forEach(function([key, value]){
     console.log(key,value)
})

// function printme(item){
//     console.log(item)
// }
// coding.forEach(printme)// give the only refrence of the functions do not call functions like this foreach(printme()) it will gives error


// inside the foreach we have access of these things item,index, arr-> return whole list of arrys
coding.forEach((item,index,arr)=>{
    // console.log(item,index,arr)
})
//ouput of this code
// python 0 [ 'python', 'javascript', 'java', 'c++' ]
// javascript 1 [ 'python', 'javascript', 'java', 'c++' ]
// java 2 [ 'python', 'javascript', 'java', 'c++' ]
// c++ 3 [ 'python', 'javascript', 'java', 'c++' ]



const mycoding =[
    {
        language:"python",
        languagefile:"py"
    },

    {
        language:"javascript",
        languagefile:"js"
    }
]
// (item)={} 
mycoding.forEach( (item)=>{
    // console.log(item.languagefile)
})


//----------------------------------------------------------

// foreach loop is not return anything

// filter and map


// const coding1 = ["python","javascript","java","c++"]
// const values = coding1.forEach((item)=>{
//     console.log(item)
// })
// console.log(values)// we got undefined because for each is not return anything



//  filter():this method also takes callbackfunction
const number =[1,2,3,4,5,6,7]
const num1=number.filter((num)=>{
    return num==5;
})
// console.log(num1)

// 
const num2 =number.filter((num)=> num>5)
// console.log(num2)


// same things by using foreach
const newnum =[]
number.forEach((num)=>{
    if(num>4){
        newnum.push(num)
    }
})
console.log(newnum)


// map() method takes callbackfunctions also return values automatically
const myNumber = [1,2,3,4,5,6,7,8,9]
const hello= myNumber.map((num)=>num+1)
// console.log(hello)



// chaining : we can use the method continiously(cont n1 = myNumber.map().map().filter)

const n1 = myNumber.map((num)=>num*10).map((num)=>num+1).filter((num)=>num)
// console.log(n1)

// ouput : [ 11, 21, 31, 41, 51,61, 71, 81, 91]


// reduce() in the reduce it takes callbackfunctions inside callbackfunc takes two param
//accumulator -> it is nothings but initial val means 
// accumulator = initialval , currentval -> array first val means 1

const myNum = [1,2,3,4,5,6,7,8,9]
const intialval=0
const sumwithinitial = myNum.reduce((accumulator,currentval)=> accumulator+ currentval, intialval);
console.log(sumwithinitial)
// input -> [1,2,3,4,5,6,7,8,9] , ouput ->  45



//-------------------------------------------------------------------------------

const strnum = [12,33,17]
const store=[]
strnum.forEach((item)=>{
    if(item>=11){
        store.push(item)
    }
    // console.log(store)
})
const abc = strnum.filter((item)=>{
    return item>11;
})
// console.log(abc)

for(key of strnum){
    // console.log(key)
}
for(key in strnum){
    // console.log(strnum[key])
}

//-----------------------------------------------------------

// DOM 
// document.getElementById('title')  -> it will return the element title
// document.getElementById('title').getAtttribute('id')   -> it will return the title element id name 
// document.getElementById('title').setAtttribute('class','test')   -> it will set the class name of the title element

// const title = document.getElementById('title')
// title.style.backgroundColor='red'
// title.style.padding='12px'
// title.style.border-radious='5px'

// HOW TO ADD THE CONTENT and retrive

// title.textContent // it gives all the content including hidden

//  title.innerHTML -> return the content ---> it gives content also html value 
//  title.textContent -> return the content ---> it gives all the content including hidden
//  title.innerText -> return the content  ---> it gives only visible content


//  document.getElementByClassName('.heading')-> it return -> HTML COLLECTIONS DATA TYPE
//  document.querySelector('h1') --> return the first element of h1 which present in our document
//  document.querySelector('#title')
//  document.querySelector('.heading') 
//  document.querySelector('input[type="password"]') 


//  Example 
// -----------
/* <ul>
    <li>one</li>
    <li>two</li>
    <li>three</li>
</ul> */

// QUERYSELECTOR
// const myul = document.querySelector('ul')
// turngreen = myul.querySelector('li')  //it will return firt li elemet of ul
// turngreen.style.background-color ='green'
// turngreen.style.padding ='12px'
// turngreen.innerText // will return "one"
// turngreen.innerText="ten" // now  it will "ten"








//------------------------------------------------

const paragraph = document.getElementsByClassName('exmaple')
console.log(paragraph)//{0:p, 1:p , 2:p}
console.log(paragraph[0])// <p>fisrt</p>
console.log(paragraph[1])// <p>Second</p>
console.log(paragraph[2])// <p>Third</p>
for(i=0, i<paragraph.length , i++){
    console.log(paragraph[i].textContent)//fisrt,Second,Third
}

const newpragraph = document.createElement('p')
newpragraph.className='unique'
newpragraph.textContent="Fourth"
document.getElementById('id').appendChild('newparagraph')



//  Example 
// -----------
/* <ul>
    <li>one</li>
    <li>two</li>
    <li>three</li>
</ul> */

// **  QUERYSELECTOR ALL : it will return NODE LIST DATA TYPE 
// const myul = document.querySelectorAll('li')// it will return nodelist all the li elements
// const templist = document.QuerySelectorAll('li')
// templist // return nodelist  and this is not an array 
// templist.style.color = 'green' /// this will not work because this is not an array this is node list so for that we wil apply another approach which will be work and for that see the below 
// templist[0].style.color='green' // now this will work
// templist.forEach((li){
//   li.style.color='orange',
//   li.style.padding='12px',
//   li.innerHTML="Mohammed"// will set mohammed inside li  
//   li.style.border-radious='5px',}) // this will also will work properly when we get the data type node list 
//  when we got the data type node list at that time we should use mostly "forEach" loop

//---------------------------

// ** GETELEMENT BY CALSS NAME : RETURN THE HTML COLLECTIONS DATA TYPE which is like array (not array like array)
// EXAMPLE:

/* <ul>
<li class="list-item">one</li>
<li class="list-item">two</li>
<li class="list-item">three</li>
</ul> */

// document.getElementsByClassName(list-item) // it will return "HTML COLLECTIONS DATA TYPE"  in this foreach will not work so for this we will convert into array below 
// const templist= document.getElementsByClassName(list-item)/ will convert this by using Array.from()
// Array.from(templist) // now it will become array and then we get the for each loop
// const myarray = Array.from(templist)
// myarray.forEach((item){
    //  item.color="blue",
    //  item.background-color="white",
//  })

//---------------------

// Array.from('temp')-> means convert the temp into array list  
// HTML COLLECTIONS AND NODE LIST

//---------------------------------------------

// HOW TO CREATE NEW ELEMENT IN DOM
/* <html>
<body>
    <div class="parent">
        <div class="day">Monday</div>
        <div class="day">Tuesday</div>
        <div class="day">Wednesday</div>
        <div class="day">Thursday</div>
        <div class="day">Friday</div>
        <div class="day">Saturday</div>
        <div class="day">Sunday</div>
    </div>
</body>
<script>
  const parent = document.querySelectorAll('.parent')
  console.log(parent)// will get all the days div element
  console.log(parent.children)// will return html-collections  with all children
  console.log(parent.children[1])// will return this "<div class="day">Tuesday</div>"
  console.log(parent.children[1].innerHTML)// will return the text also which is Tuesday "<div class="day">Tuesday</div>"

  for (let i = 0; i<parent.children.length; i++) {
    console.log(parent.children[i].innerHTML);// will return all the days which are present
    
  }
  parent.children[1].style.color="orange" // tuesday will be orange 
  console.log(parent.firstElementChild); // will return the "<div class="day">Monday</div>"
  console.log(parent.lastElementChild); // will return the  "<div class="day">Sunday</div>"

  const dayone = document.querySelectorAll('.day')
  console.log(dayone)
  console.log(dayone.parentElement); // it will return the parent element 
  console.log(dayone.nextElementSibling);// it will return the sibling like here (monday sibling is tuesday)

  console.log("NODES:",parent.childNodes);
  
  
</script>

</html> */

//--------------------------------------------

// HOW TO CREATE NODE LIST PROGRAMMICALLY

/*<html>
<body>

</body>
<script>

  // to create element

  const div = document.createElement('div')
  div.className = 'main'
  div.id = 'test'
  div.setAtttribute("title","genrated title")// this is used to create custom getAtttribute
  div.style.backgroundColor ="green"
  div.style.padding ="12px"
  div.innerText="hello"// this will override
  const addtext = document.createTextNode("hello")// this will not override 
  div.appendChild(addtext)
  document.body.appendChild(div) // this will attach to the document of this element

</script>

</html>  */

//---------------------------------------------------------------------

// EDIT AND REMOVE ELEMENTS IN DOM:

/* <html>
    <body>

        <ul class="language">
            <li>JavaScript</li>
        </ul>

        <script>
            // insert element by using function but this one is not a proper optimize 
             function addlanguage(langName){
                const li = document.createElement('li');
                li.innerHTML=`${li}`
                document.querySelector('.language').appendChild(li)

             }
             addlanguage("pthon")
             addlanguage("javascript")


   

             
             // insert element by using function but  proper optimize 
             function addoptimize(langName){
                const li = document.createElement('li')
                // const addtext = document.createTextNode(langName)
                // li.appendChild(addtext)
                li.appendChild(document.createTextNode(langName))
                document.querySelector('.language').appendChild(li)

             }
             addoptimize('golang')


             // Edit value
             const secondlang = document.querySelector("li:nth-child(2)")
             secondlang.innerHTML='Mojo'// this is not a optimize approach

             const newli = document.createElement('li')
             newli.textContent = "Mojo" 
             secondlang.replaceWith(newli)


             // Edit
             const firstlang=document.querySelector("li:first-child")
             fisrtlang.outerHTML = "<li>Typescript</li>"


             // remove
             const lastlang = document.querySelector('li:last-child')
             lastlang.remove()


        </script>
    </body>
</html> */

//-------------------------------

// practice project

// FIRST
// <!DOCTYPE html>
// <html lang="en">

// <head>
//     <meta charset="UTF-8">
//     <meta name="viewport" content="width=device-width, initial-scale=1.0">
//     <title>code sandbox / stackblitz</title>
//     <style>
//         /* #grey {
//             padding: 18px;
//             background-color: gray;
//             border-radius: 2px;
//             border-color: 2px;
//         }


//         #blue {
//             padding: 18px;
//             background-color: rgb(64, 64, 184);
//             border-radius: 2px;
//         }

//         #charcol {
//             padding: 18px;
//             background-color: rgb(52, 49, 49);
//             border-radius: 2px;
//         }

//         #black {
//             padding: 18px;
//             background-color: rgb(0, 0, 0);
//             border-radius: 2px;
//         } */



//         #canvas {
//             text-align: center;
//             padding: 50px;
//         }

//         /* Style the buttons */
//         .button {
//             padding: 10px 20px;
//             margin: 10px;
//             font-size: 18px;
//             cursor: pointer;
//             border-radius: 5px;
//             display: inline-block;

//         }

//         #grey {
//             background-color: grey;
//             color: white;
//         }

//         #blue {
//             background-color: blue;
//             color: white;
//         }

//         #charcol {
//             background-color: rgb(61, 58, 56);
//             color: white;
//         }

//         #black {
//             background-color: black;
//             color: white;
//         }
//     </style>
// </head>

// <body>
//     <div id="canvas">
//         <h1>button</h1>
//         <span class="button" id="grey">grey</span>
//         <span class="button" id="blue">blue</span>
//         <span class="button" id="charcol">charcol</span>
//         <span class="button" id="black">black</span>
//     </div>

//     <script>
//         const buttons = document.querySelectorAll('.button')
//         console.log(buttons)
//         const body = document.querySelector('body')
//         console.log(body)

//         buttons.forEach(function (button) {
//             console.log(button);

//             button.addEventListener('click', function (e) {
//                 console.log(e)// this will tell us which event occured
//                 console.log(e.target) // this will return the detailsof event from which button we have clicked
//                 if (e.target.id === 'grey') {
//                     body.style.backgroundColor = e.target.id
//                 }

//                 if (e.target.id === 'blue') {
//                     body.style.backgroundColor = e.target.id
//                     // body.style.backgroundColor = 'red'
//                 }


//                 if (e.target.id === 'charcol') {
//                     body.style.backgroundColor = e.target.id
//                 }

//                 if (e.target.id === 'black') {
//                     body.style.backgroundColor = e.target.id
//                 }


                // by using switch case 
                // switch (e.target.id) {
                //     case 'grey':
                //         body.style.backgroundColor = 'grey';
                //         break;
                //     case 'blue':
                //         body.style.backgroundColor = 'blue';
                //         break;
                //     case 'charcol':
                //         body.style.backgroundColor = 'chocolate';
                //         break;
                //     case 'black':
                //         body.style.backgroundColor = 'black';
                //         break;
                //     default:
                //         body.style.backgroundColor = 'white'; // Default color in case of unexpected button
                //         break;
                // }
        //     })
        // });


        // call back functions example

        // This is the callback function
            // function sayHello() {
            //     console.log("Hello, the task is complete!");
            // }

            // // This is the function that takes another function (callback) as an argument
            // function completeTask(callback) {
            //     console.log("Task is being done...");
            //     // When the task is done, we call the callback function
            //     callback();
            // }

            // // Calling completeTask and passing sayHello as a callback
            // completeTask(sayHello);


//         </script>

// </body>

// </html>


//----------------------------------------------

// SECOND

// const form = document.querySelector('form')
// form.addEventListener('submit',function(e){
//     e.preventDefault();
    
//     const height = parseInt(document.querySelector('#height').values);
//     const weight = parseInt(document.querySelector('#weight').values);
//     const result = document.querySelector('#result');

//     if(height==='' || height<0 || isNaN(height)){
//         result.innerHTML="please provide a valid height"
//     }else if(weight==='' || weight<0 || isNaN(weight)){
//          result.innerHTML="please provide a valid weight"
//     }
//     else{
//         (weight/((height*height)/1000).toFixed(2))
//     }

// });

//------------------------------------------------------

// THIRD PROJECT: clock

//  <script>
//     const clock = document.getElementById('clock')
//     setInterval(function(){
//         let date = new Date()
//         clock.innerHTML = date.toLocaleTimeString()
//     },1000)
// </script> 



//-----------------------------------------------------------

// PROJECT FORTH

// let randomNumber = parseInt(Math.random() * 100 + 1);

// const submit = document.querySelector('#subt');
// const userInput = document.querySelector('#guessField');
// const guessSlot = document.querySelector('.guesses');
// const remaining = document.querySelector('.lastResult');
// const lowOrHi = document.querySelector('.lowOrHi');
// const startOver = document.querySelector('.resultParas');

// const p = document.createElement('p');

// let prevGuess = [];
// let numGuess = 1;

// let playGame = true;

// if (playGame) {
//   submit.addEventListener('click', function (e) {
//     e.preventDefault();
//     const guess = parseInt(userInput.value);
//     console.log(guess);
//     validateGuess(guess);
//   });
// }

// function validateGuess(guess) {
//   if (isNaN(guess)) {
//     alert('PLease enter a valid number');
//   } else if (guess < 1) {
//     alert('PLease enter a number more than 1');
//   } else if (guess > 100) {
//     alert('PLease enter a  number less than 100');
//   } else {
//     prevGuess.push(guess);
//     if (numGuess === 11) {
//       displayGuess(guess);
//       displayMessage(`Game Over. Random number was ${randomNumber}`);
//       endGame();
//     } else {
//       displayGuess(guess);
//       checkGuess(guess);
//     }
//   }
// }

// function checkGuess(guess) {
//   if (guess === randomNumber) {
//     displayMessage(`You guessed it right`);
//     endGame();
//   } else if (guess < randomNumber) {
//     displayMessage(`Number is TOOO low`);
//   } else if (guess > randomNumber) {
//     displayMessage(`Number is TOOO High`);
//   }
// }

// function displayGuess(guess) {
//   userInput.value = '';
//   guessSlot.innerHTML += `${guess}, `;
//   numGuess++;
//   remaining.innerHTML = `${11 - numGuess} `;
// }

// function displayMessage(message) {
//   lowOrHi.innerHTML = `<h2>${message}</h2>`;
// }

// function endGame() {
//   userInput.value = '';
//   userInput.setAttribute('disabled', '');
//   p.classList.add('button');
//   p.innerHTML = `<h2 id="newGame">Start new Game</h2>`;
//   startOver.appendChild(p);
//   playGame = false;
//   newGame();
// }

// function newGame() {
//   const newGameButton = document.querySelector('#newGame');
//   newGameButton.addEventListener('click', function (e) {
//     randomNumber = parseInt(Math.random() * 100 + 1);
//     prevGuess = [];
//     numGuess = 1;
//     guessSlot.innerHTML = '';
//     remaining.innerHTML = `${11 - numGuess} `;
//     userInput.removeAttribute('disabled');
//     startOver.removeChild(p);

//     playGame = true;
//   });
// }

//-----------------------------------------------------------

// Events 

// this will work but does not gives us more informations so for that we use listner like addEvenetListner()
// document.getElementById('owl').onclick=function(){
//     alert("owl clicked")
// }

// this is goood approach and addEventListener('click',function(){},false) it takes three arguments and the last argument by default is false
// document.getElementById("owl").addEventListener('click',function(){
//     alert("pwl clicked")
// })

// pending topic
// event object , event type , timestamp , defaultprevent, target , toElement ,soureElemenet,current target , client x,y, screen x,y , altkey, ctlkey, shiftkey , keyCode


// bublingup : means it gose from the below to top below  this is laos called event propegation example is bublingup and the reason is output 
// first : owl clicked  and then :"clicked inside ul"
// document.getElementById("images").addEventListener('click',function(e){
//     alert("clicked inside ul")
// }, false)
// document.getElementById("owl").addEventListener('click',function(e){
//     console.log("owl clicked")
// },false)



// capturing mode : it goes to to bottom
// document.getElementById("images").addEventListener('click',function(e){
//     alert("clicked inside ul")
// }, true)
// document.getElementById("owl").addEventListener('click',function(e){
//     console.log("owl clicked")
// }, true)


// to prevent event bubling we use stoppropegations
// document.getElementById("owl").addEventListener('click',function(e){
//     console.log("owl clicked")
//     e.stopPropagation()// to prevent bubling
// }, true)


//  prevent default
// document.getElementById('google').addEventListener('click',function(){
//     e.preventDefault();
//     e.stopPropagations()
// },false)


// to remove any pictue or anythings
// document.querySelector('#images').addEventListener('click',function(e){
//     console.log(e)
//     console.log(e.target.parentNode);
//     console.log(e.target.tagName);
    
//     if(e.target.tagName==='IMG'){
//         console.log(e.target.id)
//         let removeit = e.target.parentNode
//         removeit.remove() // eacy and simple way to remove
//     }

    // let removeit = e.target.parentNode
    // removeit.remove() // eacy and simple way to remove
    
    // removeit.parentNode.removeChild(removeit) // second approach little bit complicated

// })


//---------------------------------------------------------

// // Async in javascripts
// <h1>chai aur code </h1>
// <button id="stop"> STOP</button>

// const sayM = function(){
//     console.log("Mohammed")
// }

// const chantext = function(){
//     document.querySelector('h1').innerHTML="best js seres"
// }

// const changeme = setTimeout(chantext,2000)//

// document.querySelector('#stop').addEventListener('click',function(){
//     clearTimeout(changeme)//
//     console.log("Stopped")
// })
// //--------------------------------------------------

// /* <h1> Start should change the background color evry second</h1>
//    <button id="start">start</button>
//    <button id="stop">stop</button>  */


// // genrate random color 

// const randomcolor = function(){
//     const hex = "0123456789ABCDEF"
//     let color = "#"
//     for(let i= 0; i<6; i++){
//         color +=hex[Math.floor(Math.random()*16)]
//     }
//     return color
// }
// console.log(randomcolor)

// let intervalid;

// const startchangingcolor = function(){
//   if(!intervalid){
//     intervalid = setInterval(changebgcolor,1000)
//   }

//     function changebgcolor(){
//         document.body.style.backgroundColor=randomcolor
//     }
// }
// const stopchangingcolor = function(){
//     clearInterval(intervalid)
//     intervalid=null
// }

// document.getElementById("#start").addEventListener('click',startchangingcolor)
// document.getElementById("#stop").addEventListener('click',stopchangingcolor)



// // ----------------------------------------------------------------------

// //  API REQUEST AND V8 ENGINE

//     const requestUrl = "https://api.github.com"
//     const xhr = new XMLHttpRequest()
//     xhr.open('GET',requestUrl)
//     console.log(xhr.readyState)
//     xhr.onreadystatechange = function(){
//         console.log(xhr.readyState)
//         // if(xhr.onreadystatechange===4)
//         if(xhr.readystate===4){
//             const data = JSON.parse(this.response)
//             console.log(typeof data)
//             console.log(data.follower)
//         }
//     }
//     xhr.send()

// //---------------------------------------------------------------


// //  CALLBACK EXMAPLE:

// function getData(dataId,getnextData){
//     setTimeout(()=>{
//         console.log("data",dataId);
//         if(getnextData){
//             getnextData()
//         }
//     },2000)
// }
// getData(1,()=>{
//     getData(2,()=>{
//         getData(3,()=>{
//             getData(4);
//         })
//     })
// })


// //---------------------------------------


// const promise = new Promise(function(resolve,reject){
//     setTimeout(()=>{
//         let error = false
//         if(!error){
//             resolve({'username':"smith"})
//         }else{
//             reject("something is wrong")
//         }
//     },1000)
// })


// async function xyz(){
//     const response = await promise
//     console.log(response)
// }



// async function xyz(){
//     try{
//     const response = await promise
//     console.log(response)
//     } catch(error){
//         console.log(error)
//     }
// }
// xyz()



// function myfunc(username){
//     this.username=username
//     console.log("called")
// }
// myfunc("testing")

// function mycall(username,email,password){
//     myfunc(username)// if we call this then the functions will be called but there referece or all the things which is inside that functions will be remove so for that we use ".CALL()"
//     myfunc.call(this,username)// .call store the reference of the myfunc "call will pass the current executions to the other "
//     this.email=email
//     this.password=password
// }

// const obj1 = new mycall("xyz","xyz@gmail.com",123)
// const obj2 = new mycall("abc","abc@gmail.com",1122)
// console.log(obj1)
// console.log(obj2)


//-----------------------------------------

// class User{
//     constructor(username,email,password){
//         this.username=username
//         this.email=email
//         this.password=password
//     }

//     encyptpassword(){    
//         return `${this.password}123`
//     }

//     chnageusername(){
//         return `${this.username.toUppperCase()}`
//     }
// }

// const obj = new User("Mohammed","mohame@gmail.com","mohffs$df")
// console.log(obj.encyptpassword())
// console.log(obj.chnageusername())


//------------------------------------------------------

// behind Scene of this class base option 

// function User(username,email,password){
//     this.username=username
//     this.email=email
//     this.password=password
// }

// User.prototype.encyptpassword=function(){
//     return `${this.password}123`
// }

// User.prototype.chnageusername=function(){
//     return `${this.username.toUpperCase()}`
// }

// const abc = new User("Mohammed","mohame@gmail.com","mohffs$df")
// console.log(abc.encyptpassword())
// console.log(abc.chnageusername())



// class User{
//     constructor(username,email,password){
//         this.username=username
//         this.email=email
//         this.password=password
//     }

//     encyptpassword(){
//         return `${this.password}123`
//     }

//     chnageusername(){
//         return `${this.username}`
//     }
// }


// class emp extends User{
// }
// const obj = new emp("Mohammed","mohd@gmail.com","i@#didhid")
// console.log(obj.encyptpassword())
// console.log(obj.chnageusername())




// function myfunc(username){
//     this.username=username
//     console.log("called")
// }
// myfunc("testing")

// function mycall(username,email,password){
//     myfunc(username)// if we call this then the functions will be called but there referece or all the things which is inside that functions will be remove so for that we use ".CALL()"
//     myfunc.call(this,username)// .call store the reference of the myfunc "call will pass the current executions to the other "
//     this.email=email
//     this.password=password
// }

// const obj1 = new mycall("xyz","xyz@gmail.com",123)
// const obj2 = new mycall("abc","abc@gmail.com",1122)
// console.log(obj1)
// console.log(obj2)




//-----------------------------------------

// class User{
//     constructor(username,email,password){
//         this.username=username
//         this.email=email
//         this.password=password
//     }

//     encyptpassword(){
//         return `${this.password}123`
//     }

//     chnageusername(){
//         return `${this.username.toUppperCase()}`
//     }
// }

// const obj = new User("Mohammed","mohame@gmail.com","mohffs$df")
// console.log(obj.encyptpassword())
// console.log(obj.chnageusername())


//------------------------------------------------------

// behind Scene of this class base option

// function User(username,email,password){
//     this.username=username
//     this.email=email
//     this.password=password
// }

// User.prototype.encyptpassword=function(){
//     return `${this.password}123`
// }

// User.prototype.chnageusername=function(){
//     return `${this.username.toUpperCase()}`
// }

// const abc = new User("Mohammed","mohame@gmail.com","mohffs$df")
// console.log(abc.encyptpassword())
// console.log(abc.chnageusername())





class User{
    constructor(username,email,password){
        this.username=username
        this.email=email
        this.password=password
    }

    encyptpassword(){
        return `${this.password}123`
    }

    chnageusername(){
        return `${this.username}`
    }
}


class emp extends User{

}

const obj = new emp("Mohammed","mohd@gmail.com","i@#didhid")
console.log(obj.encyptpassword())
console.log(obj.chnageusername())



// -----------------------------------
const a =  Object.getOwnPropertyDescriptor(Math,"PI")
// {
//     value: 3.141592653589793,
//     writable: false,
//     enumerable: false,
//     configurable: false
//   }


console.log(a)


let mypi = Math.PI
mypi = 3.14
console.log(mypi)


// ------------------------------------

// lexical scope 

function outer(){
    let username = "xyz" // this is called lexical scope this variable is accessible in the inner function however we cannot access it outside the functions
    function inner(){
        let s = "abc"
        console.log(username)
    }
    inner()
    function innertwo(){
        console.log(username)
        console.log(s)// this s is not accessible because the varibale is decalre inside the functions of the above funtion so in lexical scope we can access the parent property but we cannot access our varible of children functions 
    }
    innertwo()
}
outer()
// console.log(username)



// -------------------------------------























































































// -----------






















































































































































































































