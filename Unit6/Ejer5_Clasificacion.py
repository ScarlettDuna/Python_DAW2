with open("files/log_errores.txt", "r", encoding="utf-8") as log:
    with (open("files/log-info.txt", "w", encoding="utf-8") as info,
          open("files/log-warning.txt", "w", encoding="utf-8") as warning,
          open("files/log-error.txt", "w", encoding="utf-8") as error):
        for line in log:
            if "[INFO]" in line:
                info.write(line)
            elif "[ERROR]" in line:
                error.write(line)
            elif "[WARNING]" in line:
                warning.write(line)
