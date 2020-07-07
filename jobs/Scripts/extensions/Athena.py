CONFIG_PATH = 'C:/Users/user/AppData/Roaming/Blender Foundation/Blender/2.83/scripts/addons/rprblender/config.py'
ATHENA_DIR = 'C:/Users/user/AppData/Local/Temp/rprblender/'

def set_clean_false():
    with open(CONFIG_PATH, 'r') as file:
        data = file.readlines()
    i = 0
    for s in data:
        if("clean_athena_files = True" in s):
            data[i] = "clean_athena_files = False\n"
            break
        i += 1

    with open(CONFIG_PATH, 'w') as file:
        file.writelines(data)

def set_clean_true():
    with open(CONFIG_PATH, 'r') as file:
        data = file.readlines()
    i = 0
    for s in data:
        if("clean_athena_files = False" in s):
            data[i] = "clean_athena_files = True\n"
            break
        i += 1

    with open(CONFIG_PATH, 'w') as file:
        file.writelines(data)

def validate_athena(case):
    athena_files = os.listdir(ATHENA_DIR)
    if(not athena_files):
        copyfile(path.join(WORK_DIR, '..', '..', '..', '..', 'jobs_launcher', 'common', 'img', 'error.jpg'), path.join(WORK_DIR, 'Color', case['case'] + ".jpg"))
    # this is separate from try except, because athena_file.read() causes exception
    with open(ATHENA_DIR + athena_files[0], "r") as athena_file:
        print("Athena file content:")
        print(athena_file.read())
    try:
        with open(ATHENA_DIR + athena_files[0], "r") as athena_file:
            data = json.load(athena_file)
            copyfile(path.join(WORK_DIR, '..', '..', '..', '..', 'jobs_launcher', 'common', 'img', 'passed.jpg'), path.join(WORK_DIR, 'Color', case['case'] + ".jpg"))
    except Exception as e:
        print(e)
        copyfile(path.join(WORK_DIR, '..', '..', '..', '..', 'jobs_launcher', 'common', 'img', 'error.jpg'), path.join(WORK_DIR, 'Color', case['case'] + ".jpg"))
