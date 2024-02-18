name_fs = "[%(name)s] "
location_fs = "(%(module)s.%(funcName)s:%(lineno)d) "
message_fs = "%(message)s"
default_format_string = f"%(asctime)s.%(msecs)03d [%(levelname)s] {name_fs}{location_fs}{message_fs}"
