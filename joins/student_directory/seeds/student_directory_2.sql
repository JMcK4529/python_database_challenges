DROP TABLE IF EXISTS students;
DROP TABLE IF EXISTS cohorts;

CREATE TABLE cohorts (
  id SERIAL PRIMARY KEY,
  name text,
  starting_date date
);

CREATE TABLE students (
  id SERIAL PRIMARY KEY,
  name text,
  cohort_id int,
  constraint fk_cohort foreign key(cohort_id) references cohorts(id) on delete cascade
);

INSERT INTO cohorts (name, starting_date) VALUES ('A1', '2020-01-01');
INSERT INTO cohorts (name, starting_date) VALUES ('B1', '2021-01-01');
INSERT INTO cohorts (name, starting_date) VALUES ('B2', '2021-02-01');

INSERT INTO students (name, cohort_id) VALUES ('Johnny Test', 3);
INSERT INTO students (name, cohort_id) VALUES ('Susan Test', 2);
INSERT INTO students (name, cohort_id) VALUES ('Mary Test', 2);
INSERT INTO students (name, cohort_id) VALUES ('Andy Notha-Test', 1);
INSERT INTO students (name, cohort_id) VALUES ('Yetta Notha-Test', 1);