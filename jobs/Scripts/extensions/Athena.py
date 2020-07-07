def set_clean_false():
    with open('C:/Users/user/AppData/Roaming/Blender Foundation/Blender/2.83/scripts/addons/rprblender/config.py', 'r') as file:
        data = file.readlines()
    i = 0
    for s in data:
        if("clean_athena_files = True" in s):
            data[i] = "clean_athena_files = False\n"
            break
        i += 1

    with open('C:/Users/user/AppData/Roaming/Blender Foundation/Blender/2.83/scripts/addons/rprblender/config.py', 'w') as file:
        file.writelines(data)

def set_clean_true():
    with open('C:/Users/user/AppData/Roaming/Blender Foundation/Blender/2.83/scripts/addons/rprblender/config.py', 'r') as file:
        data = file.readlines()
    i = 0
    for s in data:
        if("clean_athena_files = False" in s):
            data[i] = "clean_athena_files = True\n"
            break
        i += 1

    with open('C:/Users/user/AppData/Roaming/Blender Foundation/Blender/2.83/scripts/addons/rprblender/config.py', 'w') as file:
        file.writelines(data)

def validate_athena():
    athena_files = os.listdir("C:/Users/user/AppData/Local/Temp/rprblender")
    if(not athena_files):
        copyfile(path.join('..', '..', '..', '..', 'jobs_launcher', 'common', 'img', 'error.jpg'), path.join(WORK_DIR, 'Color', 'BL28_RS_ATH_001.jpg'))
    # this is separate from try except, because athena_file.read() causes exception
    with open("C:/Users/user/AppData/Local/Temp/rprblender/" + athena_files[0], "r") as athena_file:
        print("Athena file content:")
        print(athena_file.read())
    try:
        with open("C:/Users/user/AppData/Local/Temp/rprblender/" + athena_files[0], "r") as athena_file:
            data = json.load(athena_file)
            copyfile(path.join(WORK_DIR, '..', '..', '..', '..', 'jobs_launcher', 'common', 'img', 'passed.jpg'), path.join(WORK_DIR, 'Color', 'BL28_RS_ATH_001.jpg'))
    except Exception as e:
        print(e)
        copyfile(path.join(WORK_DIR, '..', '..', '..', '..', 'jobs_launcher', 'common', 'img', 'error.jpg'), path.join(WORK_DIR, 'Color', 'BL28_RS_ATH_001.jpg'))
