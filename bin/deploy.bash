#!/bin/bash
CLUSTER="${ECS_PREFIX}-cluster-${ECS_APP}"
SERVICE="${ECS_PREFIX}-service-${ECS_APP}"
#
aws ecs update-service --force-new-deployment --service $SERVICE --cluster $CLUSTER