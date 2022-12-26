from contextlib import contextmanager
from typing import List, Tuple, Union
from psycopg2 import sql
import DBConnector as Connector


@contextmanager
def db_connection():
    conn = None
    try:
        conn = Connector.DBConnector()
        yield conn
    finally:
        conn and conn.close()


def create_tables():
    create_tables_query = """
    CREATE TABLE cones (
        cone_id INTEGER PRIMARY KEY CHECK ( cone_id > 0 ),
        right_value DECIMAL NOT NULL ,
        forward_value DECIMAL NOT NULL ,
        up_value DECIMAL NOT NULL ,
        type INTEGER NOT NULL CHECK ( type >= 0 AND type <= 4 ),
        confidence DECIMAL NOT NULL
    );
    CREATE TABLE bounding_box (
        cone_id INTEGER CHECK (cone_id > 0),
        cone_type INTEGER NOT NULL CHECK ( cone_type >= 0 AND cone_type <= 4 ),
        height DECIMAL NOT NULL CHECK ( height > 0 ),
        width DECIMAL NOT NULL CHECK ( width > 0 ),
        length DECIMAL NOT NULL CHECK ( length > 0 ),
        frame_position_u INTEGER NOT NULL CHECK ( frame_position_u > 0 ),
        frame_position_v INTEGER NOT NULL CHECK ( frame_position_v > 0 ),
        frame_position_depth INTEGER NOT NULL CHECK ( frame_position_depth > 0 ),
        vector_x DECIMAL NOT NULL,
        vector_y DECIMAL NOT NULL,
        vector_z DECIMAL NOT NULL,
        FOREIGN KEY (cone_id) REFERENCES cones ON DELETE CASCADE
    );
    CREATE TABLE cone_state (
        cone_state_number INTEGER PRIMARY KEY,
        cone_id INTEGER CHECK (cone_id > 0),
        r DECIMAL NOT NULL,
        alpha DECIMAL NOT NULL,
        vector_x DECIMAL NOT NULL,
        vector_y DECIMAL NOT NULL,
        cone_type INTEGER NOT NULL CHECK ( cone_type >= 0 AND cone_type <= 4 ),
        position_deviation DECIMAL NOT NULL,
        cluster_info_age INTEGER NOT NULL CHECK ( cluster_info_age > 0 ),
        cluster_info_num_of_cones INTEGER NOT NULL CHECK ( cluster_info_num_of_cones > 0 ),
        cluster_info_extra DECIMAL NOT NULL,
        FOREIGN KEY (cone_id) REFERENCES cones ON DELETE CASCADE
    );
    CREATE TABLE car_state (
        car_state_number INTEGER PRIMARY KEY,
        position_x DECIMAL NOT NULL,
        position_y DECIMAL NOT NULL,
        position_deviation_x DECIMAL NOT NULL,
        position_deviation_y DECIMAL NOT NULL,
        velocity_x DECIMAL NOT NULL,
        velocity_y DECIMAL NOT NULL,
        velocity_deviation_x DECIMAL NOT NULL,
        velocity_deviation_y DECIMAL NOT NULL,
        theta DECIMAL NOT NULL,
        theta_deviation DECIMAL NOT NULL,
        theta_dot DECIMAL NOT NULL,
        theta_dot_deviation DECIMAL NOT NULL,
        steering_angle DECIMAL NOT NULL,
        steering_angle_deviation DECIMAL NOT NULL,
        acceleration DECIMAL NOT NULL,
        acceleration_deviation DECIMAL NOT NULL
    );
    CREATE TABLE formula_state_from_right (
        right_cones INTEGER NOT NULL,
        current_car_state INTEGER REFERENCES car_state(car_state_number) ON DELETE CASCADE ,
        distance_to_finish DECIMAL NOT NULL,
        message_type TEXT NOT NULL CHECK ( message_type IN ('only_prediction', 'prediction_and_correction', 'still_calibrating', 'finished_lap') ),
        distance_from_left DECIMAL NOT NULL,
        distance_from_right DECIMAL NOT NULL,
        road_angle DECIMAL NOT NULL,
        FOREIGN KEY (right_cones) REFERENCES cone_state(cone_state_number) ON DELETE CASCADE
    );
    CREATE TABLE formula_state_from_left (
        left_cones INTEGER NOT NULL,
        current_car_state INTEGER REFERENCES car_state(car_state_number) ON DELETE CASCADE ,
        distance_to_finish DECIMAL NOT NULL,
        message_type TEXT NOT NULL CHECK ( message_type IN ('only_prediction', 'prediction_and_correction', 'still_calibrating', 'finished_lap') ),
        distance_from_left DECIMAL NOT NULL,
        distance_from_right DECIMAL NOT NULL,
        road_angle DECIMAL NOT NULL,
        FOREIGN KEY (left_cones) REFERENCES cone_state(cone_state_number) ON DELETE CASCADE
    );
    CREATE TABLE drive_instructions (
        gas DECIMAL NOT NULL CHECK ( gas BETWEEN 0.0 AND 1.0),
        brakes DECIMAL NOT NULL CHECK ( brakes BETWEEN 0.0 AND 1.0),
        steering DECIMAL NOT NULL CHECK ( steering BETWEEN -1.0 AND 1.0),
        optimal_speed DECIMAL NOT NULL CHECK ( optimal_speed BETWEEN 0.0 AND 80.0)
    );
    """

    with db_connection() as conn:
        conn.execute(create_tables_query)


def clear_tables():
    clear_tables_query = """
    DELETE FROM cones;
    DELETE FROM bounding_box;
    DELETE FROM cone_state;
    DELETE FROM car_state;
    DELETE FROM formula_state_from_right;
    DELETE FROM formula_state_from_left;
    DELETE FROM drive_instructions;
    """

    with db_connection() as conn:
        conn.execute(clear_tables_query)


def delete_tables():
    delete_tables_query = """
    DROP TABLE formula_state_from_right;
    DROP TABLE formula_state_from_left;
    DROP TABLE drive_instructions;
    DROP TABLE car_state;
    DROP TABLE cone_state;
    DROP TABLE bounding_box;
    DROP TABLE cones;
    """

    with db_connection() as conn:
        conn.execute(delete_tables_query)


def main():
    create_tables()
    delete_tables()


if __name__ == "__main__":
    main()

