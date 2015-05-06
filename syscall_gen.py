all_types = list()
input_file = open("/usr/include/x86_64-linux-gnu/asm/unistd_64.h", "r")
for line in input_file:
	if "#define __NR_" in line:
		syscall_base = line.split("#define __NR_")[1].split()[0]
		syscall_number = line.split("#define __NR_")[1].split()[1]
		syscall_func = "sys_" + syscall_base + "\t"
		file2 = open("tags", "r")
		for line2 in file2:
			if syscall_func in line2:
				arg_list = line2.split("signature:")[1].replace("(","").replace(")","").replace("__user","").replace("const","").replace("* ","*").replace("* ","*").split(",")
				arg_number = len(arg_list)
				final_arg_list = list()
				for item in arg_list:
					if len(item.split()) == 0:
						arg_name = ""
						arg_type = "VOID"
					elif len(item.split()) == 1:
						arg_name = ""
						arg_type = item.split()[0]
					elif (len(item.split()) == 2) and (item.split()[0] == "unsigned") and (item.split()[1] in ["int","long","char"]):
							arg_name = ""
							type_list = item.split()
							arg_type = ' '.join(type_list)
					else:
						arg_name = item.split()[-1]
						type_list = item.split()
						del type_list[-1]
						arg_type = ' '.join(type_list)

					if "*" in arg_name: 
						final_arg_list.append(("PT", arg_type))
					else:
						#print(arg_name)
						final_arg_list.append(("ST", arg_type))
					if not (arg_type.upper() in all_types):
						all_types.append(arg_type.upper())
		syscallent_file = open("syscall_info.h", "a")
		syscallent_file.write( "[" + syscall_number + "] = { " + str(arg_number) )
		for arg in final_arg_list:
				syscallent_file.write(", {" + str(arg[0]) + ", " + str(arg[1]).upper() + "}")
		syscallent_file.write(" }\t/* " + syscall_func.replace("\t","") + " */\n")
new_file = open("types.txt", "a")
new_file.write(', '.join(all_types)) 
