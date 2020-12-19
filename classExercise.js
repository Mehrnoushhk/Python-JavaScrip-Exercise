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
myDog = new Dog('Lucy', 1982);
console.log('My dog Name is ' + myDog.dogName);
console.log('She is ' + myDog.age() + ' years old');