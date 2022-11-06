.PHONY: get-leagues-raw-data
get-leagues-raw-data:
	poetry run python consumer/football.py get-data --endpoint=all_leagues

.PHONY: get-teams-raw-data
get-teams-raw-data:
	poetry run python consumer/football.py get-data --endpoint=all_teams

.PHONY: get-venues-raw-data
get-venues-raw-data:
	poetry run python consumer/football.py get-data --endpoint=all_venues

.PHONY: test-consumer
test-consumer:
	poetry run python consumer/test.py --endpoint=${ENDPOINT}