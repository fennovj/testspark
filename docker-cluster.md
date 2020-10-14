# Cluster in Docker

You can also run a cluster locally in Docker. This saves you from having to install Java, running multiple processes, etcetera.

Note that Docker is intended for running non-distributed applications on a single host. So this is mainly for local testing purposes.

I used the Spark image maintained and updated by bitnami. You can find more details and instructions here: <https://hub.docker.com/r/bitnami/spark/>

A quick default docker-compose.yml can be found here: <https://github.com/bitnami/bitnami-docker-spark/blob/master/docker-compose.yml> Running that will start a local cluster with two workers. Note that the two workers have 1 core and 1GB of memory each. So if that's too much or too little, make some changes there.

This works like normal with findspark, findspark will be able to find the local cluster just fine.
