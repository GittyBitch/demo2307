#!/bin/bash

echo "Willkommen bei WSL"

bucket=dasistunscherbugget
cidr=15.0.0.0/24

vpc_id=$(aws ec2 create-vpc --cidr-block $cidr --query Vpc.VpcId --output text)
read -n1 -p "weiter"
aws ec2 delete-vpc --vpc-id $vpc_id


#aws s3 mb s3://$bucket
#aws s3 ls 
#aws s3 rb s3://$bucket


