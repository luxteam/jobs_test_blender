def setError(case):
    work_dir = path.join(
        WORK_DIR, 'Color', case['case'] + case.get('extension', '.jpg'))
    source_dir = path.join(WORK_DIR, '..', '..', '..',
                           '..', 'jobs_launcher', 'common', 'img')

    copyfile(path.join(source_dir, 'error.jpg'), work_dir)

def render_animation(case, frame_start, frame_end, check_frame):
    logging('Render animation')
    event('Prerender', False, case['case'])

    bpy.data.scenes['Scene'].frame_start = frame_start
    bpy.data.scenes['Scene'].frame_end = frame_end
    start_time = datetime.datetime.now()
    bpy.ops.render.render(write_still=True, animation=True)
    render_time = (datetime.datetime.now() - start_time).total_seconds()
    print(WORK_DIR)
    if (os.path.exists(
        os.path.join(WORK_DIR, 'Color', case['case'] + check_frame + '.jpg')
        )):
        os.rename(os.path.join(WORK_DIR, 'Color', case['case'] + check_frame + '.jpg'), os.path.join(WORK_DIR, 'Color', case['case'] + '.jpg'))
    else:
        setError(case)
        
    event('Postrender', True, case['case'])

    reportToJSON(case, render_time)