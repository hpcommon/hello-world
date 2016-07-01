"fast script execute"
import os
import sys
import json
import logging

log = logging.getLogger(__name__)

def execute(arg):
    log.info('execute param:' + arg)
    jsonObj = json.loads(arg)
    content = jsonObj['content']
    type = str(jsonObj['type'])
    taskId = jsonObj['taskId']
    param = jsonObj['param']
    fileName = ''
    cmd = ''
    if('python'==type):
        fileName=taskId+'.py'
        if(param):
            cmd = 'python '+os.getcwd()+'/'+fileName+' '+param
        else:
            cmd = 'python '+os.getcwd()+'/'+fileName
    elif('shell'==type):
        fileName=taskId+'.sh'
        if(param):
            cmd = 'sh ' + os.getcwd() + '/' + fileName + ' ' + param
        else:
            cmd = 'sh ' + os.getcwd() + '/' + fileName
    file=open(fileName,'w')
    file.write(content)
    file.close
    log.info('fileName:' + fileName)
    log.info('cmd:' + cmd)
    result =  __salt__['cmd.run'](cmd)
	log.info('script-'+result)
    return result

if __name__=='__main__':
    j = '{"content":"hello world","type":"python","taskId":"script_exe1","param":" i am param"}'
    execute(j)

	{"content":"import sys\ndef hh(arg):\n    print arg\n    return arg\nif __name__ == '__main__':\n    s = sys.argv[1]\n    hh(s)","param":"hello","taskId":"script_exe145","type":"python"}
