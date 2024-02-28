-- Schema
DROP TABLE IF EXISTS student;
CREATE TABLE student (
  id           serial PRIMARY KEY,
  first_name   varchar NOT NULL,
  last_name    varchar  NOT NULL,
  age           integer,
  subject       integer REFERENCES subjects(id)
);


DROP TABLE IF EXISTS subjects;
CREATE TABLE subjects (
  id           serial PRIMARY KEY,
  subject    varchar NOT NULL
);


DROP TABLE IF EXISTS teachers;
CREATE TABLE teachers (
  id           serial PRIMARY KEY,
  first_name   varchar NOT NULL,
  last_name    varchar  NOT NULL,
  age           integer,
  subject       integer REFERENCES subjects(id)
);

