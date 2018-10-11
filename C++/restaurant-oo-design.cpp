/*
设计餐馆

- 不能预订座位
- 不能订外卖
- 餐馆的桌子有不同大小
- 餐馆会优先选择适合当前Party最小的空桌
- 需要实现Restaurant Class
- 每次调用findTable, takeOrder, checkOut之后都会调用restaurantDescription, 来验证你的程序是否正确。

Example
meal(10.0) // 创建Meal_1, price是10.0
meal(13.0) // 创建Meal_2, price是13.0
meal(17.0) // 创建Meal_3, price是17.0
table(4)   // 创建table_1
table(4)   // 创建table_2
table(10)  // 创建table_3
party(3)   // 创建party_1
party(7)   // 创建party_2
party(4)   // 创建party_3
party(6)   // 创建party_4
party(1)   // 创建party_5
order(1)   // order meal_1
order(2,3) // order meal_2 & meal_3
findTable(1) // find table for party_1
findTable(3) // find table for party_3
findTable(4)
takeOrder(1, 1) // table, order
takeOrder(3, 2)
checkOut(3) // table
findTable(4)

Table: 0, table size: 4, isAvailable: false. No current order for this table.
Table: 1, table size: 4, isAvailable: true. No current order for this table.
Table: 2, table size: 10, isAvailable: true. No current order for this table.
*****************************************
Table: 0, table size: 4, isAvailable: false. No current order for this table.
Table: 1, table size: 4, isAvailable: false. No current order for this table.
Table: 2, table size: 10, isAvailable: true. No current order for this table.
*****************************************
Table: 0, table size: 4, isAvailable: false. No current order for this table.
Table: 1, table size: 4, isAvailable: false. No current order for this table.
Table: 2, table size: 10, isAvailable: false. No current order for this table.
*****************************************
Table: 0, table size: 4, isAvailable: false. Order price: 10.0.
Table: 1, table size: 4, isAvailable: false. No current order for this table.
Table: 2, table size: 10, isAvailable: false. No current order for this table.
*****************************************
Table: 0, table size: 4, isAvailable: false. Order price: 10.0.
Table: 1, table size: 4, isAvailable: false. No current order for this table.
Table: 2, table size: 10, isAvailable: false. Order price: 30.0.
*****************************************
Table: 0, table size: 4, isAvailable: false. Order price: 10.0.
Table: 1, table size: 4, isAvailable: false. No current order for this table.
Table: 2, table size: 10, isAvailable: true. No current order for this table.
*****************************************
Table: 0, table size: 4, isAvailable: false. Order price: 10.0.
Table: 1, table size: 4, isAvailable: false. No current order for this table.
Table: 2, table size: 10, isAvailable: false. No current order for this table.
*****************************************

Solution: Table is most important class which holds orders on this table (holding party is not useful in this problem).

classes
Meal: float price;

Order: vector<Meal*> *meals;
    Order * mergeOrder(Order *order);
    float getBill();

Party: int size;

Table: int capacity; bool available; Order * order;

    void markAvailable();
    void markUnavailable();
    void setOrder(Order *o); // may clear order on the table in checkout

Restaurant:  vector<Table*> *tables; vector<Meal*> *menu;

    void findTable(Party *p); // set a table unavailable
    void takeOrder(Table *t, Order *o); // set a table's order
    float checkOut(Table *t); // return bill, reset table's availability and order
    void addTable(Table *t); // sort table in the order of capacity
*/

class Meal {
private:
    float price;
    
public:
    Meal(float price) {
        this->price = price;
    }
    
    float getPrice() {
        return this->price;
    }
};

class Order {
private:
    vector<Meal*> *meals;
    
public:
    Order() {
        meals =new vector<Meal*>;
    }
    
    vector<Meal*>* getMeals() {
        return meals;
    }
    
    Order* mergeOrder(Order *order) {
        Order* ans = new Order;
        for(Meal* &meal : *(this->getMeals())) {
            ans->meals->push_back(meal);
        }
        if(order != NULL) {
            for(Meal* &meal : *(order->getMeals())) {
                ans->meals->push_back(meal);
            }
        }
        return ans;
    }
    
    float getBill() {
        float bill = 0;
        for(int i = 0; i < meals->size(); i++) {
            bill += (*meals)[i]->getPrice();
        }
        return bill;
    }
};

class Party {
private:
        int size;
    
public:
    Party(int size) {
        this->size = size;
    }
    
    int getSize() {
        return this->size;
    }
};

class Table {
private:
    int capacity;
    bool available;
    Order *order;
    
public:
    Table(int capacity) {
        this->capacity = capacity;
        available =true;
        order = NULL;
    }
    
    int getCapacity() {
        return this->capacity;
    }
    
    bool isAvailable() {
        return this->available;
    }
    
    void markAvailable() {
        this->available = true;
    }
    
    void markUnavailable() {
        this->available = false;
    }
    
    Order * getCurrentOrder() {
        return this->order;
    }
    
    void setOrder(Order *o) {
        if (o == NULL || order = NULL) { // clear order
            this->order = o;
        } else {
            order = order->mergeOrder(o);
        }
    }
};

class Restaurant {
private:
    vector<Table *> *tables;
    vector<Meal *> *menu;
    
public:
    Restaurant() {
        tables = new vector<Table *>;
        menu = new vector<Meal *>;
    }
    
    void findTable(Party *p) {
        for(Table* &t: *tables) {
            if(t->isAvailable() && t->getCapacity() >= p->getSize()) {
                t->markUnavailable();
                return;
            }
        }
    }
    
    void takeOrder(Table *t,Order *o) {
        t->setOrder(o);
    }
    
    float checkOut(Table *t) {
        Order *o = t->getCurrentOrder();
        float bill = o ? o->getBill() : 0.0;
        t->markAvailable();
        t->setOrder(NULL);
        return bill;
    }
    
    vector<Meal *>* getMenu() {
        return menu;
    }
    
    void addTable(Table *t) {
        vector<Table *>::iterator it;
        for(it = tables->begin(); it!=tables->end(); it++) {
            if((*it)->getCapacity() > t->getCapacity()) {
                tables->insert(it,t);
                return;
            }
        }
        tables->push_back(t);
    }
    
    string to_string(int x) {
        string ans;
        stringstream st;
        st << x;
        st >> ans;
        return ans;
    }
    
    string restaurantDescription() {
        string description = "";
        for(int i = 0; i < tables->size(); i++) {
            Table* table = (*tables)[i];
            description += "Table: " + to_string(i) + ", table size: " 
            + to_string(table->getCapacity()) + ", isAvailable: " +(table->isAvailable()?"true":"false") + ".";
            if(table->getCurrentOrder() == NULL)
                description += " No current order for this table";
            else 
            {
                description +=  " Order price: " + to_string(table->getCurrentOrder()->getBill())+".0";
            }
            description += ".\n";
        }
        description += "*****************************************\n";
        return description;
    }
    
};
