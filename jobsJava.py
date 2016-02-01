import getopt
import sys
import requests
import xml.etree.ElementTree as ET 
 
############################## The START of functions ####################################

def load_config_xml(file_name, job_name):
    print("Changing the config.xm at the job: " + job_name)
    url = serverUrl + "job/" + job_name + '/' + file_name  
    update_request = requests.post(url, data=open(file_name,'rb'))

def modification_jdk(jdk_ver):
    print("Modification of JDK")
    tree = ET.parse('config.xml')
    root = tree.getroot()
    root.find('jdk').text = "JDK " + jdk_ver
    tree.write('config.xml')    
      
def existing_jdk_check(jdk_ver, jdk_list):
    print("Checking if the given JDK exists")
    if (jdk_ver in jdk_list):
        return True 
    else:
        usage()     
 
def the_same_jdk_check(job_name, jdk_ver):
    print("Checking if the given JDK isn't already set")
    url = serverUrl + "job/" + job_name + '/' + 'config.xml'
    with open('config.xml','wb') as handle:
        response = requests.get(url, stream=True)
        for block in response.iter_content(1024):
	    handle.write(block)
    tree = ET.parse('config.xml')
    root = tree.getroot()  
    jdk = root.find('jdk').text
    jdk = jdk[4:]
    if (jdk_ver == jdk):
        print("The same JDK version is set")
        usage
    else:
        return True 
    
def job_name_check(job_name):
    print("Checking if the "+ job_name + " exists.")
    url = serverUrl + "job/" + job_name +'/'
    job_request = requests.head(url)
    if (job_request.status_code == 200):
        return True
    else:
        usage() 
    
def usage():
    usage="""
     -j<jobsName> -x<jdkVersion>
     -j First option takes 1 argument
     -x Second option takes 1 argument
    """
    print(usage)
    sys.exit(2)

def main(argv):
    args_count = 0
    try:
        opts, args = getopt.getopt(argv, "j:x:h", ["jobName=", "jdkVer=", "help"])
    except getopt.GetoptError as err:
        print(str(err))
        usage()
        sys.exit(2)
    for o,a in opts:
        if o in ("-h","--help"):
            usage()
            sys.exit()
        elif o in ("-j", "--jobName"):
            args_count += 1
        elif o in ("-x", "--jdkVer"):
            args_count += 1
        else:
            assert False, "unhandled option"
    return args_count
        
############################## The END of functions #######################################

my_jdk_list = ('1.8.0_66','1.8.0_20','1.7.0_79','1.7.0_80','1.7.0_55')

serverUrl = "http://jenkins-server.local:8080/"

args = main(sys.argv[1:])

if ( args == 2):
    job_name_check(sys.argv[2])
    the_same_jdk_check(sys.argv[2], sys.argv[4])
    existing_jdk_check(sys.argv[4], my_jdk_list)
    modification_jdk(sys.argv[4])
    load_config_xml('config.xml',sys.argv[2])
else:
    usage()
