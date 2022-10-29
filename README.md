# Software Requirements Specification

## Project description

Simple e-commerce API for a smartphone store.

## Purpose

The purpose of this document is to describe the requirements for the e-commerce API.

# Features

- [ ] Add a new product
- [ ] List all products
- [ ] Get a product by id
- [ ] Update a product
- [ ] Delete a product
- [ ] Get a product by Company

# Database Schema

The database schema for Company is as follows:

| Field | Type | Description |
| --- | --- | --- |
| id | int | The unique identifier for the product |
| name | string | The name of the product |
| logo | string | The logo of the company |
| website | string | The website of the company |

The database schema for Product is as follows:

| Field | Type | Description |
| --- | --- | --- |
| id | int | The unique identifier for the product |
| name | string | The name of the product |
| color | string | The color of the product |
| RAM | int | The RAM of the product |
| memory | int | The memory of the product |
| price | int | The price of the product |
| image | string | The image of the product |
| company_id | int | The company id of the product |
| created_at | datetime | The date and time when the product was created |
| updated_at | datetime | The date and time when the product was updated |


