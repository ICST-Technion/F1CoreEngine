import random
from datetime import datetime
from time import sleep

import psycopg2

CONNECTION = "postgres://postgres:password@localhost:5432/postgres"


def send_velocity(velocity: int, experiment: str):
    with psycopg2.connect(CONNECTION) as conn:
        cursor = conn.cursor()
        date = datetime.utcnow()
        query = "INSERT INTO velocity VALUES (TO_TIMESTAMP('{}', 'YYYY-MM-DD HH24:MI:SS.US'), {}, '{}')"
        cursor.execute(query.format(date, velocity, experiment))


def generator_handler():
    for vel in range(1, 200):
        rand = random.randint(-20, 20)
        send_velocity(vel + rand, "exp3")
        sleep(1)


if __name__ == '__main__':
    generator_handler()
