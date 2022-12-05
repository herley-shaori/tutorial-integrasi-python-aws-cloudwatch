import watchtower, logging

logging.basicConfig(filename="logDemo.log",
                    format='%(asctime)s %(levelname)s %(message)s',
                    filemode='a')
FORMATTER = logging.Formatter("%(asctime)s — %(name)s — %(levelname)s — %(message)s")


logger = logging.getLogger(__name__)

def infoLogs(pesanLogs):
    logger.addHandler(watchtower.CloudWatchLogHandler(log_group_name='aplikasi_satu',log_stream_name='info'))
    logger.setLevel(logging.INFO)
    logger.info(pesanLogs)
    logger.handlers.clear() 

def errorLogs(pesanLogs):
    logger.addHandler(watchtower.CloudWatchLogHandler(log_group_name='aplikasi_satu',log_stream_name='error'))
    logger.setLevel(logging.ERROR)
    logger.error(pesanLogs)
    logger.handlers.clear()

infoLogs('proses dimulai.')
errorLogs('galat.')
infoLogs('proses selesai.')