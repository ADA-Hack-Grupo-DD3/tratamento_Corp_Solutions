EMPLOYEE = """employee (
                id SERIAL PRIMARY KEY,
                name VARCHAR(100),
                gender VARCHAR(10),
                age INTEGER,
                study VARCHAR(20),
                state VARCHAR(20),
                time NUMERIC(5, 2),
                department VARCHAR(20),
                seniority varchar(20),
                entry_age NUMERIC(5, 2)
            )"""