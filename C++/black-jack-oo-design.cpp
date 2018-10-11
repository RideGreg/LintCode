/*
- 每位玩家起始有1000筹码
- 庄家有10000筹码
- 如果玩家获胜，双倍获得押注的筹码
- 庄家获胜，玩家押注的筹码归庄家
- 点数相同，庄家获胜
- A 可当做 1 或 11

Example:
Player(10) // Player #1 bet 筹码 10 from his all 筹码
Player(100) // Player #2 bet 筹码 100 from his all 筹码
Player(500) // Player #3 bet 筹码 500 from his all 筹码
Card([1,4,2,3,1,4,2,3,9,10]) // stack of cards, goes to player 1, 2, 3 ... and dealer.
InitialCards()
compareResult()

You should return below:
playerid: 1 ;Cards: 1 , 1; Current best value is: 12, current bets: 10, total bets: 990
playerid: 2 ;Cards: 4 , 4; Current best value is: 8, current bets: 100, total bets: 900
playerid: 3 ;Cards: 2 , 2; Current best value is: 4, current bets: 500, total bets: 500
Dealer Cards: 3 , 3; Current best value is: 6, total bets: 10000
playerid: 1 ;Cards: 1 , 1; Current best value is: 12, current bets: 0, total bets: 1010
playerid: 2 ;Cards: 4 , 4; Current best value is: 8, current bets: 0, total bets: 1100
playerid: 3 ;Cards: 2 , 2; Current best value is: 4, current bets: 0, total bets: 500
Dealer Cards: 3 , 3; Current best value is: 6, total bets: 10390

Solution: player/dealer should own cards and bets 筹码.
BlackJack game object should own method to deal cards, compare results and handle bets.

classes
BlackJack: vector<NormalPlayer *> *players; Dealer *dealer; vector<Card *> *cards;

    ctor will init cards and add players
    void dealInitialCards() // distribute cards to player 1, 2, 3... and dealer
    void compareResult() // follow win-lose rule to handle bets that are put down by players

NormalPlayer:
    Hand *hand; // necessary
    int totalBets; // necessary
    int bets; // necessary
    BlackJack *game;
    int id;
    bool StopDealing;

    void insertCard(Card *card) // call Hand::insertCard(Card *card)
    void placeBets(int amount) // move some from totalBets to bets
    int getBestValue()
    void win()
    void lose()

Dealer:
    Hand *hand; // necessary
    int bets; // necessary
    BlackJack *game;

    void insertCard(Card *card) // call Hand::insertCard(Card *card)
    bool largerThan(NormalPlayer *p) // compare cards value
    void updateBets(int amount)

Card: int value

Hand: vector<Card *> *cards;

    int getBestValue() // calculate all possible total values, pick the best
    void insertCard(Card *card)
*/

class Card {
private:
    int value;

public:
    Card(int value) {
        this->value = value;
    }

    int getValue() {
        return value;
    }
};

class Hand {
private:
    vector<Card *> *cards;

public:
    Hand() {
        cards = new vector<Card *>();
    }

    vector<int> *getPossibleValues() {
        vector<int> *results = new vector<int>;

        int aceCount = 0;
        int resultWithoutAce = 0;
        for (Card *card : (*cards)) {
            if (card->getValue() == 1) {
                aceCount++;
            } else if (card->getValue() == 11 || card->getValue() == 12 || card->getValue() == 13) {
                resultWithoutAce += 10;
            } else {
                resultWithoutAce += card->getValue();
            }
        }

        for (int i = 0; i <= aceCount; i++) {
            int ones = i;
            int elevens = aceCount - i;

            results->push_back(resultWithoutAce + ones + elevens * 11);
        }

        return results;
    }

    int getBestValue() {
        vector<int> *results = getPossibleValues();

        int maxUnder = -1;
        for (int result : (*results)) {
            if (result <= 21 && result > maxUnder) {
                maxUnder = result;
            }
        }
        return maxUnder;
    }

    void insertCard(Card *card) {
        cards->push_back(card);
    }

    string printHand() {
        string res = "Cards: ";
        for (int i = 0; i < cards->size(); i++) {
            res += to_string(cards->at(i)->getValue());
            if (i != (int)(cards->size()) - 1) {
                res += " , ";
            } else {
                res += ';';
            }
        }
        res += " Current best value is: " + to_string(getBestValue());
        return res;
    }
};

class BlackJack;

class NormalPlayer {
private:
    BlackJack *game;
    int id;
    Hand *hand;
    int totalBets;
    int bets;
    bool StopDealing;

public:
    NormalPlayer(int id, int bets) {
        this->id = id;
        hand = new Hand();
        totalBets = 1000;
        try {
            placeBets(bets);
        } catch (string e) {
            cout << e << endl;
        }
        StopDealing = false;
    }

    void placeBets(int amount) {
        if (totalBets < amount) {
            throw "No enough money.";
        }
        bets = amount;
        totalBets -= bets;
    }

    int getId() {
        return this->id;
    }

    void insertCard(Card *card) {
        hand->insertCard(card);
    }

    int getBestValue() {
        return hand->getBestValue();
    }

    void stopDealing() {
        this->StopDealing = true;
    }

    void joinGame(BlackJack *game);

    void dealNextCard();

    int getCurrentBets() {
        return bets;
    }

    string printPlayer() {
        return hand->printHand()+ ", current bets: " + to_string(bets) + ", total bets: " + to_string(totalBets) + "\n";
    }

    void win() {
        totalBets += bets * 2;
        bets = 0;
    }

    void lose() {
        bets = 0;
    }
};

class Dealer {
private:
    BlackJack *game;
    Hand *hand;
    int bets;
public:
    Dealer() {
        hand = new Hand();
        bets = 10000;
    }

    void insertCard(Card *card) {
        hand->insertCard(card);
    }

    bool largerThan(NormalPlayer *p) {
        return hand->getBestValue() >= p->getBestValue();
    }

    void updateBets(int amount) {
        bets += amount;
    }

    void setGame(BlackJack *game);

    void dealNextCard();

    string printDealer()
    {
        return "Dealer " + hand->printHand() + ", total bets: " + to_string(bets) + "\n";
    }
};

class BlackJack {
private:
    vector<NormalPlayer *> *players;
    Dealer *dealer;
    vector<Card *> *cards;
public:
    BlackJack() {
        players = new vector<NormalPlayer *>;
        dealer = new Dealer;
    }

    void initCards(vector<Card *> *cards) {
        this->cards = cards;
    }

    void addPlayer(NormalPlayer *p) {
        players->push_back(p);
    }

    void dealInitialCards() {
        for (NormalPlayer *player : (*players)) {
            player->insertCard(dealNextCard());
        }
        dealer->insertCard(dealNextCard());

        for (NormalPlayer *player : (*players)) {
            player->insertCard(dealNextCard());
        }
        dealer->insertCard(dealNextCard());
    }

    Card *dealNextCard() {
        Card *card = *(cards->begin());
        cards->erase(cards->begin());
        return card;
    }

    Dealer *getDealer() {
        return dealer;
    }

    void compareResult() {
        for (NormalPlayer *p : (*players)) {
            if (dealer->largerThan(p)) {
                dealer->updateBets(p->getCurrentBets());
                p->lose();
            } else {
                dealer->updateBets(-(p->getCurrentBets()));
                p->win();
            }
        }
    }

    string print() {
        string s = "";
        for (NormalPlayer *player : (*players)) {
            s += "playerid: " + to_string((player->getId() + 1)) + " ;" + player->printPlayer();
        }
        return s;
    }
};

void NormalPlayer::joinGame(BlackJack *game) {
    this->game = game;
    game->addPlayer(this);
}

void NormalPlayer::dealNextCard() {
    insertCard(game->dealNextCard());
}

void Dealer::setGame(BlackJack *game) {
    this->game = game;
}

void Dealer::dealNextCard() {
    insertCard(game->dealNextCard());
}