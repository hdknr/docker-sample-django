#!/bin/bash
# Build Docker Image and push it to ECR
REPO=djdocker
REGION=ap-northeast-1
PROFILE=spindd
AWS_ID=$1               # AWS ID
ECR=$AWS_ID.dkr.ecr.$REGION.amazonaws.com
DOCKERFILE=Dockerfile
#
#aws ecr get-login-password --profile $PROFILE --region $REGION  | docker login --username AWS --password-stdin $ECR
docker build -t $REPO -f docker/deployment/$DOCKERFILE .
docker tag $REPO:latest $ECR/$REPO:latest
#docker push $ECR/$REPO:latest
