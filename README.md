# Docker_K8s_Python_Webservice 
A Project for deploying a simple python microservices into Docker and K8s
Required tools
==============
python 3.x and pip 

creating python virtual environments 
===============================================
below are the commands for git bash 
python -m venv tutorial-env (creating virtual environment)
source tutorial-env/scripts/activate  (activating the virtual environment)

Installing python extensions for vs code
==========================================
python(microsoft)

Creating a sample flask application
=============================================
Install flask 
We recommend using the latest version of Python. Flask supports Python 3.9 and newer.
recomended to create a virtual environment which we have already done 
next install flask using below command 
pip install Flask
pip list (to list the number of python packages installed)

flask is by default run on port 5000 , we can set to 80 if we want 
http://192.168.1.4:5000 -> add / at the end of the link to see the app open in browser like below 
http://192.168.1.4:5000/ 

using jinja templating we have rendered web pages and displayed hostname and ip of the system the app is running on 
render template is what we are using 

pip freeze - command to get the dependencies used in running this python application
pip freeze - to check dependencies 
pip freeze > requirements.txt (redirecting it to a file) the file will get created under source we can move it werever we want
anyone who wants to install dependencies can use below command to install 
 pip install -r requirements.txt

 eval $(minikube docker-env) -> to create the image inside the docker on minikkube instead of local 
 so that kubernetes can acess the image without having to push it into docker hub or registry 

 eval $(minikube docker-env -u) > this is the commant o switch back to pc docker daemon
 docker info -> command to check before changing avfter chaging or just info of docker in general 
 
 it didn't work for me to access from my web browser after running conatiner inside minikube we will see let me create deployment and see 

 docker build -t webapp:1.0 .
 docker run -d -p 80:5000 --name web webapp:1.0 
 
 when . is used in below statements it means the docker file is in current work directory and the docker file name is as defualt Dockerfile 
 build: 
    context : .

if not then we will need to mention docker file name which we have given like below 
build: 
    context : .
    dockerfile : mydockerfile
if we use above for default docker file also no problem 
below are docker compose commands 
docker-compose build -> to build the image 
docker-compose up -d -> to up the containers and all the stck in compose file 
docker-compose down -> to bring down and remove all stacks 

docker@minikube:~$ curl http://localhost:8080/
<p>Hello, World!</p>docker@minikube:~$
docker@minikube:~$ 


kubectl apply -f service.yml
kubectl apply -f deployment.yml
kubectl delete service service_name 



minikube service pythonweb-service --> without this servicde i was unable to access it in the browser of my system was only able to access inside minikube 
running above produces below output and wen i do ctrl c the browser cant access minikube ip again 
|-----------|-------------------|-------------|---------------------------|
| NAMESPACE |       NAME        | TARGET PORT |            URL            |
|-----------|-------------------|-------------|---------------------------|
| default   | pythonweb-service |        8080 | http://192.168.49.2:31269 |
|-----------|-------------------|-------------|---------------------------|
🏃  Starting tunnel for service pythonweb-service.
|-----------|-------------------|-------------|------------------------|
| NAMESPACE |       NAME        | TARGET PORT |          URL           |
|-----------|-------------------|-------------|------------------------|
| default   | pythonweb-service |             | http://127.0.0.1:55690 |
|-----------|-------------------|-------------|------------------------|
🎉  Opening service default/pythonweb-service in default browser...
❗  Because you are using a Docker driver on windows, the terminal needs to be open to run it.
✋  Stopping tunnel for service pythonweb-service.

(tutorial-env)


we can also do something called as port forwarding 
kubectl port-forward service/pythonweb-service 8080:8080

It creates a live tunnel between your local machine and the Kubernetes service.
This tunnel lasts only as long as the command is running.
When you stop the command, the port-forwarding stops immediately.

Browser on your host
     |
     |  localhost:8080
     V
kubectl port-forward (local tunnel)
     |
     |  port 8080 on service/pythonweb-service
     V
Service in Kubernetes (port 8080)
     |
     |  targetPort 5000
     V
Pod(s) running your app (listening on 5000)

make sure helm cli is installed 
helm version -> command 
helm create webapp-python -> command to create helm chart 
helm template webapp-python -> command to render the helm chart and see what will be created 
helm install pyhelmwebapp webapp-python -> Helm installs the chart webapp-python into your Kubernetes cluster with release name pyhelmwebapp
helm  list -> command to check the installed releases 
helm uninstall pyhelmwebapp -> to uninstall the release 


