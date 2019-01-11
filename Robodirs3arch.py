import docker
from robot.api import logger
from docker.types import Mount

class Robodirs3arch(object):

    def __init__(self):
        self.client = docker.from_env()
        self.dirs3arch_docker = "dirs3arch"

    def run_dirs3arch(self, url, extensions, wordlist, results_path):
        self.url = url
        self.extensions = extensions
        self.wordlist = wordlist
        self.results_path = results_path
        results_mount = Mount("/dirs3arch_results", self.results_path, type="bind")
        #self.url = [str(self.url)]
        mounts = [results_mount]
        command = '-u {0} -e {1} -w {2} --json-report=/dirs3arch_results/dirs3arch_{0}_results.json'.format(self.url, self.extensions, self.wordlist)
        self.client.containers.run(self.dirs3arch_docker, mounts=mounts, command=command)
        logger.info("Successfully ran dirs3arch against the target URL {0}. Please find the *.json output in the results directory".format(self.url))
