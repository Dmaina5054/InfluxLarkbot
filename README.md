<strong>#InfluxLarkbot</strong>

<h1>Description</h1>
We want to create a service that sends alert messages to a larkbot through webhook.
To achieve this, we need to prepare the data to be sent as a message.
We shall interact with our influxdb service and fetch data from the buckets.
We clean the data and send it as a payload in a POST request to the webhook url.
<br/>
</hr>

<h4>Notes:</h4>

We need to control the alerts to avoid alert panic.
Implement an asyncio pattern and cache influxdb results. We shall check if result in cache  before sending as alarm data to bot- control rate limit.
Implement celery beat to allow us control workflow run behavior.

<h3> Core Implementations</h3>

1. Fetch data from influxdb
    - query influxdb api and pass influx query as payload
    - Call cache function

2. Cache Function
    - Define an alarm key from influx call result
    - Check if key exists in redis db
    - If exists ignore calling sendalert function
    - If ! exists, call sendalert funtion and pass alarm message as payload

2. SendAlert Function
    - based on cache funtion result, send POST request to webhook url
    - pass cache function result as payload


<h2>Celery Implementation</h2>
We shall use Celery as task runner and scheduler. We shall then define a celery beat to control number of runs for our workflow.


<h2>Celery Workers as Daemons</h2>

For production environment we shall set more than one worker. The workers should be daemonized so that they are started automatically at server startup.

    1. create a new service definition file in /etc/systemd/system/celeryd.service
    2. Create a /etc/default/celeryd configuration file
    3. Create log and pid directories:

</hr>

<h2>Daemonizing Celery</h2>
We need two services:
    <ol>
    <li>Celery Beat Service</li>
    <li>Celeryd service</li>
    </ol>

Create log and pid directories:
<code>
sudo mkdir /var/log/celery /var/run/celery
sudo chown $USER:$USER /var/log/celery /var/run/celery
</code>
Reload systemctl daemon. You should run this command each time you change the service definition file.

<code>sudo systemctl daemon-reload</code>

Enable the services to startup at boot:

<h3>Celery Beat Service</h4>
<code>sudo systemctl enable celeryd</code>

<h3>Celery Beat Service</h4>
<code>sudo systemctl enable celerybeat</code>

</hr>


<h2>Starting the services</h2>

<code>sudo systemctl start celeryd</code>
<code>sudo systemctl start celeryd</code>



