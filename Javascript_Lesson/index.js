// a comment - this is my first js script code
console.log("Hello World");
console.log("This is my second log");
console.log("This is my third log");

let name = "ibrahim";
console.log(name);

const homeTown = "owo";
console.log(homeTown)

let age = 30;
let drinksAlcohol = false;

console.log(drinksAlcohol)
console.log(age)

let cousin = {
    id: "Kamil",
    locality: "Owo"
};
// you can use the dot notation to change the property of cousin
cousin.id = "Taofeeq"
console.log(cousin.id);

// another way to change the name is to use the bracket notation
cousin["id"] = "Kamil"; // we change the name back from taofeeq to kamil
console.log(cousin.id);

// some properties of a variable
console.log(cousin.id.length)
console.log(cousin.id.split(""))
console.log(cousin.id.toUpperCase())


const myColours = ["yellow", "green", "blue", "white", "black"];
myColours.push("indigo");
myColours.unshift("berries");
console.log(myColours)
console.log(myColours[0]);
myColours[3] = "Pink"
myColours.pop();   // this removed that last item in the array
console.log(myColours)

// To check if a variable is an array, use the following
console.log(Array.isArray(myColours));

console.log(myColours.indexOf("white"));


function identity(id, locality) {
    console.log("Hello my name is and I come from " + locality);
    // a better way to do this is by using template strings
    console.log(`Hello my name is ${id} and I come from ${locality}`)
}

identity("Ibrahim","owo");
identity("Kamil", "okedogbon");


function calculateSquare(number) {
    return number * number
}
let result = calculateSquare(5)
console.log(result)
// another way to do the above is 
console.log(calculateSquare(5))

const profile = {
    hisName: "Anas",
    hisAge: 2,
    complexion: "fair",
    handsome: true,
    hobbies:["cooing","youtube","eating","running"],
    address: {
        street: "Hogan Point Ct",
        no: 5075,
        zipCode: 27127,
        city: "Winston Salem",
        state: "NC",
        country: "USA",
    }
}
profile.email = "anas@cooing.com"
console.log(`His name is ${profile.hisName} and he is ${profile.hisAge} years old`);
console.log(`One of ${profile.hisName}'s hobbies is ${profile.hobbies[2]}`);
console.log(profile)


const todos = [
    {
        id: 1,
        task: "learn python",
        state: "completed",
    },
    {
        id: 2,
        task: "learn javascript",
        state: "ongoing",
    },
    {   id: 3,
        task: "learn flask",
        state: "not started",
    }
];

console.log(todos);
console.log(todos[1].task);

const todosJSON = JSON.stringify(todos);
console.log(todosJSON);

for (let x = 0; x < todos[1].state.length; x++) {
    console.log(x)
}

/// A better way to loop through an array is 
for(let todo of todos) {
    console.log(todo);
}

//ForEach

todos.forEach(function(work) {
    console.log(todos.task);
});