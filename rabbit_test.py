
import rabbitpy

def publish(channel):
    body = "Hello world!"
    message = rabbitpy.Message(channel, body, {'content_type': 'text/plain'})
    delivered = message.publish('rabbitpy-tests', 'ha-routing-key', mandatory=True)

    if delivered:
        print('Message delivered')
    else:
        print('Delivery failed')

if __name__ == '__main__':
    # I have created a new admin user "test" with password "test"
    # The below is the IP of the proxy
    url = "amqp://test:test@192.168.0.221:5672/"
    try:
        with rabbitpy.Connection(url) as connection:
            with connection.channel() as channel:
                # enabled publisher confirms
                channel.enable_publisher_confirms()
                publish(channel)
    except rabbitpy.exceptions.MessageReturnedException as ex:
        print('Failed to publish')
    except KeyboardInterrupt:
        print('exiting...')