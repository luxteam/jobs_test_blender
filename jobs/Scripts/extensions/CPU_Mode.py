def enable_cpu_mode():
    render_device_settings = get_user_settings().final_devices
    set_value(render_device_settings, 'cpu_state', True)
    render_device_settings.gpu_states[0] = False