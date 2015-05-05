# syscall-_arg-table
To Generate the syscall table:
1) Generate a "tag" file for the syscalls.h file.
sudo ctags --fields=S --c-kinds=+pc /"kernel_path"/include/linux/syscalls.h
2) Execute the python script
python syscall_gen.py

There are two outputs files:
syscall_info.h: It contains the defintion of the syscall entries.
types.txt: It contains all syscall arguments types. (The types are of the type "syscall_arg_type" defined in "syscall_param.h")
