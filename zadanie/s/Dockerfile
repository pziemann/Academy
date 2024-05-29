# Stage 1: Build environment with Alpine and dependencies
FROM alpine:3.17 AS build-env

WORKDIR /app

COPY requirements.txt app.py config.cfg /app/

# Install Python 3, pip, development headers (for psycopg2), gcc, and musl-dev
RUN apk add --no-cache python3 py3-pip python3-dev postgresql-dev gcc musl-dev

# Install dependencies using pip
RUN pip3 install -r requirements.txt

# Stage 2: Final Busybox image
FROM busybox:latest
WORKDIR /app
# Copy application and Python dependencies from build stage
COPY --from=build-env /usr/lib/python3.10 /lib/
COPY --from=build-env /usr/lib/libpython3.10.so /lib/
COPY --from=build-env /usr/lib/libpython3.10.so.1.0 /lib/
COPY --from=build-env /usr/lib/libpython3.so /lib/


COPY --from=build-env /usr/bin/python /bin/
COPY --from=build-env /usr/bin/python-config /bin/
COPY --from=build-env /usr/bin/python3.10 /bin/
COPY --from=build-env /usr/bin/python3.10-config /bin/
COPY --from=build-env /usr/bin/python3 /bin/
COPY --from=build-env /usr/bin/python3-config /bin/

ENV PYTHONPATH=/usr/lib/python3.10
COPY --from=build-env /app /app

# Set the default command (optional)
#CMD ["python3", "app.py"]