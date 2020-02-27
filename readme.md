# ETL service

## Application setup

Requirements:

- docker: 1.13.0+
- docker-compose: 1.10.0+

Run the application

```shell script
docker-compose up -d --build
```

## Development setup

Build images

```shell script
docker-compose -f dev-docker-compose.yml up -d --build
```

Generate test data

- Import data from CSV

```shell script
docker exec -it etl bash -c 'python _import_from_csv.py'
```

- Create sample PostgreSQL table

```shell script
docker exec -it etl bash -c 'python _create_sample_table.py' 
```

## Configuration

All application configuration can be handled from `app/config/config.py`

## Logging

All application logging is written in `logs` directory:

- `workers.json` stores workers execution logs
- `error.log` flask application error file

## Worker execution

Worker is executed at every application launch.

Crontab record for `orders workes` is set on every 5 minutes.

### Run cron job manually

- Get cronjob id

```shell script
flask crontab show
```

- Run cronjob

```shell script
flask crontab run <id>
```