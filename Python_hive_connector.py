import subprocess
tables=raw_input("enter the name of the table")
p=subprocess.Popen("hive -f /tmp/python_poc/my_hql.hql"+" --hiveconf x="+tables,shell=True,
                 stdout=subprocess.PIPE,
                 stderr=subprocess.PIPE)
out, err = p.communicate()
print(out)
if err==None:
    print "successfull"
else:
    print(err)
    print "not successfull"
