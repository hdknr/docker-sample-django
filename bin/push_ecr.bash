#!/bin/bash
# Build Docker Image and push it to ECR
ECR=$AWS_ID.dkr.ecr.$AWS_REGION.amazonaws.com
DOCKERFILE=Dockerfile
#
# https://dev.classmethod.jp/articles/aws-cli-v2-ecr-get-login-password/
aws ecr get-login-password | docker login --username AWS --password-stdin $ECR
docker build -t $REPO --platform x86_64 -f docker/deployment/$DOCKERFILE .
docker tag $REPO:latest $ECR/$REPO:latest
docker push $ECR/$REPO:latest
