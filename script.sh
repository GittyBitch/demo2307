#!/bin/bash

echo "Willkommen bei WSL"

bucket=dasistunscherbugget

aws s3 mb s3://$bucket
aws s3 ls 
aws s3 rb s3://$bucket


