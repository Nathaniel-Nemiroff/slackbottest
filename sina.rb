require 'sinatra'
require 'json'
require 'rubypython'
require 'json'


get '/' do
    RubyPython.start
    sys = RubyPython.import('sys')
    sys.path.append('.')
    sb=RubyPython.import('slackbot')
    sb.sendMsg('sent from ruby')
    RubyPython.stop
    "hello world"
end

post '/' do
    dat = params['action']
    postdata= JSON.parse(request.body.read)
    RubyPython.start
    sys = RubyPython.import('sys')
    sys.path.append('.')
    sb=RubyPython.import('slackbot')
    sb.sendMsg(postdata)
    RubyPython.stop
    "hello world"
end
