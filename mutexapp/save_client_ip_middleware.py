import datetime
from models import Userlog

class SaveClientIpMiddleware(object):
    """
        Save the client's IP address 
    """
    def process_request(self, request):
        print "The ip middleware is getting processed."
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.spli(',')[-1].strip()
        else:
            ip = request.META.get('REMOTE_ADDR')
        try:
            Userlog.objects.get(client_ip=ip)
        except Userlog.DoesNotExist:
            ip_address = Userlog(client_ip=ip, visiting_time=datetime.datetime.now())
            ip_address.save()
        return None