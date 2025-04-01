import abc

class Document(abc.ABC):
    @abc.abstractmethod
    def open(self): pass

class PdfDocument(Document):
    def open(self): print("Opening PDF Document")

class WordDocument(Document):
    def open(self): print("Opening Word Document")


# WITHOUT FACTORY METHOD
def create_document_no_factory(doc_type: str) -> Document:
    """Client code directly creates objects based on type."""
    doc = None
    if doc_type == "pdf":
        doc = PdfDocument() # Client knows concrete classes
    elif doc_type == "word":
        doc = WordDocument() # Client knows concrete classes
    else:
        raise ValueError("Unknown document type")
    return doc
print("################# Without factory")
doc1 = create_document_no_factory("pdf")
doc1.open()
doc2 = create_document_no_factory("word")
doc2.open()

# This code is tightly coupled to concrete product classes (`PdfDocument`, `WordDocument`).
# If we add a new document type we will require modifying the client's creation logic (the `if/elif`).

# USING THE FACTORY METHOD
# Abstract Creator with the factory_method
class DocumentCreator(abc.ABC):
    @abc.abstractmethod
    def factory_method(self) -> Document:
        """The Factory Method"""
        pass

    def open_document(self):
        """Operation using the factory method"""
        document = self.factory_method() # Gets object via factory method
        document.open()                 # Uses the object

# Concrete Creators implementing the factory_method
class PdfCreator(DocumentCreator):
    def factory_method(self) -> Document:
        return PdfDocument() # Subclass decides which concrete class

class WordCreator(DocumentCreator):
    def factory_method(self) -> Document:
        return WordDocument() # Subclass decides which concrete class

# Client usage (with Factory) - Client interacts with abstract Creator
def client_code_factory(creator: DocumentCreator):
    """Client code works with a Creator instance."""
    creator.open_document() # Client doesn't know concrete Document class

# The client code (`client_code_factory`) only knows the abstract `DocumentCreator`.
# The creation logic is ruled by concrete creator subclasses (`PdfCreator`, `WordCreator`) using the `factory_method`.
#  Is we add new document type we just have to create new concrete creators.
print("#########Using factory pattern")
client_code_factory(PdfCreator())
client_code_factory(WordCreator())

