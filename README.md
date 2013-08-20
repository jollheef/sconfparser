sconfparser
===========

### Installation

	$ git clone https://github.com/jollheef/sconfparser/
	$ cd sconfparser
	$ sudo python3 setup.py install

### Examples

#### Create config

	>>> from sconfparser import SConfParser
	>>> config = SConfParser()
	>>> config.firstvar = "12345"
	>>> config['secondvar'] = "67890"
	>>> config
	{'firstvar': '12345', 'secondvar': '67890'}
	>>> config.write("/tmp/myconfig")
	λ> cat /tmp/myconfig 
	firstvar = 12345
	secondvar = 67890

#### Read config

	>>> from sconfparser import SConfParser
	>>> config = SConfParser("/tmp/myconfig")
	>>> config
	{'firstvar': '12345', 'secondvar': '67890'}

#### Read multiple config

	>>> from sconfparser import SConfParser
	>>> config = SConfParser()
	>>> config.read("/tmp/myconfig")
	>>> config
	{'firstvar': '12345', 'secondvar': '67890'}
	>>> config.read("/tmp/fconfig")
	>>> config
	{'a': 'hello world', 'firstvar': '12345', 'b': 'true', 'secondvar': '67890'}

#### Print all variables

	>>> for var in config:
	...     print(var + " = " + config[var])
	... 
	a = hello world
	firstvar = 12345
	b = true
	secondvar = 67890

#### Remove from config

	>>> config
	{'a': 'hello world', 'firstvar': '12345', 'b': 'true', 'secondvar': '67890'}
	>>> del config.a
	>>> config
	{'firstvar': '12345', 'b': 'true', 'secondvar': '67890'}
