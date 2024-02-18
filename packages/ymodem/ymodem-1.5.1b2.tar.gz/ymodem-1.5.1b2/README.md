![ymodem-logo](https://raw.githubusercontent.com/alexwoo1900/ymodem/master/docs/assets/ymodem-logo.png)

Fork of the YMODEM project by [alexwoo1900](https://github.com/alexwoo1900/ymodem)
Now available on PyPi, also now it can be used as cli tool for Serial ports
The YMODEM project is based on XMODEM implementation written by tehmaze. 
It is also compatible with XMODEM mode.


[![license](https://img.shields.io/github/license/mashape/apistatus.svg)](https://opensource.org/licenses/MIT)
[![PyPI Version](https://img.shields.io/pypi/v/ymodem?label=PyPI&logo=pypi)](https://pypi.org/project/ymodem/)

README: [ENGLISH](https://github.com/alexwoo1900/ymodem/blob/master/README.md) | [简体中文](https://github.com/alexwoo1900/ymodem/blob/master/README_CN.md)

- [**Installation**](#installation)
- [**Usage**](#usage)
  - [CLI TOOL](#cli-tool) 
    - [Sending a batch of files](#sending-a-batch-of-files)
    - [Receive a file](#receive-a-file)
  - [Demo](#demo)
  - [Interact with SecureCRT](#interact-with-securecrt)
  - [Quick start](#quick-start)
- [API](#api)
  - [Create MODEM Object](#create-modem-object)
  - [Send files](#send-files)
  - [Receive files](#receive-files)
  - [Debug](#debug)
- [Changelog](#changelog)
- [License](#license)

## Installation
```Bash
pip install ymodem
```

## Usage

### CLI TOOL

```Bash
# To get help
ymodem -h
# or
python -m ymodem -h
```

#### Sending a batch of files
```Bash
ymodem send ./file.bin ./file2.bin -p COM4 -b 115200
# or
python -m ymodem send ./file.bin ./file2.bin -p COM4 -b 115200
```

#### Receive a file
```Bash
ymodem recv ./ -p COM4 -b 115200
# or
python -m ymodem recv ./ -p COM4 -b 115200
```



## Demo

### Test the sending and receiving functions

If you want to run the test sample, please do the following:
1. use virtual serial port tool to generate COM1 and COM2 that can communicate
2. run the FileReceiver.py and FileSender.py on the command line

The specific transmission process is shown in the following figure:
![SenderAndReceiver](https://raw.githubusercontent.com/alexwoo1900/ymodem/master/docs/assets/console_test.gif)

### Interact with SecureCRT

Interact with SecureCRT as sender
![SecureCRT1](https://raw.githubusercontent.com/alexwoo1900/ymodem/master/docs/assets/sender.gif)

Interact with SecureCRT as Finder
![SecureCRT2](https://raw.githubusercontent.com/alexwoo1900/ymodem/master/docs/assets/receiver.gif)

## Quick start

```python
from ymodem.Socket import ModemSocket

# define read
def read(size, timeout = 3):
    # implementation

# define write
def write(data, timeout = 3):
    # implementation

# create socket
cli = ModemSocket(read, write)

# send multi files
cli.send([file_path1, file_path2, file_path3 ...])

# receive multi files
cli.recv(folder_path)
```

For more detailed usage, please refer to the demo/FileReceiver.py and demo/FileSender.py files.

## API

### Create MODEM Object

```python
def __init__(self, 
             read: Callable[[int, Optional[float]], Any], 
             write: Callable[[Union[bytes, bytearray], Optional[float]], Any], 
             protocol_type: int = ProtocolType.YMODEM, 
             protocol_type_options: List[str] = [],
             packet_size: int = 1024,
             style_id: int = _psm.get_available_styles()[0]):
```
- protocol_type: Protocol type, see Protocol.py
- protocol_type_options: such as g representing the YMODEM-G in the YMODEM protocol.
- packet_size: The size of a single packet, 128/1024 bytes, may be adjusted depending on the protocol style
- style_id: Protocol style, different styles have different support for functional features

### Send files

```python
def send(self, 
         paths: List[str], 
         callback: Optional[Callable[[int, str, int, int], None]] = None
        ) -> bool:
```

- callback: callback function. see below.

    Parameter | Description
    -|-
    task index | index of current task
    task (file) name | name of the file
    total packets | number of packets plan to send
    success packets | number of packets successfully sent

### Receive files

```python
def recv(self, 
         path: str, 
         callback: Optional[Callable[[int, str, int, int], None]] = None
        ) -> bool:
```

- callback: callback function. Same as the callback of send().

## Debug

If you want to output debugging information, set the log level to DEBUG.

```python
logging.basicConfig(level=logging.DEBUG, format='%(message)s')
```

## Changelog

### v1.5.1b1 (2024/02/03)

- Added additional options to cli tool

### v1.5.1b0 (2024/02/03)

- Added cli tool to iteract with YMODEM via Serial bus
- Fix of transaction end logic in send()

### v1.5 (2023/05/20 11:00 +00:00)

- Rewritten send() and recv()
- Support YMODEM-G. 
    The success rate of YMODEM-G based on pyserial depends on the user's OS, and after testing, the success rate is very low without any delay.

## License
[MIT License](https://opensource.org/licenses/MIT)