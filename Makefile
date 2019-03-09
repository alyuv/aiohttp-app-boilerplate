up:  ## start service
	@printf "=========Start service=========\n\n"
	@docker-compose up

stop:  ## stop service
	@printf "=========Stop service=========\n\n"
	@docker-compose stop

.PHONY: stop
rm:  ## remove service
	@printf "=========Remove service=========\n\n"
	@docker-compose rm -f

reset:  ## stop and remove service
	@printf "=========Stop and remove service=========\n\n"
	@docker-compose down

build:  ## build service
	@printf "=========Build service=========\n\n"
	docker-compose build

build-no-cache:  ## build service without cache
	@printf "=========Build service without cache =========\n\n"
	docker-compose build --no-cache

restart: ## restart service
	@printf "=========Restart service=========\n\n"
	docker-compose stop
	docker-compose down --rmi local
	docker-compose build
	docker-compose up -d

restart-v:  ## remove local images, volumes(postgres/redis) and restart service
	@printf "=========Remove local images ... and resart service=========\n\n"
	docker-compose stop
	docker-compose down --rmi local -v
	docker-compose build
	docker-compose up -d

clean clear:  ## clean all useless data
	@printf "=========Clean all useless data=========\n\n"
	rm -rf `find . -name __pycache__`
	rm -f `find . -type f -name '*.py[co]' `
	rm -f `find . -type f -name '*~' `
	rm -f `find . -type f -name '.*~' `
	rm -f `find . -type f -name '@*' `
	rm -f `find . -type f -name '#*#' `
	rm -f `find . -type f -name '*.orig' `
	rm -f `find . -type f -name '*.rej' `
	rm -f .coverage
	rm -rf htmlcov
	rm -rf docs/_build/
	rm -rf coverage.xml
	rm -rf dist

attach:  ## attach to aiohtpp-app-boilerplate service for debug
	docker attach aiohtpp-app-boilerplate

help:  ## show available commands
	@grep -E '^[a-zA-Z-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'
