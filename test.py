a = '<a target="blank" href="http://olk81jnmn.bkt.clouddn.com/00{index}.jpg"><img src="http://olk81jnmn.bkt.clouddn.com/00{index}.jpg"></a>'
for i in range(0, 10):
    print a.format(index=i+1)