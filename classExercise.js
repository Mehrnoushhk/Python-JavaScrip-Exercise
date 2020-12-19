// * Example 1
class Dog {
    constructor(dogName, birthDate){
        this.dogName = dogName;
        this.birthDate = birthDate;
    }
    age(){
        let date = new Date();
        console.log(date);
        return date.getFullYear() - this.birthDate;
    }
}
// myDog = new Dog('Lucy', 1982);
// console.log('My dog Name is ' + myDog.dogName);
// console.log('She is ' + myDog.age() + ' years old');

// * Example 2
// * Define car object with 2 properties (speed, brand, model) and 3 methods (breake, accelerate, describe, decelerate)

class Car {
    constructor(brand, model) {
        this.brand = brand;
        this.model = model;
        this.speed = 0;
        this.motion = 'The car is at rest'
    }
    motionCheck() {
        if (this.speed > 0) {
            this.motion = 'The car is moving';
        }
        else {
            this.motion = 'The car is at rest';
        }
    }
    accelerate(amount) {
        this.speed += amount;
        this.motionCheck();
    }
    decelerate(amount) {
        if (amount <= this.speed) {
            this.speed -= amount;
        } else {
            this.speed = 0;
        }
        this.motionCheck();
    }
    break() {
        this.speed = 0;
        this.motionCheck();
    }
    describe() {
        console.log(`The car brand is ${this.brand} and its model is ${this.model} ${this.motion}`)
    }

}
myCar = new Car('BMW', 'X6');
myCar.describe();
myCar.accelerate(60);
console.log(myCar.describe());
myCar.decelerate(40);
console.log(myCar.describe());
myCar.break();
console.log(myCar.describe());
