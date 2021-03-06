var gummyBearFlavors = [{
        flavor: "cherry",
        color: "red"
    },
    {
        flavor: "strawberry",
        color: "red"
    },
    {
        flavor: "mango",
        color: "yellow"
    },
    {
        flavor: "pineapple",
        color: "yellow"
    },
    {
        flavor: "lemon",
        color: "yellow"
    },
    {
        flavor: "orange",
        color: "orange"
    },
    {
        flavor: "green apple",
        color: "green"
    },
    {
        flavor: "watermelon",
        color: "red"
    },
    {
        flavor: "pink grapefruit",
        color: "pink"
    },
    {
        flavor: "lime",
        color: "green"
    },
    {
        flavor: "blue rasberry",
        color: "blue"
    },
    {
        flavor: "grape",
        color: "purple"
    }
];

// all functions in this code drill require the use of the .map() method as well as => fat arrow syntax

// create a function that console logs "my favorite gummy bear flavor is <flavor>" for each item in the array.
var favoriteFlavors = gummyBearFlavors.map(gummy => {
    console.log(`my favorite gummy bear flavor is ${gummy.flavor}`);
});

// create a function that returns a string that looks like "<number>. <flavor> gummy bears are <color>." for each item in the array. console log the function
var numberedFlavors = gummyBearFlavors.map((gummy, index) => {
    return `${index}. ${gummy.flavor} gummy bears are ${gummy.color}.`
});

console.log(numberedFlavors)

// create a function that checks whether an item in the array has flavors that are either red or yellow and pushes them to new arrays called redFlavor and yellowFlavor.
var redFlavor = [];
var yellowFlavor = [];

var colorCheck = gummyBearFlavors.map(gummy =>{
    if(gummy.color === "red"){
        redFlavor.push(gummy);
    }
    if(gummy.color === "yellow"){
        yellowFlavor.push(gummy);
    }
});

// using the new arrays, create a function that console logs "<flavor name> flavored gummy bears are <color>. mmm delicious!"
var delicious = redFlavor.map(gummy => {
    console.log(`${gummy.flavor} flavored gummy bears ${gummy.color}. mmm delicious!`)
});
var delicious = yellowFlavor.map(gummy => {
    console.log(`${gummy.flavor} flavored gummy bears ${gummy.color}. mmm delicious!`)
});