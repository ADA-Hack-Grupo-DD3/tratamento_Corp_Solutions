EMPLOYEE = """employee (
                id SERIAL PRIMARY KEY,
                name VARCHAR(100),
                gender VARCHAR(20),
                age INTEGER,
                race VARCHAR(20),
                study VARCHAR(20),
                state VARCHAR(20),
                time NUMERIC(5, 2),
                department VARCHAR(40),
                seniority varchar(20),
                entry_age NUMERIC(5, 2)
            )"""