from datetime import datetime


class Logger:
    """
    self-written 'module' for storing logs and printing their into terminal output
    class: Logger
    """

    def _write_to_file_(self, msg) -> None:
        """
        Func that receive text msg and paste it into log file in './logs/{now date}.log file'
        :param msg: test message to log
        :return: None
        """
        with open(f"logs/{datetime.now().date()}.log", "a") as f:
            f.write(datetime.now().strftime("%m/%d/%Y, %H:%M:%S") + " - " + msg + "\n")

    @staticmethod
    def log(msg: str) -> None:
        """
        got log and print it into terminal and file
        :param msg: text
        :return: None
        """
        print(msg)
        logger._write_to_file_(msg)


logger = Logger()
