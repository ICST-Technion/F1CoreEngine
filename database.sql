--
-- PostgreSQL database dump
--

-- Dumped from database version 14.6 (Ubuntu 14.6-1.pgdg22.04+1)
-- Dumped by pg_dump version 14.6 (Ubuntu 14.6-1.pgdg22.04+1)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: timescaledb; Type: EXTENSION; Schema: -; Owner: -
--

CREATE EXTENSION IF NOT EXISTS timescaledb WITH SCHEMA public;


--
-- Name: EXTENSION timescaledb; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION timescaledb IS 'Enables scalable inserts and complex queries for time-series data';


--
-- Name: timescaledb_toolkit; Type: EXTENSION; Schema: -; Owner: -
--

CREATE EXTENSION IF NOT EXISTS timescaledb_toolkit WITH SCHEMA public;


--
-- Name: EXTENSION timescaledb_toolkit; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION timescaledb_toolkit IS 'Library of analytical hyperfunctions, time-series pipelining, and other SQL utilities';


SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: bounding_box; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.bounding_box (
    cone_id integer,
    cone_type integer NOT NULL,
    height numeric NOT NULL,
    width numeric NOT NULL,
    length numeric NOT NULL,
    frame_position_u integer NOT NULL,
    frame_position_v integer NOT NULL,
    frame_position_depth integer NOT NULL,
    vector_x numeric NOT NULL,
    vector_y numeric NOT NULL,
    vector_z numeric NOT NULL,
    CONSTRAINT bounding_box_cone_id_check CHECK ((cone_id > 0)),
    CONSTRAINT bounding_box_cone_type_check CHECK (((cone_type >= 0) AND (cone_type <= 4))),
    CONSTRAINT bounding_box_frame_position_depth_check CHECK ((frame_position_depth > 0)),
    CONSTRAINT bounding_box_frame_position_u_check CHECK ((frame_position_u > 0)),
    CONSTRAINT bounding_box_frame_position_v_check CHECK ((frame_position_v > 0)),
    CONSTRAINT bounding_box_height_check CHECK ((height > (0)::numeric)),
    CONSTRAINT bounding_box_length_check CHECK ((length > (0)::numeric)),
    CONSTRAINT bounding_box_width_check CHECK ((width > (0)::numeric))
);


ALTER TABLE public.bounding_box OWNER TO postgres;

--
-- Name: car_state; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.car_state (
    car_state_number integer NOT NULL,
    position_x numeric NOT NULL,
    position_y numeric NOT NULL,
    position_deviation_x numeric NOT NULL,
    position_deviation_y numeric NOT NULL,
    velocity_x numeric NOT NULL,
    velocity_y numeric NOT NULL,
    velocity_deviation_x numeric NOT NULL,
    velocity_deviation_y numeric NOT NULL,
    theta numeric NOT NULL,
    theta_deviation numeric NOT NULL,
    theta_dot numeric NOT NULL,
    theta_dot_deviation numeric NOT NULL,
    steering_angle numeric NOT NULL,
    steering_angle_deviation numeric NOT NULL,
    acceleration numeric NOT NULL,
    acceleration_deviation numeric NOT NULL,
    time_stamp timestamp without time zone NOT NULL
);


ALTER TABLE public.car_state OWNER TO postgres;

--
-- Name: cone_state; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.cone_state (
    cone_state_number integer NOT NULL,
    cone_id integer,
    r numeric NOT NULL,
    alpha numeric NOT NULL,
    vector_x numeric NOT NULL,
    vector_y numeric NOT NULL,
    cone_type integer NOT NULL,
    position_deviation numeric NOT NULL,
    cluster_info_age integer NOT NULL,
    cluster_info_num_of_cones integer NOT NULL,
    cluster_info_extra numeric NOT NULL,
    time_stamp timestamp without time zone NOT NULL,
    CONSTRAINT cone_state_cluster_info_age_check CHECK ((cluster_info_age > 0)),
    CONSTRAINT cone_state_cluster_info_num_of_cones_check CHECK ((cluster_info_num_of_cones > 0)),
    CONSTRAINT cone_state_cone_id_check CHECK ((cone_id > 0)),
    CONSTRAINT cone_state_cone_type_check CHECK (((cone_type >= 0) AND (cone_type <= 4)))
);


ALTER TABLE public.cone_state OWNER TO postgres;

--
-- Name: cones; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.cones (
    cone_id integer NOT NULL,
    right_value numeric NOT NULL,
    forward_value numeric NOT NULL,
    up_value numeric NOT NULL,
    type integer NOT NULL,
    confidence numeric NOT NULL,
    CONSTRAINT cones_cone_id_check CHECK ((cone_id > 0)),
    CONSTRAINT cones_type_check CHECK (((type >= 0) AND (type <= 4)))
);


ALTER TABLE public.cones OWNER TO postgres;

--
-- Name: drive_instructions; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.drive_instructions (
    gas numeric NOT NULL,
    brakes numeric NOT NULL,
    steering numeric NOT NULL,
    optimal_speed numeric NOT NULL,
    CONSTRAINT drive_instructions_brakes_check CHECK (((brakes >= 0.0) AND (brakes <= 1.0))),
    CONSTRAINT drive_instructions_gas_check CHECK (((gas >= 0.0) AND (gas <= 1.0))),
    CONSTRAINT drive_instructions_optimal_speed_check CHECK (((optimal_speed >= 0.0) AND (optimal_speed <= 80.0))),
    CONSTRAINT drive_instructions_steering_check CHECK (((steering >= '-1.0'::numeric) AND (steering <= 1.0)))
);


ALTER TABLE public.drive_instructions OWNER TO postgres;

--
-- Name: formula_state_from_left; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.formula_state_from_left (
    left_cones integer NOT NULL,
    current_car_state integer NOT NULL,
    car_time timestamp without time zone NOT NULL,
    distance_to_finish numeric NOT NULL,
    message_type text NOT NULL,
    distance_from_left numeric NOT NULL,
    distance_from_right numeric NOT NULL,
    road_angle numeric NOT NULL,
    time_stamp timestamp without time zone NOT NULL,
    CONSTRAINT formula_state_from_left_message_type_check CHECK ((message_type = ANY (ARRAY['only_prediction'::text, 'prediction_and_correction'::text, 'still_calibrating'::text, 'finished_lap'::text])))
);


ALTER TABLE public.formula_state_from_left OWNER TO postgres;

--
-- Name: formula_state_from_right; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.formula_state_from_right (
    right_cones integer NOT NULL,
    current_car_state integer NOT NULL,
    car_time timestamp without time zone NOT NULL,
    distance_to_finish numeric NOT NULL,
    message_type text NOT NULL,
    distance_from_left numeric NOT NULL,
    distance_from_right numeric NOT NULL,
    road_angle numeric NOT NULL,
    time_stamp timestamp without time zone NOT NULL,
    CONSTRAINT formula_state_from_right_message_type_check CHECK ((message_type = ANY (ARRAY['only_prediction'::text, 'prediction_and_correction'::text, 'still_calibrating'::text, 'finished_lap'::text])))
);


ALTER TABLE public.formula_state_from_right OWNER TO postgres;

--
-- Data for Name: cache_inval_bgw_job; Type: TABLE DATA; Schema: _timescaledb_cache; Owner: postgres
--

COPY _timescaledb_cache.cache_inval_bgw_job  FROM stdin;
\.


--
-- Data for Name: cache_inval_extension; Type: TABLE DATA; Schema: _timescaledb_cache; Owner: postgres
--

COPY _timescaledb_cache.cache_inval_extension  FROM stdin;
\.


--
-- Data for Name: cache_inval_hypertable; Type: TABLE DATA; Schema: _timescaledb_cache; Owner: postgres
--

COPY _timescaledb_cache.cache_inval_hypertable  FROM stdin;
\.


--
-- Data for Name: hypertable; Type: TABLE DATA; Schema: _timescaledb_catalog; Owner: postgres
--

COPY _timescaledb_catalog.hypertable (id, schema_name, table_name, associated_schema_name, associated_table_prefix, num_dimensions, chunk_sizing_func_schema, chunk_sizing_func_name, chunk_target_size, compression_state, compressed_hypertable_id, replication_factor) FROM stdin;
7	public	car_state	_timescaledb_internal	_hyper_7	1	_timescaledb_internal	calculate_chunk_interval	0	0	\N	\N
\.


--
-- Data for Name: chunk; Type: TABLE DATA; Schema: _timescaledb_catalog; Owner: postgres
--

COPY _timescaledb_catalog.chunk (id, hypertable_id, schema_name, table_name, compressed_chunk_id, dropped, status, osm_chunk) FROM stdin;
\.


--
-- Data for Name: dimension; Type: TABLE DATA; Schema: _timescaledb_catalog; Owner: postgres
--

COPY _timescaledb_catalog.dimension (id, hypertable_id, column_name, column_type, aligned, num_slices, partitioning_func_schema, partitioning_func, interval_length, integer_now_func_schema, integer_now_func) FROM stdin;
7	7	time_stamp	timestamp without time zone	t	\N	\N	\N	604800000000	\N	\N
\.


--
-- Data for Name: dimension_slice; Type: TABLE DATA; Schema: _timescaledb_catalog; Owner: postgres
--

COPY _timescaledb_catalog.dimension_slice (id, dimension_id, range_start, range_end) FROM stdin;
\.


--
-- Data for Name: chunk_constraint; Type: TABLE DATA; Schema: _timescaledb_catalog; Owner: postgres
--

COPY _timescaledb_catalog.chunk_constraint (chunk_id, dimension_slice_id, constraint_name, hypertable_constraint_name) FROM stdin;
\.


--
-- Data for Name: chunk_data_node; Type: TABLE DATA; Schema: _timescaledb_catalog; Owner: postgres
--

COPY _timescaledb_catalog.chunk_data_node (chunk_id, node_chunk_id, node_name) FROM stdin;
\.


--
-- Data for Name: chunk_index; Type: TABLE DATA; Schema: _timescaledb_catalog; Owner: postgres
--

COPY _timescaledb_catalog.chunk_index (chunk_id, index_name, hypertable_id, hypertable_index_name) FROM stdin;
\.


--
-- Data for Name: compression_chunk_size; Type: TABLE DATA; Schema: _timescaledb_catalog; Owner: postgres
--

COPY _timescaledb_catalog.compression_chunk_size (chunk_id, compressed_chunk_id, uncompressed_heap_size, uncompressed_toast_size, uncompressed_index_size, compressed_heap_size, compressed_toast_size, compressed_index_size, numrows_pre_compression, numrows_post_compression) FROM stdin;
\.


--
-- Data for Name: continuous_agg; Type: TABLE DATA; Schema: _timescaledb_catalog; Owner: postgres
--

COPY _timescaledb_catalog.continuous_agg (mat_hypertable_id, raw_hypertable_id, user_view_schema, user_view_name, partial_view_schema, partial_view_name, bucket_width, direct_view_schema, direct_view_name, materialized_only, finalized) FROM stdin;
\.


--
-- Data for Name: continuous_agg_migrate_plan; Type: TABLE DATA; Schema: _timescaledb_catalog; Owner: postgres
--

COPY _timescaledb_catalog.continuous_agg_migrate_plan (mat_hypertable_id, start_ts, end_ts) FROM stdin;
\.


--
-- Data for Name: continuous_agg_migrate_plan_step; Type: TABLE DATA; Schema: _timescaledb_catalog; Owner: postgres
--

COPY _timescaledb_catalog.continuous_agg_migrate_plan_step (mat_hypertable_id, step_id, status, start_ts, end_ts, type, config) FROM stdin;
\.


--
-- Data for Name: continuous_aggs_bucket_function; Type: TABLE DATA; Schema: _timescaledb_catalog; Owner: postgres
--

COPY _timescaledb_catalog.continuous_aggs_bucket_function (mat_hypertable_id, experimental, name, bucket_width, origin, timezone) FROM stdin;
\.


--
-- Data for Name: continuous_aggs_hypertable_invalidation_log; Type: TABLE DATA; Schema: _timescaledb_catalog; Owner: postgres
--

COPY _timescaledb_catalog.continuous_aggs_hypertable_invalidation_log (hypertable_id, lowest_modified_value, greatest_modified_value) FROM stdin;
\.


--
-- Data for Name: continuous_aggs_invalidation_threshold; Type: TABLE DATA; Schema: _timescaledb_catalog; Owner: postgres
--

COPY _timescaledb_catalog.continuous_aggs_invalidation_threshold (hypertable_id, watermark) FROM stdin;
\.


--
-- Data for Name: continuous_aggs_materialization_invalidation_log; Type: TABLE DATA; Schema: _timescaledb_catalog; Owner: postgres
--

COPY _timescaledb_catalog.continuous_aggs_materialization_invalidation_log (materialization_id, lowest_modified_value, greatest_modified_value) FROM stdin;
\.


--
-- Data for Name: dimension_partition; Type: TABLE DATA; Schema: _timescaledb_catalog; Owner: postgres
--

COPY _timescaledb_catalog.dimension_partition (dimension_id, range_start, data_nodes) FROM stdin;
\.


--
-- Data for Name: hypertable_compression; Type: TABLE DATA; Schema: _timescaledb_catalog; Owner: postgres
--

COPY _timescaledb_catalog.hypertable_compression (hypertable_id, attname, compression_algorithm_id, segmentby_column_index, orderby_column_index, orderby_asc, orderby_nullsfirst) FROM stdin;
\.


--
-- Data for Name: hypertable_data_node; Type: TABLE DATA; Schema: _timescaledb_catalog; Owner: postgres
--

COPY _timescaledb_catalog.hypertable_data_node (hypertable_id, node_hypertable_id, node_name, block_chunks) FROM stdin;
\.


--
-- Data for Name: metadata; Type: TABLE DATA; Schema: _timescaledb_catalog; Owner: postgres
--

COPY _timescaledb_catalog.metadata (key, value, include_in_telemetry) FROM stdin;
exported_uuid	d6bd2f53-2c20-48be-addf-13232ecb1f00	t
\.


--
-- Data for Name: remote_txn; Type: TABLE DATA; Schema: _timescaledb_catalog; Owner: postgres
--

COPY _timescaledb_catalog.remote_txn (data_node_name, remote_transaction_id) FROM stdin;
\.


--
-- Data for Name: tablespace; Type: TABLE DATA; Schema: _timescaledb_catalog; Owner: postgres
--

COPY _timescaledb_catalog.tablespace (id, hypertable_id, tablespace_name) FROM stdin;
\.


--
-- Data for Name: bgw_job; Type: TABLE DATA; Schema: _timescaledb_config; Owner: postgres
--

COPY _timescaledb_config.bgw_job (id, application_name, schedule_interval, max_runtime, max_retries, retry_period, proc_schema, proc_name, owner, scheduled, hypertable_id, config, check_schema, check_name) FROM stdin;
\.


--
-- Data for Name: bounding_box; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.bounding_box (cone_id, cone_type, height, width, length, frame_position_u, frame_position_v, frame_position_depth, vector_x, vector_y, vector_z) FROM stdin;
\.


--
-- Data for Name: car_state; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.car_state (car_state_number, position_x, position_y, position_deviation_x, position_deviation_y, velocity_x, velocity_y, velocity_deviation_x, velocity_deviation_y, theta, theta_deviation, theta_dot, theta_dot_deviation, steering_angle, steering_angle_deviation, acceleration, acceleration_deviation, time_stamp) FROM stdin;
\.


--
-- Data for Name: cone_state; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.cone_state (cone_state_number, cone_id, r, alpha, vector_x, vector_y, cone_type, position_deviation, cluster_info_age, cluster_info_num_of_cones, cluster_info_extra, time_stamp) FROM stdin;
\.


--
-- Data for Name: cones; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.cones (cone_id, right_value, forward_value, up_value, type, confidence) FROM stdin;
\.


--
-- Data for Name: drive_instructions; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.drive_instructions (gas, brakes, steering, optimal_speed) FROM stdin;
\.


--
-- Data for Name: formula_state_from_left; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.formula_state_from_left (left_cones, current_car_state, car_time, distance_to_finish, message_type, distance_from_left, distance_from_right, road_angle, time_stamp) FROM stdin;
\.


--
-- Data for Name: formula_state_from_right; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.formula_state_from_right (right_cones, current_car_state, car_time, distance_to_finish, message_type, distance_from_left, distance_from_right, road_angle, time_stamp) FROM stdin;
\.


--
-- Name: chunk_constraint_name; Type: SEQUENCE SET; Schema: _timescaledb_catalog; Owner: postgres
--

SELECT pg_catalog.setval('_timescaledb_catalog.chunk_constraint_name', 1, false);


--
-- Name: chunk_id_seq; Type: SEQUENCE SET; Schema: _timescaledb_catalog; Owner: postgres
--

SELECT pg_catalog.setval('_timescaledb_catalog.chunk_id_seq', 1, false);


--
-- Name: continuous_agg_migrate_plan_step_step_id_seq; Type: SEQUENCE SET; Schema: _timescaledb_catalog; Owner: postgres
--

SELECT pg_catalog.setval('_timescaledb_catalog.continuous_agg_migrate_plan_step_step_id_seq', 1, false);


--
-- Name: dimension_id_seq; Type: SEQUENCE SET; Schema: _timescaledb_catalog; Owner: postgres
--

SELECT pg_catalog.setval('_timescaledb_catalog.dimension_id_seq', 7, true);


--
-- Name: dimension_slice_id_seq; Type: SEQUENCE SET; Schema: _timescaledb_catalog; Owner: postgres
--

SELECT pg_catalog.setval('_timescaledb_catalog.dimension_slice_id_seq', 1, false);


--
-- Name: hypertable_id_seq; Type: SEQUENCE SET; Schema: _timescaledb_catalog; Owner: postgres
--

SELECT pg_catalog.setval('_timescaledb_catalog.hypertable_id_seq', 7, true);


--
-- Name: bgw_job_id_seq; Type: SEQUENCE SET; Schema: _timescaledb_config; Owner: postgres
--

SELECT pg_catalog.setval('_timescaledb_config.bgw_job_id_seq', 1000, false);


--
-- Name: car_state car_state_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.car_state
    ADD CONSTRAINT car_state_pkey PRIMARY KEY (car_state_number, time_stamp);


--
-- Name: cone_state cone_state_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.cone_state
    ADD CONSTRAINT cone_state_pkey PRIMARY KEY (cone_state_number);


--
-- Name: cones cones_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.cones
    ADD CONSTRAINT cones_pkey PRIMARY KEY (cone_id);


--
-- Name: car_state_time_stamp_idx; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX car_state_time_stamp_idx ON public.car_state USING btree (time_stamp DESC);


--
-- Name: ix_car_state_num_time; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX ix_car_state_num_time ON public.car_state USING btree (car_state_number, time_stamp);


--
-- Name: car_state ts_insert_blocker; Type: TRIGGER; Schema: public; Owner: postgres
--

CREATE TRIGGER ts_insert_blocker BEFORE INSERT ON public.car_state FOR EACH ROW EXECUTE FUNCTION _timescaledb_internal.insert_blocker();


--
-- Name: bounding_box bounding_box_cone_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.bounding_box
    ADD CONSTRAINT bounding_box_cone_id_fkey FOREIGN KEY (cone_id) REFERENCES public.cones(cone_id) ON DELETE CASCADE;


--
-- Name: cone_state cone_state_cone_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.cone_state
    ADD CONSTRAINT cone_state_cone_id_fkey FOREIGN KEY (cone_id) REFERENCES public.cones(cone_id) ON DELETE CASCADE;


--
-- Name: formula_state_from_left formula_state_from_left_current_car_state_car_time_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.formula_state_from_left
    ADD CONSTRAINT formula_state_from_left_current_car_state_car_time_fkey FOREIGN KEY (current_car_state, car_time) REFERENCES public.car_state(car_state_number, time_stamp) ON DELETE CASCADE;


--
-- Name: formula_state_from_left formula_state_from_left_left_cones_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.formula_state_from_left
    ADD CONSTRAINT formula_state_from_left_left_cones_fkey FOREIGN KEY (left_cones) REFERENCES public.cone_state(cone_state_number) ON DELETE CASCADE;


--
-- Name: formula_state_from_right formula_state_from_right_current_car_state_car_time_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.formula_state_from_right
    ADD CONSTRAINT formula_state_from_right_current_car_state_car_time_fkey FOREIGN KEY (current_car_state, car_time) REFERENCES public.car_state(car_state_number, time_stamp) ON DELETE CASCADE;


--
-- Name: formula_state_from_right formula_state_from_right_right_cones_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.formula_state_from_right
    ADD CONSTRAINT formula_state_from_right_right_cones_fkey FOREIGN KEY (right_cones) REFERENCES public.cone_state(cone_state_number) ON DELETE CASCADE;


--
-- PostgreSQL database dump complete
--

