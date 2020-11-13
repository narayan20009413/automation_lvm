import os
while True:
	os.system("clear")
	os.system("tput setaf 9")
	print("\t\t\tWelcome to LVM automation program")
	os.system("tput setaf 3")
	print("\t-------------------------------------------------------------")
	os.system("tput setaf 2")	
	print("\t\tpress 1 : To see all disk attached to OS");
	print("\t\tpress 2 : To see all mounted device");
	print("\t\tpress 3 : To create a physical volume");
	print("\t\tpress 4 : To create a volume group");
	print("\t\tpress 5 : To create  a logical volume");
	print("\t\tpress 6 : To see about a physical volume (PV)");
	print("\t\tpress 7 : To see about a Volume group(VG)");
	print("\t\tpress 8 : To see about a logical volume (LV) ");
	print("\t\tpress 9 : To format a logical volume");
	print("\t\tpress 10: To  mount logical volume");
	print("\t\tpress 11: To exit");
	os.system("tput setaf 7")
	ch=int(input("Enter your choice : "))
	if ch==1:
		os.system("fdisk -l")
	elif ch==2:
		os.system("df -h")	
	elif ch==3:
		x=input("Enter your disk name: ");
		os.system("pvcreate {}".format(x))	
	elif ch==4:
		vgname=input("Enter the name  which you want to give to VG:")
		y=input("Enter the PV separated by space: ")
		os.system("vgcreate {} {}".format(vgname,y))
	elif ch==5:
		size=input("Enter the size for LV: ")
		lvname=input("Enter name for LV: ")
		vgname=input("Enter name of VG: ")
		os.system("lvcreate --size {} --name {} {}".format(size,lvname,vgname))
	elif ch==6:
		pvname=input("Enter physical volume(PV): ")
		os.system("pvdisplay {}".format(pvname))	
	elif ch==7:
		vgname=input("Enter name of volume group(VG): ")
		os.system("vgdisplay {}".format(vgname))	 
	elif ch==8:
		lv=input("Enter path of LV: ")
		os.system("lvdisplay {}".format(lv))		 
	elif ch==9:
		lv=input("Enter the logical volume which you want to Format: ")
		os.system("mkfs.ext4 {}".format(lv))
	elif ch==10:
		folder=input("Enter name for folder: ")
		lv=input("Enter the logical volume which you want to mount: ")
		os.system("mkdir /{}".format(folder))
		os.system("mount {} /{}".format(lv,folder))	 
	elif ch==11:
		exit()
	else:
		print("Wrong choice! please enter the choice again")
	input("Please enter to continue.....")

   



