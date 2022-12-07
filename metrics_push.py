from cwmetrics import CloudWatchMetricsBuffer
import datetime
import time

cw = CloudWatchMetricsBuffer('demo_rekapitulasi_barang')

cw.put_value('jumlah',5)
cw.put_value('terjual',1)
cw.send()
time.sleep(300)

cw.put_value('jumlah',8)
cw.put_value('terjual',5)
cw.send()
time.sleep(300)

# cw.put_value('jumlah',10)
# cw.put_value('terjual',17)
# cw.send()
