import java.util.ArrayList;
import java.util.List;

public class Kindle {
    private List<Book> books;
    private EBookReaderFactory readerFactory;

    public Kindle() {
        books = new ArrayList<>();
        readerFactory = new EBookReaderFactory();
    }

    public String readBook(Book book) throws Exception {
        EBookReader reader = readerFactory.createReader(book);
        if (reader == null) {
            throw new Exception("Can't read this format");
        }
        return reader.readBook();
    }

    public void downloadBook(Book b) {
        books.add(b);
    }

    public void uploadBook(Book b) {
        books.add(b);
    }

    public void deleteBook(Book b) {
        books.remove(b);
    }
}

enum Format {
    EPUB("epub"), PDF("pdf"), MOBI("mobi");

    private String content;

    Format(String content) {
        this.content = content;
    }

    public String getContent() {
        return content;
    }
}

class Book {
    private Format format;

    public Book(Format format) {
        this.format = format;
    }

    public Format getFormat() {
        return format;
    }
}

class EBookReaderFactory {
    public EBookReader createReader(Book b) {
        switch (b.getFormat()) {
            case EPUB:
                return new EpubReader(b);
            case MOBI:
                return new MobiReader(b);
            case PDF:
                return new PdfReader(b);
            default:
                return null;
        }
    }
}

abstract class EBookReader {
    protected Book book;
    
    public EBookReader(Book b){
        this.book = b;
    }
    
    public String readBook() {
        return displayReaderType() + ", book content is: " + this.book.getFormat().getContent();
    }

    public abstract String displayReaderType();
}

class EpubReader extends EBookReader{
    public EpubReader(Book b) {
        super(b);
    }

    @Override
    public String displayReaderType() {
        return "Using EPUB reader";
    }
}

class MobiReader extends EBookReader {
    public MobiReader(Book b) {
        super(b);
    }

    @Override
    public String displayReaderType() {
        return "Using MOBI reader";
    }
}

class PdfReader extends EBookReader{
    public PdfReader(Book b) {
        super(b);
    }

    @Override
    public String displayReaderType() {
        return "Using PDF reader";
    }
}
