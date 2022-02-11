#!/bin/bash
#After destructive attack (clean_db)
docker-compose down
docker-compose up --force -d
