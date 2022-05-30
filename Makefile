help:
#	@echo "Base commands"
#	@echo "\tmake deploy\t-> \trunning project"
#	@echo "\tmake develop\t-> \trunning project (all services in docker-compose) in development env"
#	@echo "\tmake lint\t-> \trunning project (all services in docker-compose) in develop env"
	@echo "\tmake test\t-> \trunning project (all services in docker-compose) in develop env"

#develop:
#	docker-compose up --build
#
#lint:
#	sh scripts/lint.sh
#
test:
	poetry run python -m unittest discover -s app

init_db:
	poetry run python init_db.py
