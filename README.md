## Apache log parser
An application that is an aggregator of data from apache access logs
with saving in the database. File parsing is done by cron.

The application has the following functions:
- write to database
- viewing data stored in the database (grouping by IP, by date, selection by date interval)
- API for receiving data in the form of JSON (the meaning is the same: obtaining data by time interval, the ability
group/filter by IP)
- configuration through the settings file (where the logs, file mask, and everything you need to configure the application are)
DBMS: postgresql

# run
1. launch
```sh
$ docker-compose -f docker-compose.dev.yml up --build
```


# Explanations
one.




## Enter to container
```sh
$ docker exec -it <id container or name> bash
$ docker exec -it <id container or name> poetry run <command>
```