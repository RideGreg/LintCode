/*
Find top k frequent words with map reduce framework.

The mapper's key is the document id, value is the content of the document, words in a document are split by spaces.

For reducer, the output should be at most k key-value pairs, which are the top k words and their frequencies in this reducer.
The judge will take care about how to merge different reducers' results to get the global top k frequent words, so you don't need to care about that part.

The k is given in the constructor of TopK class.

Example:
Given document A =
"lintcode is the best online judge
I love lintcode"
and document B =
"lintcode is an online judge for coding interview
you can test your code online at lintcode"

The top 2 words and their frequencies should be
lintcode, 4
online, 3
*/

/**
 * Definition of Input:
 * template<class T>
 * class Input {
 * public:
 *     bool done(); 
 *         // Returns true if the iteration has elements or false.
 *     void next();
 *         // Move to the next element in the iteration
 *         // Runtime error if the iteration has no more elements
 *     T value();
 *        // Get the current element, Runtime error if
 *        // the iteration has no more elements
 * }
 * Definition of Document:
 * class Document {
 * public:
 *     int id; // document id
 *     string content; // document content
 * }
 */

class MyPair {
public:
    string key;
    int value;
    MyPair(string word, int times) {
        key = word;
        value = times;
    };

    bool operator<(const MyPair& obj) const {
        return value > obj.value || value == obj.value && key < obj.key;
    }
};

class TopKFrequentWordsMapper: public Mapper {
public:
    void Map(Input<Document>* input) {
        // Write your code here
        // Please directly use func 'output' to output 
        // the results into output buffer.
        // void output(string &key, int value);
        while (!input->done()) {
            vector<string> words = split(input->value().content, " ");
            for (string word : words) 
                if (word.size() > 0) {
                    output(word, 1);
                }
            input->next();
        }
    }

    vector<string> split(const string &str, string delim) {
        vector<string> results;
        int lastIndex = 0, index;
        while ((index = str.find(delim, lastIndex)) != string::npos) {
            results.push_back(str.substr(lastIndex, index - lastIndex));
            lastIndex = index + delim.length();
        }
        if (lastIndex != str.length()) {
            results.push_back(str.substr(lastIndex, str.length() - lastIndex));
        }
        return results;
    }
};


class TopKFrequentWordsReducer: public Reducer {
private:
    int k;
    priority_queue<MyPair> q;
public:
    void setUp(int k) {
        // initialize your data structure here
        this->k = k;
    }

    void Reduce(string &key, Input<int>* input) {
        // Write your code here
        int sum = 0;
        while (!input->done()) {
            sum += input->value();
            input->next();
        }
        
        MyPair pair(key, sum);
        if (q.size() < k)
            q.push(pair);
        else {
            q.push(pair);
            q.pop();
        }        
    }

    void cleanUp() {
        // Please directly use func 'output' to output 
        // the top k pairs <word, times> into output buffer.
        // void output(string &key, int &value);
        vector<MyPair> list;
        while (!q.empty()) {
            list.push_back(q.top());
            q.pop();
        }
        
        // reverse
        int n = list.size();
        for (int i = n - 1; i >=0; --i)
            output(list[i].key, list[i].value);
    }
};
