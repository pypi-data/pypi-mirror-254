# Copyright 2024 UW-IT, University of Washington
# SPDX-License-Identifier: Apache-2.0


from commonconf import settings
from sqlalchemy import create_engine
from sqlalchemy.pool import QueuePool
from uw_person_client.databases import AbstractDatabase


URL_PATTERN = \
    "postgresql+psycopg2://{username}:{password}@{host}:{port}/{database}"


class Postgres(AbstractDatabase):

    def create_engine(self):
        url = URL_PATTERN.format(
            username=getattr(settings, "UW_PERSON_DB_USERNAME"),
            password=getattr(settings, "UW_PERSON_DB_PASSWORD"),
            host=getattr(settings, "UW_PERSON_DB_HOSTNAME"),
            port=getattr(settings, "UW_PERSON_DB_PORT"),
            database=getattr(settings, "UW_PERSON_DB_DATABASE")
        )
        self.engine = create_engine(
            url,
            logging_name="sqlalchemy.engine",
            pool_logging_name="sqlalchemy.pool",
            poolclass=QueuePool,
            pool_size=getattr(settings, "UW_PERSON_DB_POOL_SIZE", 2),
            max_overflow=getattr(settings, "UW_PERSON_DB_MAX_OVERFLOW", 5),
            pool_recycle=getattr(settings, "UW_PERSON_DB_POOL_RECYCLE", 600)
        )
