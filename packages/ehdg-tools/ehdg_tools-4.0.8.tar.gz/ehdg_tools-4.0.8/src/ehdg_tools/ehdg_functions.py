import subprocess


# check whether there is input commandline program or not
def check_commandline_program(program_name):
    check_cmd = f"{program_name} --version"
    try:
        check_output = subprocess.check_output(check_cmd, shell=True)
        check_output = check_output.decode('utf-8')
        print(check_output)
        is_there_program = True
        print(f"{program_name} is found.")
    except Exception as error:
        print(error)
        is_there_program = False
    return is_there_program
