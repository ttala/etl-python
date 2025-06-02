# Simple ETL Application

This is a lightweight ETL (Extract, Transform, Load) Python application that uses PostgreSQL as its backend database. The project is containerized using Docker and orchestrated using Docker Compose.

### Prerequisites

Make sure you have the following installed on your system:

- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)

### Environment Configuration

Create a `.env` file in the root directory with the following variables:

```env
POSTGRES_DB=your_db_name
POSTGRES_USER=your_username
POSTGRES_PASSWORD=your_password

### Deployment

# Build the application image
docker build -t simple-etl .

# Start services
docker-compose up
