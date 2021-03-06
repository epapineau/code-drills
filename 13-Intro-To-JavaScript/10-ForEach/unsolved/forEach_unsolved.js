const diners = [
  {
    name: 'Jerome',
    happiness: 80,
    hunger: 75
  },
  {
    name: 'Jimmy',
    happiness: 80,
    hunger: 20
  },
  {
    name: 'Robert',
    happiness: 70,
    hunger: 20
  },
  {
    name: 'Eric',
    happiness: 50,
    hunger: 80
  }
];

// Using the ForEach method, iterate through each object and increase happiness by 20, and decrease hunger by 20.
diners.forEach(function(diner) {
  diner.happiness += 20;
  diner.hunger -= 20;
});

// Console log the updated 'diners' object
console.log(diners)

// Using the ForEach method, console log the name of each diner if happiness is 100;
diners.forEach(function(diner){
  if(diner.happiness === 100){
    console.log(diner.name)
  }
});

// Using the ForEach method, if a diner's hunger is at 0, increase hunger to 100 and decrease happiness by 40
// Also print the following with their name "Person ate bad lobster" and "Person's hunger is now 100." Example: "Jerome ate bad lobster" and "Jerome's hunger is now 100."
diners.forEach(function(diner){
  if(diner.hunger === 0){
    diner.hunger = 100;
    diner.happiness -= 40;
    console.log(`${diner.name} ate bad lobster.`)
    console.log(`${diner.name}'s hunger is now 100.`)
  }
});