#!/bin/bash
#
#
CLUSTER="${ECS_PREFIX}-cluster-${ECS_APP}"
SERVICE="${ECS_PREFIX}-service-${ECS_APP}"
CONTAINER="${ECS_PREFIX}-container-${ECS_APP}"
# 
TASK_ARN=$(aws ecs list-tasks --cluster ${CLUSTER} --service-name ${SERVICE} | jq -r ".taskArns[0]")
echo "@@@ TASK_ARN ${TASK_ARN}"
# 
SERVICE_ENABLED=$(aws ecs describe-services --cluster ${CLUSTER} --services ${SERVICE} | jq '.services[].enableExecuteCommand')
echo "@@@ SERVICE ENABLED ${SERVICE_ENABLED}"

TASK_ENABLED=$(aws ecs describe-tasks --cluster ${CLUSTER} --tasks ${TASK_ARN}  | jq '.tasks[].enableExecuteCommand')
echo "@@@@ TASK ENABLED ${TASK_ENABLED} for ${TASK_ARN}"

#cat << EOS
aws ecs execute-command  \
    --cluster ${CLUSTER} \
    --task "${TASK_ARN}" \
    --container ${CONTAINER} \
    --interactive \
    --command "/bin/bash"
#EOS