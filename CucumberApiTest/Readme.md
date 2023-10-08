### Solution Approach
for this solution the stack used is **Java** and **Cucumber**.
check in your local if you already have these configurations, otherwise you can install
with the following configurations described below.

**Simple configurations**

check if you already have Java installed with the following command 

```
java -version
```
Install Java 
```
sudo apt install oracle-java#-installer
```
[Java](https://www.oracle.com/java/technologies/downloads/#java11)

Cucumber installation, Maven dependencies

[Install Cucumber](https://cucumber.io/docs/installation/java/)


### REST API Automation

tests for the “pet/findPetsByStatus" endpoint and a CRUD using the following API automated checks in DEMO PET STORE: https://petstore.swagger.io/

• Get "available" pets. Assert expected result

• Post a new available pet to the store. Assert new pet added.

• Update this pet status to "sold". Assert status updated.

• Delete this pet. Assert deletion.
