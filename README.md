# SAP CAP Bookshop

A Bookshop application built using the **SAP Cloud Application Programming Model (CAP)** and **OData V4**. This project demonstrates data modeling with CDS, service projections, custom business logic, review management, and Python integration.

## Features

- **Books and Authors:** CDS data model with associations between books and authors.
- **Catalog Service:** Exposes Books, Authors, and Reviews through OData V4.
- **Discount Logic:** Displays a discount label for books with stock greater than 100.
- **Order Processing:** Custom `submitOrder` action that reduces stock when sufficient quantity is available.
- **Review Management:** Supports submitting book reviews with ratings and comments.
- **Rating Validation:** Rejects reviews with ratings outside the range of 1–5.
- **Python Integration:** A Python script submits three reviews and calculates the average rating for each selected book.

## Project Structure

| Folder / File | Purpose |
|---|---|
| `db/schema.cds` | Defines Books, Authors, and Reviews entities and their relationships |
| `db/data/*.csv` | Contains sample data loaded by CAP |
| `srv/cat-service.cds` | Defines CatalogService and exposes Books, Authors, Reviews, and the `submitOrder` action |
| `srv/cat-service.js` | Implements discount logic, order processing, and review rating validation |
| `post_reviews.py` | Posts three reviews through OData and calculates average ratings |

## Prerequisites

- Node.js (compatible LTS version)
- npm
- SAP CDS Language Support extension for VS Code (recommended)
- Python 3
- Python `requests` package

## Getting Started

Clone the repository:

```bash
git clone https://github.com/KirthigaManivannan/SAP-CAP-Bookshop.git
cd SAP-CAP-Bookshop
```

Install dependencies:

```bash
npm install
```

Start the CAP development server:

```bash
npx cds watch
```

The application should be available at:

`http://localhost:4004`

## OData Endpoints

| Endpoint | Description |
|---|---|
| `/odata/v4/catalog/Books` | Retrieve books |
| `/odata/v4/catalog/Authors` | Retrieve authors |
| `/odata/v4/catalog/Reviews` | Retrieve book reviews |
| `/odata/v4/catalog/$metadata` | View OData service metadata |

Example query to retrieve books with stock greater than 100 and their authors:

```text
http://localhost:4004/odata/v4/catalog/Books?$filter=stock gt 100&$expand=author
```

## Run the Python Review Script

Make sure the CAP server is running in a separate terminal.

Install the required Python package:

```bash
python -m pip install requests
```

Run the script from the project directory:

```bash
python post_reviews.py
```

The script selects two books, submits three reviews through the OData service, retrieves the reviews, and prints the average rating for each selected book.

## Testing Rating Validation

Reviews must have an integer rating between 1 and 5.

- Ratings from 1 to 5 are accepted.
- Ratings below 1, above 5, or non-integer ratings are rejected with an HTTP 400 response.
  
## Technologies Used

- **SAP Cloud Application Programming Model (CAP)** – Application development framework
- **CDS (Core Data Services)** – Data modeling and service definitions
- **Node.js** – Backend runtime
- **JavaScript** – Custom business logic and event handlers
- **OData V4** – RESTful data access and service integration
- **SQLite** – Development database
- **Python** – Review submission and average rating calculation
- **Python Requests** – HTTP requests to the OData service
- **Visual Studio Code** – Development environment
- **Git and GitHub** – Version control and source code hosting
  
## References

- [SAP CAP Documentation](https://cap.cloud.sap/)
- [SAP CAP Samples on GitHub](https://github.com/SAP-samples/cloud-cap-samples)
- [SAP CDS Language Support for Visual Studio Code](https://marketplace.visualstudio.com/items?itemName=SAPSE.vscode-cds)
- [Node.js](https://nodejs.org/)
- [Python Documentation](https://docs.python.org/3/)
- [Requests Documentation](https://requests.readthedocs.io/en/latest/)
- [Project Repository – SAP CAP Bookshop](https://github.com/KirthigaManivannan/SAP-CAP-Bookshop)

