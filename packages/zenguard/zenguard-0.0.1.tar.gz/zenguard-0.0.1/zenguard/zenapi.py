import sys
import socketio

class ZenError(Exception):
    pass

class zen_client ():
  def __init__(self, api_key):
    # try: 
      self.host = 'http://localhost:8080/'
      self.api_key = api_key
      self.connected = False
      self.listening = True

      self.ws = socketio.Client()

      print("Connecting to ZenGuard Server...")
      self.ws.connect(self.host)
      print("Connected sucessfully, verifying API key...")
      self.ws.emit('zenapi_key', {"api_key": self.api_key})

      @self.ws.event
      def zenapi_key_success(data):
          if (not self.connected):
            self.connected = True
            self.uid = data["id"]
            print(f'Successfully logged in as user {self.uid}!')
            self.stop_listening()

      @self.ws.event
      def zenapi_key_error(data):
          if (not self.connected):
            self.ws.disconnect()
            self.stop_listening()
            raise ZenError(data["error"])
  
      while self.listening:
          self.ws.sleep(1)
      self.listening = True

  def stop_listening(self):
    self.listening = False

  def listen(self):
    while self.listening:
        self.ws.sleep(1)
    self.listening = True

  def guardrail (self, message):
      if (self.connected):
        self.ws.emit('zenapi_message', {"message": message, "id": self.uid})

        @self.ws.event
        def zenapi_message_success(data):
            self.output = data
            self.stop_listening()

        @self.ws.event
        def zenapi_message_error(data):
            print('error')
            self.stop_listening()
            self.ws.disconnect()
            raise ZenError(data["error"])

        while self.listening:
          self.ws.sleep(1)
        return self.output

      else:
        raise ZenError('Client is not connected!')


