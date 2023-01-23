import os
import time

import psycopg2
from DBAdapter import DBAdapter as Adapter
from overrides import override


class timescaleDBAdapter(Adapter):
    def __init__(self):
        # super.__init__()
        # self.connection_string = "postgres://postgres:password@localhost:5432/formulaDB"
        self.connection_string = f"postgres://postgres:password@database:5432/postgres"
        self.conn = self._connect()
        self.cursor = self.conn.cursor()
        self.car_state_num = 0

    def _connect(self):
        timeout = 0.1
        while True:
            try:
                conn = psycopg2.connect(self.connection_string)
                break
            except psycopg2.OperationalError:
                print(f"Could not connect to database, trying in {timeout} seconds")
                time.sleep(timeout)
                timeout *= 2
                if timeout > 30:
                    raise
        return conn

    @override
    def insert_new_experiment(self, params):
        insert_new_experiment_query = """
            INSERT INTO experiments VALUES ({exp_id}, TO_TIMESTAMP('{created_at}', 'YYYY-MM-DD HH24:MI:SS.US'), NULL)
        """.format(
            exp_id=params["exp_id"],
            created_at=params["created_at"]
        )

        try:
            self.cursor.execute(insert_new_experiment_query)
            self.car_state_num += 1
        except Exception as e:
            print(e)

        self.conn.commit()

    @override
    def finish_experiment(self, params):
        finish_experiment_query = """
                UPDATE experiments 
                SET 
                    finishedAt=TO_TIMESTAMP('{finished_at}', 'YYYY-MM-DD HH24:MI:SS.US')
                WHERE exp_id = '{exp_id}'
            """.format(
            exp_id=params["exp_id"],
            finished_at=params["finished_at"]
        )

        try:
            self.cursor.execute(finish_experiment_query)
            self.car_state_num += 1
        except Exception as e:
            print(e)

        self.conn.commit()

    @override
    def insert_into_car_state(self, params):
        """
        function inserts values into the car_state table
        :param params: a dictionary of values. Should contain:
            position vector (x,y),
            position deviation vector (x,y),
            velocity vector (x,y),
            velocity deviation vector (x,y),
            theta,
            theta deviation,
            theta dot,
            theta dot deviation,
            steering angle,
            steering angle deviation,
            acceleration,
            acceleration deviation,
            time_stamp
        :return:
        """
        insert_into_car_state_query = """
        INSERT INTO car_state VALUES ({exp_id}, {state_num}, {position_x}, {position_y}, {position_deviation_x}, {position_deviation_y},
        {velocity_x}, {velocity_y}, {velocity_deviation_x}, {velocity_deviation_y}, {theta}, {theta_deviation}, {theta_dot}, 
        {theta_dot_deviation}, {steering_angle}, {steering_angle_deviation}, {acceleration}, {acceleration_deviation}, TO_TIMESTAMP('{time_stamp}', 'YYYY-MM-DD HH24:MI:SS.US'))
        """.format(
            exp_id=params["exp_id"],
            state_num=self.car_state_num,
            position_x=params["position_vector"][0],
            position_y=params["position_vector"][1],
            position_deviation_x=params["position_deviation_vector"][0],
            position_deviation_y=params["position_deviation_vector"][1],
            velocity_x=params["velocity_vector"][0],
            velocity_y=params["velocity_vector"][1],
            velocity_deviation_x=params["velocity_deviation_vector"][0],
            velocity_deviation_y=params["velocity_deviation_vector"][1],
            theta=params["theta"],
            theta_deviation=params["theta_deviation"],
            theta_dot=params["theta_dot"],
            theta_dot_deviation=params["theta_dot_deviation"],
            steering_angle=params["steering_angle"],
            steering_angle_deviation=params["steering_angle_deviation"],
            acceleration=params["acceleration"],
            acceleration_deviation=params["acceleration_deviation"],
            time_stamp=params["time_stamp"]
        )

        try:
            self.cursor.execute(insert_into_car_state_query)
            self.car_state_num += 1
        except Exception as e:
            print(e)

        self.conn.commit()  # TODO: Do we need it now?

    @override
    def insert_into_drive_instructions(self, params):
        """
        function inserts values into drive_instructions table
        :param params: a dictionary of values. Should contain:
        exp_num,
        gas,
        brakes,
        steering,
        optimal_speed,
        time_stamp
        :return:
        """
        insert_into_drive_instructions_query = """
        INSERT INTO drive_instructions VALUES ('{exp_id}', {gas}, {brakes}, {steering}, {optimal_speed}, TO_TIMESTAMP('{time_stamp}', 'YYYY-MM-DD HH24:MI:SS.US'))
        """.format(
            exp_id=params["exp_id"],
            gas=params["gas"],
            brakes=params["brakes"],
            steering=params["steering"],
            optimal_speed=params["optimal_speed"],
            time_stamp=params["time_stamp"]
        )

        try:
            self.cursor.execute(insert_into_drive_instructions_query)
        except Exception as e:
            print(e)

        self.conn.commit()  # TODO: Do we need it now?
