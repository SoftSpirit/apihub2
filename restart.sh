#!/usr/bin/env bash
docker-compose pull
docker-compose up -d
bash migrate.sh