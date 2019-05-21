Web_resourses = ['/jabba','/nothing','/']


def availability(resours):
    availability_flag = False
    for res in Web_resourses:
        if resours == res:
            availability_flag = True
    print('Our resourses',Web_resourses)
    return availability_flag


def check_post(post):
    import re
    check_result = False
    check_str = post[1:]
    if re.match("^[a-z]*$", check_str):
        check_result = True
    else:
        check_result = False
    if len(check_str) > 6:
        check_result = False
    else:
        pass
    return check_result


def application(environ, start_response):
    out_string = b'Hello world from a simple WSGI application!'
    if environ['REQUEST_METHOD'] == 'GET':
        if availability(environ['REQUEST_URI']):
            pass
            start_response('200 OK', [('Content-Type', 'text/plain')])
            if environ['REQUEST_URI'] == '/':
                pass
            if environ['REQUEST_URI'] == '/nothing':
                out_string = b'nothing more'
            if environ['REQUEST_URI'] !='/nothing' and environ['REQUEST_URI'] != '/':
                friend = environ['REQUEST_URI'][1:]
                print('friend',friend)
                out_string = b'Hell0 ' + friend.encode('utf-8') 
        else:
            out_string = b'No resours'
            start_response('404', [('Content-Type', 'text/plain')])

    # ~ print('Our resourses',Web_resourses)

    if environ['REQUEST_METHOD'] == 'POST':
        if check_post(environ['REQUEST_URI']):
            if availability(environ['REQUEST_URI']):
                start_response('205 Reset Content', [('Content-Type', 'text/plain')])
                out_string = b'reset post'
            else:
                Web_resourses.append(environ['REQUEST_URI'])
                out_string = b'post accepted'
                start_response('201 Created', [('Content-Type', 'text/plain')])
                print('Our new resourses',Web_resourses)
        else:
            start_response('205 Reset Content', [('Content-Type', 'text/plain')])
            out_string = b'reset post'
    # print('--'*50,'\n', environ,'\n', '--'*50,'\n')
    return [out_string]
