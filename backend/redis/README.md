To start Redis locally using Docker, follow these steps:

1. Make sure Docker is installed on your machine.

2. Start Redis using Docker Compose using the following command in this directory:

   ```bash
   docker-compose up -d
   ```

Redis will be available at `localhost:6379`.

### Stopping Redis

To stop the Redis container:

```bash
docker-compose down


### Data

The data persist in ./data folder in this directory