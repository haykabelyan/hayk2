
pip install allure-pytest
pytest -v --alluredir=allure-results
allure --version
allure serve allure-results/
allure generate -c allure-results/ -o allure-reports 


$ pytest -m smoke.

/////////////////////////////////////////////////////

pip install requests pytest

pip freeze
pip freeze > requirements.txt

site-page
api-endpoint


/////////////////////////////////////////////////////
UBUNTU
sudo apt install default-jdk
apt search openjdk


https://github.com/allure-framework/allure2/releases
tar -zxvf allure-2.17.3.tgz
sudo mv allure-2.17.3 /opt/allure



sudo nano /etc/environment
JAVA_HOME="/usr/lib/jvm/java-11-openjdk-amd64"
nano ~/.bashrc
export JAVA_HOME="/usr/lib/jvm/java-11-openjdk-amd64"
echo $JAVA_HOME
