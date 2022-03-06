### Project setup
1. Install [Docker](https://docs.docker.com/get-docker/) and docker-compose
2. Rename .env.example to .env and fill values
3. Run command `docker-compose build && docker-compose up -d`
4. Apply migrations: `docker-compose exec app python manage.py migrate`
    1. **(Optional):** Create superuser
5. Enter address `localhost:8000/docs/swagger` in your browser to test API
6. New user (not superuser) will be without permissions. Get token from `/auth/` route, click to Authorize in swagger UI. Enter `Token <your_token>` and use API 


### Notes

I decided to remove Car brand from UserCar model because we can get it from Car model.

And I decided to leave authorization by username (by default). Whether to make this decision or not depends on you