"""Extract plain text content of the HTML string.
- input: HTML text in the `html` field
- output: plaintext in the `text` field
"""

from hashlib import md5
import datetime
from email.utils import formatdate
from time import mktime
import trafilatura

extracted = trafilatura.extract(document["html"])
cleaned = extracted.replace('\n', ' ').replace('¶', ':').replace('\"', "'")

document["text"] = cleaned
fingerprint = md5(cleaned.encode('utf-8')).hexdigest()
if "fingerprint" != document.get("fingerprint"):
    document["fingerprint"] = fingerprint
    timestamp = mktime(datetime.datetime.now().timetuple())
    document["modified"] = formatdate(timeval=timestamp, localtime=False, usegmt=True)
