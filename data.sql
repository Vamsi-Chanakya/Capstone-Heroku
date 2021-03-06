--
-- PostgreSQL database dump
--

-- Dumped from database version 12.1
-- Dumped by pg_dump version 12.1

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
-- Data for Name: Actor; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public."Actor" (id, name, age, gender) FROM stdin;
1	Chadwick Boseman	42	male
2	Tom Holland	23	male
3	Robert Downey Jr.	55	male
4	Scarlett Johansson	35	female
5	Brie Larson	30	female
6	Gwyneth Paltrow	47	female
7	Jon Favreau	53	male
\.


--
-- Data for Name: Movie; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public."Movie" (id, title, release_date) FROM stdin;
1	Black Panther	2018-01-29
2	Spider-Man: Homecoming	2017-06-28
3	Avengers: Infinity War	2018-04-23
4	Captain Marvel	2019-02-27
5	Iron Man 3	2013-04-14
\.


--
-- Data for Name: Casting; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public."Casting" (id, actor_id, movie_id) FROM stdin;
1	1	1
2	2	2
3	3	3
4	4	3
5	5	4
6	6	3
7	6	5
8	7	5
\.


--
-- Name: Actor_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public."Actor_id_seq"', 7, true);


--
-- Name: Casting_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public."Casting_id_seq"', 8, true);


--
-- Name: Movie_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public."Movie_id_seq"', 5, true);


--
-- PostgreSQL database dump complete
--
