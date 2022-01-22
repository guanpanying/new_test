import configparser
import logging

log=logging.getLogger(__name__)

def get_jk_config(choose):
	config=configparser.ConfigParser()
	config.read(os.path.join(os.getcwd(),’jenkins_server.ini’))
	username=config.get(choose,’username’)
	password=config.get(choose,’host’)
	port=config.get(choose,’port’)
	url=“http://“+host+”:”+port
	return url, username, password
class JenkinsDemo:
	def __init__(self,job_name,choose=‘jenkins’):
		self.job_name=job_name
		config=get_jk_config(choose)
		self.jk=Jenkins(*config,useCrumbe=True)
	def __get_job_from_keys(self):
		choose_list=[]
		print(self.jk.keys())
		for my_job_name in self.jk.keys():
			if self.job_name in my_job_name:
				choose_list.append(my_job_name)
		return choose_list
	def __job_build(self,my_job_name):
		if self.jk.has_job(my_job_name):
			my_job=self.jk.get_job(my_job_name)
			if not my_job.is_queued_or_running():
				try:
					last_buil=my_job.get_last_buildnumber()
				except:
					last_build=0
				build_num=last_build+1