"use strict";
/*
let books = 
[
    {
      "id": 1,
      "title": "The Divine Comedy",
      "author": "Dante Alighieri",
      "date": dayjs('2019-10-24'),
      "reviews": 5
    },

    {
        "id": 2,
        "title": "The Prince",
        "author": "Niccolò Machiavelli",
        "date": dayjs('2019-12-30'),
        "reviews": 4
    },

    {
        "id": 3,
        "title": "Sotto le cuffie",
        "author": "Favij",
        "date": dayjs('2020-01-04'),
        "reviews": 1
    }
];

function aggiungiLibro(book)
{
    if(book && book.title && book.author && book.date)
    {
        let max = 0;
        for(a in books)
        {
            if(books.id > max)
                max = (books.id + 1);
        }

        book.id = max;
        books.push(book);
    }
}
*/
// Define an array of book objects.
// Each book is represented by the following properties:
// - A unique numeric id (required)
// - A title (required)
// - The author (required)
// - The publication date, expressed using the day.js library (required)
// - A number from 1 to 5 representing the average review for the book (optional)
var books = [  {    id: 1,    title: "The Catcher in the Rye",    author: "J. D. Salinger",    publicationDate: dayjs("1951-07-16"),    averageReview: 4.5  },  {    id: 2,    title: "To Kill a Mockingbird",    author: "Harper Lee",    publicationDate: dayjs("1960-07-11"),    averageReview: 5  },  {    id: 3,    title: "The Great Gatsby",    author: "F. Scott Fitzgerald",    publicationDate: dayjs("1925-04-10"),    averageReview: 4  }];

// Define a function to add a book to the array.
// If all required properties are present, the book is added to the array.
function addBook(book) {
  if (book.id && book.title && book.author && book.publicationDate) {
    books.push(book);
  }
}

// Define a function to delete a book from the array.
// If the book is present in the array, it is deleted.
function deleteBook(book) {
  var bookIndex = books.findIndex(b => b.id === book.id);
  if (bookIndex >= 0) {
    books.splice(bookIndex, 1);
  }
}

// Define a function to calculate the average review for all books in the array.
function calculateAverageReview() {
  var totalReviews = 0;
  var numBooks = 0;
  books.forEach(book => {
    if (book.averageReview) {
      totalReviews += book.averageReview;
      numBooks++;
    }
  });
  return numBooks > 0 ? totalReviews / numBooks : 0;
}

// Define a function to delay the publication date for all books in the array by a specified number of days.
function delayPublicationDate(numDays) {
  books.forEach(book => {
    book.publicationDate = book.publicationDate.add(numDays, "day");
  });
}

// Test the functions.

// Add a new book.
addBook({
  id: 4,
  title: "The Adventures of Tom Sawyer",
  author: "Mark Twain",
  publicationDate: dayjs("1876-12-10")
});

// Delete a book.
deleteBook({
  id: 3
});

// Calculate the average review.
console.log("Average review:", calculateAverageReview());

// Delay the publication date for all books by 7 days.
delayPublicationDate(7);

// Print the updated array of books.
console.log("Updated books:", books);
  