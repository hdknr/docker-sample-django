#!/bin/bash
SERVICE=djdocker
PROFILE=spindd
CLUSTER=services
#
aws ecs update-service --force-new-deployment --service $SERVICE --cluster $CLUSTER --profile $PROFILE