# CAP Bookshop - Training Example

The Bookshop service built in the SAP CAP (Cloud Application Programming Model) getting-started session.

## Project structure

| Folder / File | Purpose |
|---|---|
| `db/schema.cds` | Domain model: `Books` and `Authors` |
| `db/data/*.csv` | Sample data, loaded automatically on startup |
| `srv/cat-service.cds` | `CatalogService` exposing Books, Authors and the `submitOrder` action |
| `srv/cat-service.js` | Custom logic: discount label on Books and the `submitOrder` handler |

## Prerequisites

- Node.js 22 or 24 LTS
- CAP development kit: `npm i -g @sap/cds-dk`
- VS Code with the *SAP CDS Language Support* extension

## Run it

```sh
npm i
cds watch
```

Then open:

- http://localhost:4004/odata/v4/catalog/Books
- http://localhost:4004/odata/v4/catalog/Books?$filter=stock gt 100&$expand=author
- http://localhost:4004/odata/v4/catalog/$metadata

## Homework

1. Add a `Reviews` entity (rating, comment) linked to `Books`.
2. Add a `before('CREATE', 'Reviews')` handler that rejects ratings outside 1-5.
3. Write a Python script that posts three reviews and prints the average rating per book.

## Learn more

- CAP documentation: https://cap.cloud.sap
- Sample code: https://github.com/SAP-samples/cloud-cap-samples
