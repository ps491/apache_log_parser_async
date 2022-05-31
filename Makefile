help:
#	@echo "Base commands"
#	@echo "\tmake deploy\t-> \trunning project"
#	@echo "\tmake develop\t-> \trunning project (all services in docker-compose) in development env"
#	@echo "\tmake lint\t-> \trunning project (all services in docker-compose) in develop env"
	@echo "\tmake run_local\t-> \trunning project in local env"
	@echo "\tmake init_db\t-> \tcreate tables, insert test data"
	@echo "\tmake test\t-> \trunning project (all services in docker-compose) in develop env"

#develop:
#	docker-compose up --build
#
#lint:
#	sh scripts/lint.sh
#
test:
	poetry run python -m unittest discover -s app

run_local:
	poetry run python app/main.py

#init_db:
#	 poetry run python init_db.py


#init_db:
#	poetry run python init_db_2.py

init_db:
	poetry run python app/init_db_3.py
