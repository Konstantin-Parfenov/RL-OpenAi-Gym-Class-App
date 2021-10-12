# RL-OpenAi-Gym-Class-App

___

## File Structure
* app_name
  * app.py: Flask REST API application
  * env.py: MoveToBeacon1D class  
  * Dockerfile: Base image is alpine3.8 with python3.7
  * .dockerignore: Descriptions for docker to ignore files and folders
  * requirements.txt: List of packages that the app will import
  * test_env.py: Unit_test for env class

## Testing the API locally
1. Run the Flask API locally for testing. Go to directory with `app.py`.

```bash
python app.py
```
2. In a new terminal window, use HTTPie to make a GET request at the URL of the API.

```bash
http http://127.0.0.1:5000/ input==1
```
3. Example of successful output.

```bash
HTTP/1.0 200 OK
Content-Length: 121
Content-Type: application/json
Date: Tue, 12 Oct 2021 11:28:25 GMT
Server: Werkzeug/2.0.2 Python/3.7.3

{
    "Current reward experienced by the agent": 0.8519167602062225,
    "Location of agent on the x axis": -0.14808323979377747
}
```

## Testing the API in Docker
1. Build the container from Docerfile. Go to directory with Dockerfile.
```bash
docker build -t flask:flask_v3 .
```
2. Run the container.
```bash
docker run -P flask:flask_v3
```

3. Start Docker CLI for the container and use curl installed on the image to test

```bash
/ # curl 127.0.0.1:5000/?input=-1
```
4. Example of successful output.

```bash
{"Location of agent on the x axis": 0.75, "Current reward experienced by the agent": 0.25}
```
