# CADMUS - Backend services

## Dependencies
- Docker v20.10.21
- docker-compose v2.13.0
- Ubuntu 20.04 OR Git Bash
- AWS SAM CLI v1.88

## Config files
 This section contains a description of the various configuration files we use to store information on the orchestration of things like containers, deployments, and testing.

### [lib/logging_config/config.py](./lib/logging_config/config.py)
Contains the logging configuration properties for all Python services and libraries. See the [structlog](https://www.structlog.org/en/stable/index.html) for more information.

### [.env](./.env)
Contains environment variables that are injected into Docker containeres used in *local* development and testing. DO NOT ADD REAL CREDENTIALS TO THIS FILE. Use our [AWS Secrets Manager](https://us-gov-west-1.console.amazonaws-us-gov.com/secretsmanager/listsecrets?region=us-gov-west-1) to store any sensitive information. See the [.env documentation](https://docs.docker.com/compose/environment-variables/env-file/) for more information.

### [pytest.ini](./pytest.ini)
Contains pytest configuration options. See the [pytest.ini documentation](https://docs.pytest.org/en/stable/reference/customize.html#pytest-ini) for more information.

### [conftest.py](./conftest.py)
Contains pytest fixtures that are shared throughout the entire test suite. See the [conftest.py documentation](https://docs.pytest.org/en/6.2.x/fixture.html#conftest-py-sharing-fixtures-across-multiple-files) for more information.


### [samconfig.toml](./samconfig.toml)
Contains configuration options when deploying services using the AWS SAM CLI. See the [samconfig.toml documentation](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-config.html) for more information.

### [template.yaml](./template.yaml)
Contains CloudFormation deployment instructions that are used by the AWS SAM CLI. See the [CloudFormation documentation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/template-formats.html) for more information.

## Local Development
[docker-compose.yaml](./docker-compose.yaml) is used to both build and start containers locally. 

### Credentials
As stated above we are storing sensitive credentials using the AWS Secrets Manager. However, some credentials used for local development, such as those for accessing AWS resources, need to be stored locally. After configuring the CLI, you can export AWS credentials to your shell by adding the following to your `~/.bashrc`:
```shell
if [ ! -f $HOME/.pypirc ]; then
        pypiconf="$HOME/.pypirc"
        pypisecret=$(aws secretsmanager get-secret-value --secret-id cadmus_pypi_api_upload_token --query SecretString --output text)
        touch "$pypiconf"
        echo "[pypi]" > "$pypiconf"
        echo "  username = __token__" >> "$pypiconf"
        echo "  password = $pypisecret" >> "$pypiconf"
fi
export AWS_ACCESS_KEY_ID=$(aws configure get default.aws_access_key_id)
export AWS_SECRET_ACCESS_KEY=$(aws configure get default.aws_secret_access_key)
export AWS_DEFAULT_REGION=$(aws configure get default.region)
```
Note that this uses the `default` profile's credentials. You can modify the profile if you want to use a different set of credentials for your containers. This may not be necessary for all services or even APIs but some, such as downloading CDMs from SpaceTrack locally, require access to the AWS Secrets Manager to retrieve credentials for the SpaceTrack account.
### Building containers
#### Building all images
```shell
$ docker-compose build
```
#### Building a single container locally
```shell
$ docker-compose build db
```
#### Starting the entire cluster locally
```shell
$ docker-compose up
```
#### Starting a single container locally
```shell
$ docker-compose up db
```
#### List of available services with:
```shell
$ docker-compose config --services
```

### Logging
By default the Python logging is configured to only display severity levels of INFO or greater. This is the default behavior for non-development environment but it is useful to have more detailed logs for debugging purposes. You can control the level of logging for the development environment by updating the `CADMUS_LOGLEVEL` environment variable found in the [.env](./.env) file.


## Deployment
### Lambda functions
We are using the AWS SAM CLI to deploy stacks to the AWS Cloudformation service. [samconfig.toml](./samconfig.toml) contains the different staging environments and the default environment is stage. Once deployed, the stacks can be monitored on the [Cloudformation console](https://console.amazonaws-us-gov.com/cloudformation/home?region=us-gov-west-1#/stacks?filteringText=&filteringStatus=active&viewNested=true).
#### Build the containers to deploy
```shell
$ sam build --use-container
```
#### Deploy the containers to stage
```shell
$ sam deploy
```
### Database
Make sure you run any new SQL against the local database and test it prior to running against the staging and production databases. See [database README](lib/db/db_management/README.md) for more info on how to do that. 

## Testing
### Unit Testing
The `lib` module, which contains common code for various services in the project, is installed by default in the `base` image so any container that uses the `base` image can be used for unit testing, including the `base` image itself. In the example below, we will do unit testing in the `ingest` container. If you are testing a specific service, be sure to start that container instead.
```shell
# build and start the container
$ docker-compose build ingest
$ docker-compose up -d ingest db

# run the entire test suite
$ docker exec -it cadmus-ingest pytest


# run tests recursively under a directory
$ docker exec -it cadmus-ingest pytest ./my_dir/tests

# run all tests that match a pattern
$ docker exec -it cadmus-ingest pytest -k "test_something"
```

### Flask Testing
Many of our services are Flask apps, which have endpoints. In order to test these locally, there are two types of HTTP methods we are currently using. 

To test `GET` endpoints:
```shell
# start the service
$ docker-compose up ingest
# wait for the service to start and grab the URL from the output, there should be a line that says something like:
cadmus-ingest  |  * Running on http://127.0.0.1:5000
# test the endpoint via curl or the browser
$ curl http://127.0.0.1:5000/ingest/test
```

To test `POST` endpoints, you will need a payload to deliver to the app. There are a few that have already been created, such as [request.ingest.sh](./services/ingest/request_ingest.sh) so feel free to modify the payload found there or create your own as needed. The script can be pointed to either a locally running app or to one in the staging environment. To use it:
```shell
# start the service
$ docker-compose up ingest
# wait for the service to start and grab the URL from the output, there should be a line that says something like:
cadmus-ingest  |  * Running on http://127.0.0.1:5000
# send the payload defined in the shell script to a locally running ingest service
$ ./services/ingest/request_ingest.sh development
# send the payload defined in the shell script to the staging ingest service
$ ./services/ingest/request_ingest.sh staging
```
Some limitations/notes:
- Some endpoints can be tested locally since they don't require interaction with other AWS services while others do. We currently do not support testing endpoints that interact with other services locally so that testing should happen with staging resources. [CADMUS-480](https://omega1.omitron.com/browse/CADMUS-480) will resolve this.
- `API_GATEWAY_URL` is hard-coded into many of these scripts but may change if the API gateway has been recreated for some reason. To retrieve the latest URL check the [API Gateway console page](https://us-gov-west-1.console.amazonaws-us-gov.com/apigateway/main/apis?region=us-gov-west-1).

### Automated Testing
Not currently implemented, will be added in [CADMUS-180](https://omega1.omitron.com/browse/CADMUS-180)

### Ingest Testing
To test the CDM Parser without running it through the Flask application, a convenience script has been created at (local_ingest.py)[services/ingest/local_ingest.py].