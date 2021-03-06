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

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: Actor; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."Actor" (
    id integer NOT NULL,
    name character varying(60) NOT NULL,
    age integer NOT NULL,
    gender character varying(20) NOT NULL
);


ALTER TABLE public."Actor" OWNER TO postgres;

--
-- Name: Actor_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public."Actor_id_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."Actor_id_seq" OWNER TO postgres;

--
-- Name: Actor_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public."Actor_id_seq" OWNED BY public."Actor".id;


--
-- Name: Casting; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."Casting" (
    id integer NOT NULL,
    actor_id integer,
    movie_id integer
);


ALTER TABLE public."Casting" OWNER TO postgres;

--
-- Name: Casting_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public."Casting_id_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."Casting_id_seq" OWNER TO postgres;

--
-- Name: Casting_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public."Casting_id_seq" OWNED BY public."Casting".id;


--
-- Name: Movie; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."Movie" (
    id integer NOT NULL,
    title character varying(120) NOT NULL,
    release_date date
);


ALTER TABLE public."Movie" OWNER TO postgres;

--
-- Name: Movie_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public."Movie_id_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."Movie_id_seq" OWNER TO postgres;

--
-- Name: Movie_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public."Movie_id_seq" OWNED BY public."Movie".id;


--
-- Name: alembic_version; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.alembic_version (
    version_num character varying(32) NOT NULL
);


ALTER TABLE public.alembic_version OWNER TO postgres;

--
-- Name: Actor id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Actor" ALTER COLUMN id SET DEFAULT nextval('public."Actor_id_seq"'::regclass);


--
-- Name: Casting id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Casting" ALTER COLUMN id SET DEFAULT nextval('public."Casting_id_seq"'::regclass);


--
-- Name: Movie id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Movie" ALTER COLUMN id SET DEFAULT nextval('public."Movie_id_seq"'::regclass);


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
-- Data for Name: alembic_version; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.alembic_version (version_num) FROM stdin;
2d4bafaa252a
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
-- Name: Actor Actor_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Actor"
    ADD CONSTRAINT "Actor_pkey" PRIMARY KEY (id);


--
-- Name: Casting Casting_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Casting"
    ADD CONSTRAINT "Casting_pkey" PRIMARY KEY (id);


--
-- Name: Movie Movie_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Movie"
    ADD CONSTRAINT "Movie_pkey" PRIMARY KEY (id);


--
-- Name: alembic_version alembic_version_pkc; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.alembic_version
    ADD CONSTRAINT alembic_version_pkc PRIMARY KEY (version_num);


--
-- Name: Casting Casting_actor_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Casting"
    ADD CONSTRAINT "Casting_actor_id_fkey" FOREIGN KEY (actor_id) REFERENCES public."Actor"(id) ON DELETE CASCADE;


--
-- Name: Casting Casting_movie_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Casting"
    ADD CONSTRAINT "Casting_movie_id_fkey" FOREIGN KEY (movie_id) REFERENCES public."Movie"(id);


--
-- PostgreSQL database dump complete
--