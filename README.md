# DnD Class, Race and Name Generator
A Repository containing my files and commits for a school database for my character generator project.

## Contents
1. [Ansible](#ansible)
2. [Risk Assessment](#riskassess)
3. [Jira Reports](#jirareports)
4. [Problems](#problems)


## Ansible <a name="ansible"></a>

![Ansible starting](/readme_images/ansible1.png)

In this image I am running the code that will start the ansible process. Within the Ansible vm I have connected it via SSH keys to the three vms I wish to configure. I have done so in a way that I will not have to install docker to two of my vms and nginx on another.


![Ansible running](/readme_images/ansible2.png)


![Ansible finished](/readme_images/ansible3.png)


![proof of nginx on load balancer vm](/readme_images/ansible4.png)

This is an image on my load balancer vm showing that nginx was installed after the ansible code had finished running.


![proof of docker on docker manager vm](/readme_images/ansible5.png)

This is an image of my docker manger, showing that docker is installed


![proof of docker on docker worker vm](/readme_images/ansible6.png)

Lastley this is an image of my docker worker showing that docker is installed.


The use of ansible greatly cut down the time and repitiveness of setting up each of these vms.



## Risk Assessment <a name="riskassess"></a>

Some risks I have taken into consideration when designing this project are:
- Scope
  - I was aware of the timeframe I had to design and implement my coding for this project. I would make sure that I could get to an MVP before trying to go further.
- Scalability
  - While it is not necessarily something I have to worry about for this piece of work I am aware that scalability could at some point become an issue with a similar project to this is a company setting. Using GCP I could easily upgrade the vms, and docker stacks to allow for a higher number of replicas and so traffic.
- CSRF Attacks
  - To help prevent these I have included the use of a secret key that is hidden within the environment and unable to be accessed.
- DDOS Attacks
  - While there is not much I can do to prevent this I am aware they could be a problem. As this is a small project a way to prevent the server being overloaded is to not give out the IP and access to the web address.



## Jira Reports <a name="jirareports"></a>

![Burndown Chart](/readme_images/sprint_burndown_chart.PNG)

Above is one of the charts created by jira that represents one of my burndown reports from a sprint. Visually it is not very useful as I was setting a single epic per sprint really which just shows I finished it in time rather than having a stepped approach to finishing. This is something I should consider for the future.



## Problems <a name="problems"></a>

I ended up running into a couple of problems throughout the course of this project.

###### Testing
I of course created tests for each of my functions within each app and API. This however came with some issues. I had errors that I could not fix that would not allow me to run the tests. I tried for hours to fix these and did so to no avail.

![tests of the server](/readme_images/testing1.png)

Here are my tests for the server. I used get.mock and post.mock to simulate values that it wouldn't be able to draw from elsewhere in the program during testing. As far as I can tell they are all written correctly however 


![tests of the basic APIs](/readme_images/testing3.png)

Here you can see my tests for the class_api app. Once again I had the same issues as previously mentioned. saying it could not find the module flask, when it was installed in my current venv. In this image I have written tests to check that it gets a server response of 200, meaning it has reached the webpage without any errors.


![tests of the name_api](/readme_images/testing4.png)

Here are my tests for the name_api application. Once again I had identical errors to the previous tests, within these tests I wrote tests to check the response to each of the sent information from both the race and class lists to ensure that the right result was gained.


###### Docker Swarm

My last error whcih ultimately broke me was with docker swarm. I tried for hours once again to fix this and ultmiately failed, resulting in the inability to deploy my application. I created a swarm that generated 3 replicas of each of the apps and spread them across the manager and the worker. It did so perfectly fine. However it would create the server replicas but immediately close them. Resulting in the inability to access the application at all.

![docker swarm error](/readme_images/testing5.png)

Here is the image for proof of this.

