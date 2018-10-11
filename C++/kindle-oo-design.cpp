/*
Design Kindle, which can support 3 type of book format: PDF, MOBI and EPUB.

- Consider using ENUM for book format.
- Consider using simple factory to create reader for each format.

Example
Input:
readBook("EPUB")
readBook("PDF")
readBook("MOBI")

Output:
Using EPUB reader, book content is: epub
Using PDF reader, book content is: pdf
Using MOBI reader, book content is: mobi

Solution:
    EBookReaderFactory *factory = new EBookReaderFactory;
    EBookReader *ebook = factory->createReader(Book *b); // switch to get the reader subclass
    ebook->readbook();
*/

const char* names[] = { "epub","pdf","mobi" };

enum Format { EPUB, PDF, MOBI };

class Book {
private:
    Format format;

public:
    Book(Format format) {
        this->format = format;
    }

    Format getFormat() {
        return format;
    }
};

class EBookReader {
protected:
    Book *book;

public:

    EBookReader(Book *b) {
        this->book = b;
    }

    string readBook() {
        return reader->displayReaderType() + ", book content is: " + names[book->getFormat()];
    }

    virtual string displayReaderType() = 0;
};

class EpubReader :public EBookReader {
public:
    EpubReader(Book *b):EBookReader(b){}

    string displayReaderType() {
        return "Using EPUB reader";
    }
};

class MobiReader :public EBookReader {
public:
    MobiReader(Book *b):EBookReader(b){}

    string displayReaderType() {
        return "Using MOBI reader";
    }
};

class PdfReader :public EBookReader {
public:
    PdfReader(Book *b):EBookReader(b){}

    string displayReaderType() {
        return "Using PDF reader";
    }
};

class EBookReaderFactory {
public:

    EBookReader *createReader(Book *b) {
        switch (b->getFormat()) {
            case EPUB:
                return new EpubReader(b);
            case MOBI:
                return new MobiReader(b);
            case PDF:
                return new PdfReader(b);
            default:
                return NULL;
        }
    }
};

class Kindle {
private:
    vector<Book *> *books;
    EBookReaderFactory *readerFactory;

public:
    Kindle() {
        books = new vector<Book *>;
        readerFactory = new EBookReaderFactory;
    }

    string readBook(Book *book) {
        EBookReader *reader = readerFactory->createReader(book);
        return reader->readBook();
    }

    void downloadBook(Book *b) {
        books->push_back(b);
    }

    void uploadBook(Book *b) {
        books->push_back(b);
    }

    void deleteBook(Book *b) {
        vector<Book *>::iterator it;
        for (it = books->begin(); it != books->end(); it++) {
            if ((*it)->getFormat() == b->getFormat()) {
                books->erase(it);
                return;
            }
        }
    }
};
