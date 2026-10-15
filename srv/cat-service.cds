using my.bookshop as my from '../db/schema';

service CatalogService {
  entity Books   as projection on my.Books;
  entity Authors as projection on my.Authors;
  action submitOrder(book : Integer, quantity : Integer);
}
