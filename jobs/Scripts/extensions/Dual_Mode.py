def enable_dual_mode():
	render_device_settings = get_user_settings().final_devices
	render_device_settings.gpu_states[0] = True
	set_value(render_device_settings, 'cpu_state', True)