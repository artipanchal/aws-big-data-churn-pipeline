#!/bin/bash
set -e

LOGDIR="$HOME/pipeline/logs"
mkdir -p "$LOGDIR"
LOGFILE="$LOGDIR/pipeline_$(date +%F_%T).log"

echo "Pipeline started at $(date)" | tee -a "$LOGFILE"

$HOME/spark/bin/spark-submit \
  --conf "spark.hadoop.fs.s3a.aws.credentials.provider=com.amazonaws.auth.DefaultAWSCredentialsProviderChain" \
  $HOME/pipeline/scripts/churn_etl.py \
  2>&1 | tee -a "$LOGFILE"

echo "Pipeline completed at $(date)" | tee -a "$LOGFILE"
