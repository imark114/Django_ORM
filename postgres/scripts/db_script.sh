#!/bin/sh

export PGUSER="postgres"

psql -c "CREATE DATABASE inventory"

psql inventory -c "CREATE EXTENSION IF NOT EXISTS \"uuid-ossp\";"

psql inventory -c "CREATE SCHEMA inventory_schema"

psql inventory -c "CREATE SCHEMA inventory_management_schema"

psql inventory -c "ALTER DATABASE inventory SET search_path TO inventory_schema, inventory_management_schema"