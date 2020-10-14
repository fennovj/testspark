# Installing Spark locally and getting it working

Basic instructions here: <https://phoenixnap.com/kb/install-spark-on-ubuntu>

First, check the latest version here: <https://spark.apache.org/downloads.html>

Then, run something like:

```bash
sudo apt install default-jdk scala git -y
wget https://downloads.apache.org/spark/spark-3.0.1/spark-3.0.1-bin-hadoop2.7.tgz
tar xvf spark-*
sudo mv spark-3.0.1-bin-hadoop2.7 /opt/spark
echo "export SPARK_HOME=/opt/spark" >> ~/.bashrc
echo "export PATH=$PATH:$SPARK_HOME/bin:$SPARK_HOME/sbin" >> ~/.bashrc
echo "export PYSPARK_PYTHON=/usr/bin/python3" >> ~/.bashrc
```

Commands to run it:

```bash
start-master.sh  # Run the master. View the master at localhost:8080
start-slave.sh url  # Run a worker
start-slave.sh -c 1 -m 512M  # Run a worker with limited cpu/memory
spark-shell  # Scala shell
pyspark  # Python shell
stop-master.sh  # Stop the master
stop-slave.sh  # Stop the worker
start-all.sh, stop-all.sh  # Starts both master and worker
# start-all, stop-all may complain about port 22. If so, run 'service ssh restart'
```

## Working in a virtual environment

The simplest showcase is:

```bash
python3 -m virtualenv env
source env/bin/activate
pip install pandas  # For example
export PYSPARK_PYTHON=/path/to/project/env/bin/python
pyspark # Starts a python session in the virtual environment
```

Note that pyspark did not need to be installed in the new virtual env, it is by default when starting pyspark

Also note that this does not run on the 'cluster' that we started in the previous chapter. Instead it runs in a local process that mimics a cluster. To configure it to connect to a cluster, we have to do: `pyspark --master spark://XXX.localdomain:7077`. Here, the full url can be seen on the page at `localhost:8080`.

## Submitting a job

The python code should contain a line like: `spark = SparkSession.builder.getOrCreate()` to initialize the session. (In pyspark interactive, this is done automatically)

While running a job, you can view the logs at localhost:4040. See below to configure historical logging:

```bash
spark-submit python_example.py  # Run a python file in spark without historical logging

mkdir /tmp/spark-events  # Default log location, must be created
SPARK_URL='spark://XXX.localdomain:7077'  # You can find this url at localhost:8080
spark-submit --master $SPARK_URL --conf spark.eventLog.enabled=true python_example.py
```

To view the job history: `start-history-server.sh`. Now browse to localhost:18080. You can stop the history server with `stop-history-server.sh`

## Summary

```bash
# Quick start:
source env/bin/activate
export PYSPARK_PYTHON=env/bin/python
start-all.sh && start-history-server.sh

# Now we can run interactively, or run jobs
# This is assuming SPARK_URL is already set, for example in ~/.bashrc
pyspark --master $SPARK_URL
spark-submit --master $SPARK_URL --conf spark.eventLog.enabled=true python_example.py

# To close:
stop-history-server.sh && stop-all.sh
```
