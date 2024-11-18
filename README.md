# Bharath_challenge

# Prerequisites 
1. Docker Desktop must be installed
2. Need AWS acc key and ID with required Ec2 full access role attached
3.  update the aws-cli/.aws/config and credentials file with right AWS user  details

steps 



1. Run the following commands
   
 ### Host the ansible contianer to run the configuration playbooks
    cd ansible-docker
    docker build -t ansible-container . ### it will create the ansible image 
    docker run  -it --rm -v ${pwd}/playbooks:/ansible/playbooks -v  ${pwd}/inventory:/ansible/inventory -v ${pwd}/web-config-files:/web-server-config -v ~/.ssh:/root/.ssh  -v ${pwd}/aws-cli/.aws:/root/.aws ansible-container


  ### Run the following commands in side the Ansible container 

     cd /ansible/playbooks
     ansible-playbooks ec2_aws.yaml   ### To host the Ec2 and create the cert as well as Inv file for next playbooks
     ansible-playbooks -i /ansible/inventory/ec2_inventory.ini ec2_install_docker.yaml ## To Install Docker service on Ec2 
     ansible-playbooks -i /ansible/inventory/ec2_inventory.ini ec2_deploy_web.yaml   ## Install Web server as Docker container ( so it will be easy to scaleup the service )
   
  # Validate the Server infra by using the serverSpec 

     docker build -t serverspec-test serverspec-infratest/.
     docker run -it --rm  -v ${pwd}/serverspec-infratest:/serverspec   -v ${pwd}/inventory/abk-key-pair.pem:/root/.ssh/private_key.pem  -e TARGET_HOST=<Ec2 Public IP >  serverspec-test
     
  ## Access the Web page from system URL 

    http://<Ec2_public_IP>:8080 ## this is redirect to https://
     
     
