import argparse

import psycopg2

CONN_STR = "postgres://postgres:password@localhost:5432/postgres"

def create_tables():
    create_tables_query = """
    CREATE TABLE experiments (
        exp_id TEXT PRIMARY KEY,
        createdAt TIMESTAMP NOT NULL,
        finishedAt TIMESTAMP
    );
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
        time_stamp TIMESTAMP NOT NULL,
        FOREIGN KEY (cone_id) REFERENCES cones ON DELETE CASCADE
    );
    CREATE TABLE car_state (
        exp_id TEXT NOT NULL REFERENCES experiments ON DELETE CASCADE,
        car_state_number INTEGER NOT NULL,
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
        acceleration_deviation DECIMAL NOT NULL,
        time_stamp TIMESTAMP NOT NULL,
        PRIMARY KEY (car_state_number, time_stamp)
    );
    CREATE TABLE formula_state_from_right (
        right_cones INTEGER NOT NULL,
        current_car_state INTEGER NOT NULL,
        car_time TIMESTAMP NOT NULL,
        distance_to_finish DECIMAL NOT NULL,
        message_type TEXT NOT NULL CHECK ( message_type IN ('only_prediction', 'prediction_and_correction', 'still_calibrating', 'finished_lap') ),
        distance_from_left DECIMAL NOT NULL,
        distance_from_right DECIMAL NOT NULL,
        road_angle DECIMAL NOT NULL,
        time_stamp TIMESTAMP NOT NULL,
        FOREIGN KEY (current_car_state, car_time) REFERENCES car_state(car_state_number, time_stamp) ON DELETE CASCADE,
        FOREIGN KEY (right_cones) REFERENCES cone_state(cone_state_number) ON DELETE CASCADE
    );
    CREATE TABLE formula_state_from_left (
        left_cones INTEGER NOT NULL,
        current_car_state INTEGER NOT NULL,
        car_time TIMESTAMP NOT NULL,
        distance_to_finish DECIMAL NOT NULL,
        message_type TEXT NOT NULL CHECK ( message_type IN ('only_prediction', 'prediction_and_correction', 'still_calibrating', 'finished_lap') ),
        distance_from_left DECIMAL NOT NULL,
        distance_from_right DECIMAL NOT NULL,
        road_angle DECIMAL NOT NULL,
        time_stamp TIMESTAMP NOT NULL,
        FOREIGN KEY (current_car_state, car_time) REFERENCES car_state(car_state_number, time_stamp) ON DELETE CASCADE,
        FOREIGN KEY (left_cones) REFERENCES cone_state(cone_state_number) ON DELETE CASCADE
    );
    CREATE TABLE drive_instructions (
        exp_id TEXT NOT NULL REFERENCES experiments ON DELETE CASCADE,
        gas DECIMAL NOT NULL CHECK ( gas BETWEEN 0.0 AND 1.0),
        brakes DECIMAL NOT NULL CHECK ( brakes BETWEEN 0.0 AND 1.0),
        steering DECIMAL NOT NULL CHECK ( steering BETWEEN -1.0 AND 1.0),
        optimal_speed DECIMAL NOT NULL CHECK ( optimal_speed BETWEEN 0.0 AND 80.0),
        time_stamp TIMESTAMP NOT NULL
    );
    SELECT create_hypertable('car_state','time_stamp');
    CREATE INDEX ix_car_state_num_time ON car_state (car_state_number, time_stamp);
    SELECT create_hypertable('drive_instructions', 'time_stamp');
    CREATE INDEX ix_drive_instructions_gas_over_time ON drive_instructions (gas, time_stamp);
    CREATE INDEX ix_drive_instructions_brakes_over_time ON drive_instructions (brakes, time_stamp);
    CREATE INDEX ix_drive_instructions_steering_over_time ON drive_instructions (steering, time_stamp);
    CREATE INDEX ix_drive_instructions_speed_over_time ON drive_instructions (optimal_speed, time_stamp);
    """

    try:
        conn = psycopg2.connect(CONN_STR)
        cursor = conn.cursor()
        cursor.execute(create_tables_query)
        conn.commit()
        cursor.close()
    except (Exception) as e:
        print(e)



def clear_tables():
    clear_tables_query = """
    DELETE FROM experiments;
    DELETE FROM cones;
    DELETE FROM bounding_box;
    DELETE FROM cone_state;
    DELETE FROM car_state;
    DELETE FROM formula_state_from_right;
    DELETE FROM formula_state_from_left;
    DELETE FROM drive_instructions;
    """

    try:
        conn = psycopg2.connect(CONN_STR)
        cursor = conn.cursor()
        cursor.execute(clear_tables_query)
        conn.commit()
        cursor.close()
    except (Exception) as e:
        print(e)


def delete_tables():
    delete_tables_query = """
    DROP TABLE formula_state_from_right;
    DROP TABLE formula_state_from_left;
    DROP TABLE drive_instructions;
    DROP TABLE car_state;
    DROP TABLE cone_state;
    DROP TABLE bounding_box;
    DROP TABLE cones;
    DROP TABLE experiments;
    """

    try:
        conn = psycopg2.connect(CONN_STR)
        cursor = conn.cursor()
        cursor.execute(delete_tables_query)
        conn.commit()
        cursor.close()
    except (Exception) as e:
        print(e)

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--clear', action='store_true', help="clear tables")
    parser.add_argument('-d', '--delete', action='store_true', help="drop tables")
    parser.add_argument('-i', '--init', action='store_true', help="init tables")
    parser.set_defaults(clear=False, delete=False, init=False)
    return parser.parse_args()


def main():
    args = parse_args()

    if args.clear:
        clear_tables()
    elif args.delete:
        delete_tables()
    elif args.init:
        create_tables()


if __name__ == "__main__":
    main()

