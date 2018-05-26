#!/bin/sh
echo $PROJECT_DIR
DOCKFILE=$PROJECT_DIR/Dockerfile
echo $DOCKFILE
docker build -t mytest -f $DOCKFILE  $PROJECT_DIR
