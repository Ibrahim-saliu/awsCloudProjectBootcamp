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

const myColours = ["yellow", "green", "blue", "white", "black"];
console.log(myColours)
console.log(myColours[0]);
myColours[3] = "Pink"
console.log(myColours)

function identity(id, locality) {
    console.log("Hello my name is and I come from " + locality);
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

