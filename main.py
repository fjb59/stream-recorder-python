#
import requests
import datetime



def recordstream(url,**tParameters):
    #records a mp3 stream. it probably does other formats  too but as it saves to mp3

    tm = datetime.datetime.now()
    filename = f"{tm.strftime('%Y-%m-%d-%H-%M')}.mp3"
    print (f"Creating {filename}")
    r = requests.get(url, stream=True)

    with open(filename, 'wb') as f:
        try:
            for block in r.iter_content(1024):
                f.write(block)
        except KeyboardInterrupt: #this forces  my stream grabber to close on ctrl +c
            f.close()
            print("closed")
            quit(0)


if __name__ == '__main__':

    stream_url = 'http://149.255.59.3:8009/stream.mp3'

    recordstream(stream_url)
