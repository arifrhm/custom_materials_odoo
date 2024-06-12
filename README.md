# Custom Materials Odoo Module

## Introduction
`custom_materials_odoo` is an Odoo module designed to manage custom materials within your Odoo environment. This module allows users to create, update, list, and delete materials with specific attributes such as code, name, type, buy price, and supplier information.

## Features
- Create new materials with specific attributes.
- Update existing materials.
- List all available materials.
- Delete materials from the database.
- Secure endpoints with CSRF protection.

## Prerequisites
- Docker
- Docker Compose

## Installation
To install and run this module using Docker, follow these steps:

1. Clone the repository:
    ```sh
    git clone https://github.com/arifrhm/custom_materials_odoo.git
    cd custom_materials_odoo
    ```

2. Build and run the Docker containers:
    ```sh
    docker-compose up --build -d
    ```

3. Access Odoo by navigating to `http://localhost:8069` in your web browser.

## Usage
Once the containers are up and running, you can start using the module to manage your custom materials.

### Creating a Material
To create a new material, navigate to the Custom Materials menu in Odoo and click on the "Create" button. Fill in the necessary details and save.

### Updating a Material
To update a material, open the material record you want to update, make the necessary changes, and save.

### Listing Materials
To view all materials, navigate to the Custom Materials menu in Odoo. You will see a list of all materials with their details.

### Deleting a Material
To delete a material, open the material record you want to delete and click on the "Delete" button.

## Running Tests
To run tests for the `custom_materials_odoo` module, use the following command:
```sh
docker-compose exec odoo odoo --test-enable --stop-after-init -d custom_materials
```

## Viewing Logs
To view the logs of the Odoo container, use the following command:
```sh
docker-compose logs -f odoo
```