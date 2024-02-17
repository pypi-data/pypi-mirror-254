FROM python:3.9-slim


# Install system dependencies
# and create a `geovisio` user, to run the app as non root user
RUN apt update \
    && apt install -y git \
    && pip install waitress \
    && rm -rf /var/lib/apt/lists/* \
    && mkdir -p /opt/geovisio /data/geovisio \
    && useradd -m -u 1000 geovisio \
    && chown -R geovisio /opt/geovisio /data/geovisio

WORKDIR /opt/geovisio
USER geovisio

# Install Python dependencies
COPY ./README.md ./LICENSE ./pyproject.toml ./
COPY ./geovisio/__init__.py ./geovisio/
RUN pip install -e . --user

# Add source files
COPY ./images ./images/
COPY ./docker/docker-entrypoint.sh ./
COPY ./geovisio ./geovisio
COPY ./migrations ./migrations

# Environment variables
ENV FLASK_APP=geovisio
ENV DB_URL="postgres://user:pass@host/dbname"
ENV FS_URL="osfs:///data/geovisio"
ENV PICTURE_PROCESS_DERIVATES_STRATEGY="ON_DEMAND"

# Expose service
EXPOSE 5000
ENTRYPOINT ["./docker-entrypoint.sh"]
