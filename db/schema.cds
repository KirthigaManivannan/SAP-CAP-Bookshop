namespace my.bookshop;
using { managed } from '@sap/cds/common';

entity Books : managed {
  key ID : Integer;
  title  : String(111);
  stock  : Integer;
  price  : Decimal(9,2);
  author : Association to Authors;
}

entity Authors {
  key ID : Integer;
  name   : String(111);
  books  : Association to many Books on books.author = $self;
}
