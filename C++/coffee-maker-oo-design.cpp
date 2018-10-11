/*
Can you design a coffee maker, that take a coffee pack, and can simply make a cup of coffee.

- Coffee pack contains the recipe of the coffee, like how many milk / how many sugar to be added in the coffee
- Coffee maker can make coffee based on the recipe provided by the coffee pack
- Only consider 2 type of ingredients: sugar and milk
- the cost of Plain coffee is 2. Add one portion of milk/sugar will increase the cost by 0.5
- Consider use decorator design pattern

Example
Input:
pack(2, 3)
makeCoffee()

Output:
Cost for this coffee is: 4.5
Ingredients for this coffee is: Plain Coffee, Milk, Milk, Sugar, Sugar, Sugar
*/

class CoffeePack {
private:
    int neededMilk;
    int neededSugar;

public:
    CoffeePack(int neededMilk, int neededSugar) {
        this->neededMilk = neededMilk;
        this->neededSugar = neededSugar;
    }

    int getNeededMilk() {
        return neededMilk;
    }

    int getNeededSugar() {
        return neededSugar;
    }
};

class Coffee {
public:
    virtual double getCost() = 0;
    virtual string getIngredients() = 0;
};

class SimpleCoffee :public Coffee {
public:
    double getCost() {
        return 2;
    }

    string getIngredients() {
        return "Plain Coffee";
    }
};

class CoffeeDecorator :public Coffee {
protected:
    Coffee *decoratedCoffee;

public:
    CoffeeDecorator(Coffee *coffee) {
        this->decoratedCoffee = coffee;
    }

    double getCost() {
        return decoratedCoffee->getCost();
    }

    string getIngredients() {
        return decoratedCoffee->getIngredients();
    }
};

class WithMilk :public CoffeeDecorator {
public:

    WithMilk(Coffee *coffee):CoffeeDecorator(coffee){}

    double getCost() {
        return CoffeeDecorator::getCost() + 0.5;
    }

    string getIngredients() {
        return CoffeeDecorator::getIngredients() + ", Milk";
    }
};

class WithSugar :public CoffeeDecorator
{
public:

    WithSugar(Coffee *coffee):CoffeeDecorator(coffee){}

    double getCost() {
        return CoffeeDecorator::getCost() + 0.5;
    }

    string getIngredients() {
        return CoffeeDecorator::getIngredients() + ", Sugar";
    }
};

class CoffeeMaker {
public:
    Coffee *makeCoffee(CoffeePack *pack) {
        Coffee *coffee = new SimpleCoffee();

        for (int i = 0; i < pack->getNeededMilk(); i++) {
            coffee = new WithMilk(coffee);
        }

        for (int i = 0; i < pack->getNeededSugar(); i++) {
            coffee = new WithSugar(coffee);
        }
        return coffee;
    }
};
